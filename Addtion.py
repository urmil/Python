
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
    user_choice = input("Would you like to add(a), subtract(s), or multiply (m) or divide(d)? ")
    if user_choice == "a":
      x = input("Please enter the first number")
      y = input("Please enter the second number")
      print (f" sum of two number x and y: {Addtion(x,y)}")
    elif user_choice == "s":
        x = input("Please enter the first number")
        y = input("Please enter the second number")
        print (f" Subtraction of two number y and x: {Subtraction(x,y)}")
    elif user_choice == "m":
        x = input("Please enter the first number")
        y = input("Please enter the second number")
        print (f" Multiplication of two number x and y: {Multiplication(x,y)}")
    elif user_choice == "d":
        x = input("Please enter the first number")
        y = input("Please enter the second number")
        print (f" Division of two number x and y: {Division(x,y)}")

if __name__ == "__main__":
    main()


