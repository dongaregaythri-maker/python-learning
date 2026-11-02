# When we pass values using parameter names, they are called keyword arguments.
# Example

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Gaythri")

# Notice something interesting!

# In positional arguments, position matters. But in keyword arguments, we specify the parameter name, so we can change the order.

# Tricky question 🤔
# Predict the output:

def display(a, b):
    print(a)
    print(b)

display(b=50, a=100)