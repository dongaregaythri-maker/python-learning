# Task 1: Positive, Negative or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Example:
# Enter a number: -5
# Negative


# Task 2: Greatest Among Two Numbers


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greatest number is", num1)
elif num2 > num1:
    print("Greatest number is", num2)
else:
    print("Both numbers are equal")


# Example:
# Enter first number: 20
# Enter second number: 15
# Greatest number is 20


# Task 3: Password Check


password = input("Enter password: ")

if password == "12345":
    print("Login Successfully!")
else:
    print("Wrong Password")