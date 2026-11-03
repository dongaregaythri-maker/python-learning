# A variable declared outside a function is called a Global Variable.

# It can be accessed:
# - Inside a function.
# - Outside a function.
# - From different functions in the same module.
# Example 1: Accessing a Global Variable


name = "Gaythri"

def student():
    print(name)

student()
print(name)

# Explanation:
# - name = "Gaythri" is declared outside the function.
# - The student() function can access it.
# - We can also access it outside the function.
# Example 2: Using a Global Variable in Multiple Functions

x = 100

def addition():
    print(x + 20)

def multiplication():
    print(x * 2)

addition()
multiplication()

# Example 3: Changing a Global Variable

x = 10

def change():
    global x
    x = 50

change()
print(x)

# Local vs Global Variables
# Local	                                        Global
# Declared inside a function       	            Declared outside a function
# Local scope	                                    Global scope
# Normally accessible only inside its function	Accessible inside and outside functions
# Exists during function execution	            Exists while the module is running