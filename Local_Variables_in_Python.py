# Local Variables in Python

# A Local Variable is a variable that is declared inside a function.

# It can normally be accessed only inside that function.

# Example :

def student():
    name = "Gaythri"
    age = 22

    print(name)
    print(age)

student()

# name is a local variable.

# age is a local variable.

# Both are declared inside the student() function.

# What happens if we access a local variable outside the function?

# def student():
#     name = "Gaythri"

# student()

# print(name)

# NameError: name 'name' is not defined

# Why?

# Because name is a local variable. It is available inside student(), but not outside it.

