
def reading(file):
    with open(file,'r+') as f:
       print(f"Final Content of the {file}: ")
       print(f.read())
       print(" ")

def writing(ud,file):
    with open(file,'w+') as f:
        #print("Writing file Content")
        f.write(ud)
        print(f"Data successfully written to {file}")
        print(" ")

def appending(ud,file):
    with open(file,'a+') as f:
        f.write(ud)
        print(f"Data successfully appended to {file}")
        print(" ")

def main():
    user_data = input("Enter text to write to the file: ")
    file = "output.txt"
    writing(user_data,file)
    user_add_data = '\n'+ input("Enter additional text to append: ")
    appending(user_add_data,file)
    reading(r'output.txt')

if __name__ == '__main__':
    main()