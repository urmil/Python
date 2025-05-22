import speech_recognition as sr
import time
import openai
import os
import sounddevice as sd
import numpy as np
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


class KiaChatbot:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.wake_word = "hi kia"
        self.is_listening = False
        self.last_speech_time = time.time()
        self.silence_threshold = 5.0  # seconds of silence before processing

    def listen_for_wake_word(self):
        """Listen for the wake word continuously"""
        print("Listening for wake word 'Hi Kia'...")

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)

            while True:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=3)
                    try:
                        text = self.recognizer.recognize_google(audio).lower()
                        if self.wake_word in text:
                            print("Wake word detected! How can I help you?")
                            self.is_listening = True
                            self.listen_for_command()
                    except sr.UnknownValueError:
                        pass
                    except sr.RequestError:
                        print("Could not request results from speech recognition service")
                except sr.WaitTimeoutError:
                    pass

    def listen_for_command(self):
        """Listen for user commands after wake word detection"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)

            while self.is_listening:
                try:
                    print("Listening for your command...")
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=None)
                    current_time = time.time()

                    try:
                        text = self.recognizer.recognize_google(audio).lower()
                        if text:
                            print(f"You said: {text}")
                            self.last_speech_time = current_time

                            # If there's a significant pause, process the command
                            if current_time - self.last_speech_time > self.silence_threshold:
                                self.process_command(text)
                                self.is_listening = False
                                print("\nListening for wake word 'Hi Kia'...")
                                break

                    except sr.UnknownValueError:
                        # Check if silence duration exceeds threshold
                        if current_time - self.last_speech_time > self.silence_threshold:
                            print("Processing due to pause...")
                            self.is_listening = False
                            print("\nListening for wake word 'Hi Kia'...")
                            break

                except sr.WaitTimeoutError:
                    pass

    def process_command(self, command):
        """Process the command using OpenAI API"""
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Kia, a helpful AI assistant."},
                    {"role": "user", "content": command}
                ]
            )

            answer = response.choices[0].message.content
            print(f"\nKia: {answer}\n")

        except Exception as e:
            print(f"Error processing command: {e}")


def main():
    print("Starting Kia Chatbot...")
    print("Please make sure you have set your OPENAI_API_KEY in the .env file")
    chatbot = KiaChatbot()
    chatbot.listen_for_wake_word()


if __name__ == "__main__":
    main()