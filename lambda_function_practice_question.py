
# Python Lambda Function Practice
# Date: 05-11-2026

# 1. Square of a number
square = lambda x: x ** 2
print("Square:", square(12))

# 2. Cube of a number
cube = lambda x: x ** 3
print("Cube:", cube(4))

# 3. Even or Odd
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Number:", check_even_odd(15))

# 4. Positive, Negative or Zero
check_number = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print("Number:", check_number(-15))

# 5. Eligibility check
eligibility = lambda age: "Eligible" if age >= 18 else "Not Eligible"
print("Eligibility:", eligibility(20))

# 6. Find greater number
greater = lambda a, b: a if a > b else b
print("Greater number:", greater(20, 30))

# 7. Reverse a string
reverse = lambda text: text[::-1]
print("Reverse:", reverse("Python"))

# 8. Map using lambda - square every number
numbers = [2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print("Squares using map:", result)

# 9. Map using normal function
def multiply_by_five(x):
    return x * 5

numbers = [2, 4, 6, 8]
result = list(map(multiply_by_five, numbers))
print("Multiplication using map:", result)
