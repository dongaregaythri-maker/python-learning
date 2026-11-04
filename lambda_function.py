# 1. Lambda Function
# A lambda function is a small anonymous function written using the lambda keyword.
# It is generally used when we need a short function for a simple operation.
# Syntax:

lambda arguments: expression

# Example:

add = lambda a, b: a + b
print(add(10, 20))

# 3. Lambda Function Examples

# A. Arithmetic Operations

# 1. Addition

add = lambda a, b: a + b
print(add(10, 5))

# 2. Subtraction

sub = lambda a, b : a - b
print(sub(20,30))

# 3. Multiplication

mul = lambda a, b : a * b 
print(mul(10, 30))

# 4. Division

div = lambda a, b : a / b
print(div(20, 30))

# B. Mathematical Operations

# 1. Square of a number

square = lambda x : x ** 2 
print(square(5))

# 2. Cube of a number

cube = lambda x : x ** 3 
print(cube(3))

# 3. Square root

square_root = lambda x : x ** 0.5
print(square_rooot(5))

# Important operator:

# ** is the exponentiation operator.

# x ** 2 = Square

# x ** 3 = Cube

# x ** 0.5 = Square root

# x ** (1/3) = Cube root for non-negative numbers

# C. Conditional Statements Using Lambda

# Syntax:

# lambda arguments: value_if_true if condition else value_if_false

# 1. Even or Odd

check = lambda x: "even" if x % 2 == 0 else "odd"
print(check(10))

# 2. Positive, Negative or Zero

check = lambda x: "positive" if x > 0 else "negative" if  x < 0  else "zero"

print(check (30))
print(check (-5))
print(check (0))

# 3. Check eligibility

eligibility = lambda age : "eligible" if age>=18 else "not eligible"

print(eligibility(20))
print(eligibility(15))


# 4. Find the greater number

greater = lambda a, b: a if a > b else b

print(greater(20, 30))

# Output: 30

# 5. Find the smaller number

smaller = lambda a, b: a if a < b else b

print(smaller(20, 30))

# Output: 20

# 6. Check divisibility by 5

check = lambda x: "Divisible" if x % 5 == 0 else "Not Divisible"

print(check(25))

# Output: Divisible

# D. String Operations Using Lambda

# 1. Convert to uppercase

upper = lambda s: s.upper()
print(upper("python"))

# Output: PYTHON

# 2. Convert to lowercase

lower = lambda s: s.lower()
print(lower("PYTHON"))

# Output: python

# 3. Reverse a string

reverse = lambda s: s[::-1]
print(reverse("python"))

# Output: nohtyp

# 4. Find string length

length = lambda s: len(s)
print(length("Python"))

# Output: 6

# 5. Check palindrome

palindrome = lambda s: "Palindrome" if s == s[::-1] else "Not Palindrome"

print(palindrome("madam"))

# Output: Palindrome

# E. Other Useful Lambda Examples

# 1. Calculate simple interest

interest = lambda p, r, t: (p * r * t) / 100
print(interest(1000, 5, 2))

# Output: 100.0

# 2. Convert Celsius to Fahrenheit

fahrenheit = lambda c: (c * 9/5) + 32
print(fahrenheit(30))

# Output: 86.0

# 3. Factorial using recursion

factorial = lambda n: 1 if n <= 1 else n * factorial(n-1)
print(factorial(5))

# Output: 120

# Note: This is an advanced example. For practical programs, a normal function is often easier to understand and maintain.