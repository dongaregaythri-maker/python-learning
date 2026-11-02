# Python provides two types:
# 1. *args
# 2. **kwargs
# 1. *args — Multiple positional arguments
# When we don't know how many arguments the user will pass, we can use *args.

# Example:

def addition(*numbers):
    print(numbers)

addition(10, 20, 30, 40)

# Why use *args?

# Normally:

# def addition(a, b):

# This function accepts only 2 arguments.

# But:

# def addition(*numbers):

# This function can accept any number of positional arguments.

# 2. **kwargs — Multiple keyword arguments:

# It allows us to pass multiple values using parameter names.

def student(**details):
    print(details)

student(name="Gaythri", age=22, city="Barshi")

# Difference between *args and **kwargs

# *args	                                         **kwargs
# Multiple positional arguments	          Multiple keyword arguments
# Stores values in a tuple	            Stores values in a dictionary
# Uses one *                              	Uses two **

