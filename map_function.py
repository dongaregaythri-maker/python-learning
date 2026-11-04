# Map Function (map())

# The map() function applies a given function to every element of an iterable, such as a list or tuple.

# Definition for exams:

# The map() function is a built-in Python function that applies a specified function to each item of an iterable and returns a map object.


# Syntax

# map(function, iterable)

# Map Using Lambda Function

# Example 1: Square of every number

numbers = [2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)

# Output:

# [4, 9, 16, 25]

# Example 2: Add 10 to every number

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x + 10, numbers))

print(result)

# Output:

# [11, 12, 13, 14]

# Example 3: Convert names into uppercase

names = ["ram", "riya", "priya"]

result = list(map(lambda x: x.upper(), names))

print(result)

# Output:

# ['RAM', 'RIYA', 'PRIYA']

# Example 4: Convert Celsius into Fahrenheit

celsius = [0, 10, 20, 30]

result = list(map(lambda c: (c * 9/5) + 32, celsius))

print(result)

# Output:

# [32.0, 50.0, 68.0, 86.0]

# B. Map Using Normal Function (def)

# We can also use a normal function inside map().

# Example 1: Square of every number

def square(x):
    return x ** 2

numbers = [2, 3, 4, 5]

result = list(map(square, numbers))

print(result)

# Output:

# [4, 9, 16, 25]

# Example 2: Add 10 to every number

def add(x):
    return x + 10

numbers = [1, 2, 3, 4]

result = list(map(add, numbers))

print(result)

# Output:

# [11, 12, 13, 14]

# Example 3: Convert names into uppercase

def uppercase(name):
    return name.upper()

names = ["ram", "riya", "priya"]

result = list(map(uppercase, names))

print(result)

# Output:

# ['RAM', 'RIYA', 'PRIYA']

# 6. Difference Between Map With Lambda and Normal Function

# Map with lambda

# Map with normal function

# Uses lambda directly

# Uses a separately defined function

# Shorter code

# More structured code

# Suitable for simple operations

# Suitable for reusable or complex operations

# Example:

# Lambda
result = list(map(lambda x: x * 5, numbers))

# Normal function
def multiply(x):
    return x * 5

result = list(map(multiply, numbers))