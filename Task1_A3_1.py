
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

def main():
    n = int(input("Enter the number: "))
    print(f"Factorial for the number {n} is {fac(n)}")
if __name__ == "__main__":
    main()