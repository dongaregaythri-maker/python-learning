# Let's understand Arguments in Python. 😊

# An argument is the actual value that we pass to a function when calling it.
# Example

def addition(a, b):
    print(a + b)

addition(10, 20)

# Easy trick to remember:
# - Parameters = Variables in the function definition.
# - Arguments = Values given when calling the function.

# Positional arguments

# Values are passed according to their position.

def student(name, age):
    print(name)
    print(age)

student("Gaythri", 22)

# Here, "Gaythri" goes to name, and 22 goes to age.

# Let's test your understanding! 😎 Here's a tricky interview-style question on Positional Arguments.
# Question 1: Predict the output

def display(a, b, c):
    print(a)
    print(b)
    print(c)

display(10, 20, 30)
display(30, 10, 20)