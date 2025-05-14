#Task 1
def Addtion(x,y):

 sum = int(x) + int(y)
 return sum

def Subtraction(x,y):
 subtraction = int(x) - int(y)
 return subtraction

def Multiplication(x,y):
    multiplication = int(x) * int(y)
    return multiplication
def Division(x,y):
    division = int(x) / int(y)
    return division

def main():
        x = input("Please enter the first number: ")
        y = input("Please enter the second number: ")
        print (f" Addition is: {Addtion(x,y)}")
        print (f" Subtraction is: {Subtraction(x,y)}")
        print (f" Multiplication is: {Multiplication(x,y)}")
        print (f" Division is: {Division(x,y)}")


if __name__ == "__main__":
    main()


