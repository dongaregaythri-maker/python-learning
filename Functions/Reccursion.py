'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2*1
factorial(3) = 3*2*1
factorial(4) = 4*3*2*1
factorial(5) = 5*4*3*2*1
factorial(6) = 6*5*4*3*2*1
factorial(7) = 7*6*5*4*3*2*1
fraction(n) = n*fraction(n-1)
'''

from math import factorial


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter the number: "))
print(f"The factorial of this number is : {factorial(n)}")

