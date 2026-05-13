# This is a basic calculator made by Ben Hughes in Python
# Please only put in integers into the program
# Addition
print("Would you like to do some addition?")
answer = input()
if answer == "yes":
    num1 = int(input("Please enter the first number you would like to add together (It has to be an integer): "))
    num2 = int(input("Please enter the second number you would like to add together: "))
    print(num1 + num2)
else:
    print("Okay, understood")
    
# Multiplication
print("Would you like to do some multiplication?")
answer = input()
if answer == "yes":
    num1 = int(input("Please enter first number you would like to times together (It has to be an integer): "))
    num2 = int(input("Please enter second number you would like to times together: "))
    print(num1 * num2)
else:
    print("Okay, understood")
    
# Division
print("Would you like to do some division?")
answer = input()
if answer == "yes":
    num1 = int(input("Please enter the first number you would like to divide (It has to be an integer): "))
    num2 = int(input("Please enter the second number you would like to divide from the first number: "))
    print(num1 / num2)
else:
    print("Okay understood")
    
# Subtraction
print("Would you like to do some subtraction?")
answer = input()
if answer == "yes":
    num1 = int(input("Please enter the first number you would like to subtract (It has to be an integer): "))
    num2 = int(input("Please enter the second number you would like to subtract from the first: "))
    print(num1 - num2)
else:
    print("Okay, understood")

# Prints regardless of anything when all if and else statements are met
print("Program finished!")
