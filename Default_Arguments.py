# A default argument is a value that is already assigned to a parameter in the function definition.

# Example:

def student(name, age=22):
    print(name)
    print(age)

student("Gaythri")
# Here, if we don't pass age, Python automatically uses 22.

# Tricky question:

def greet(name, message="Hello"):
    print(message, name)

greet("Gaythri", "Good Morning")