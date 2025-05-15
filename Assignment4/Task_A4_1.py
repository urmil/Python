
def reading(file):
    with open(file,'r+') as f:
       print("Reading file Content")
       num =0
       for line in f:
         num += 1
         print(f"Line {num}: {line}")


def main():
    reading(r'./Sample.txt')

if __name__ == '__main__':
    main()