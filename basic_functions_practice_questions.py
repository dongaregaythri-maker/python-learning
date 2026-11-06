# Write a function to add two numbers.
def add(a, b):
    return a + b

print(add(10, 20))



# Write a function to find the square of a number.
def square(x):
    return x ** 2

print(square(5))



# Write a function to check whether a number is even or odd.
def even_odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(7))



# Write a function to find the largest of three numbers.
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(largest(10, 25, 15))



# Write a function to calculate the factorial of a number.
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(5))