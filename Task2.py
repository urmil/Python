def welcome_message(fn,ln):
    print(f" Hello, {fn} {ln}! Welcome to Python Program")

def main():
    fn = input("Enter the First name: ")
    ln = input("Enter the Last Name: ")
    welcome_message(fn,ln)

if __name__ == "__main__":
     main()
