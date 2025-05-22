# Kia Chatbot

A voice-activated chatbot that uses wake word detection and connects to OpenAI's GPT API for intelligent responses.

## Features

- Wake word detection ("Hi Kia")
- Speech recognition for commands
- Pause detection for natural conversation flow
- Integration with OpenAI's GPT-3.5 API

## Prerequisites

- Python 3.8 or higher
- A microphone connected to your computer
- An OpenAI API key

## Installation

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the chatbot:
   ```bash
   python kia_chatbot.py
   ```
2. Say "Hi Kia" to activate the bot
3. Speak your command or question
4. Wait for a brief pause (2 seconds) for the bot to process your input
5. Listen to the response

## How it Works

1. The bot continuously listens for the wake word "Hi Kia"
2. Once activated, it starts recording your command
3. When it detects a pause in speech (2 seconds), it processes the command
4. The command is sent to OpenAI's API for processing
5. The response is printed to the console
6. The bot returns to listening for the wake word

## Troubleshooting

- Make sure your microphone is properly connected and selected as the default input device
- Check that your OpenAI API key is correctly set in the `.env` file
- Ensure you have a stable internet connection for API calls
- If you encounter issues with PyAudio installation, you may need to install portaudio:
  - On macOS: `brew install portaudio`
  - On Linux: `sudo apt-get install python3-pyaudio`