
def reading(file):
    with open(file,'r+') as f:
        print(f.read())


def main():
    reading(r'./Sample.txt')

if __name__ == '__main__':
    main()