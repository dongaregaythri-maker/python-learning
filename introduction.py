# what is list ?
# A list in Python is used to store multiple values in a single variable.
# Think of a shopping bag 🛍️. You can keep apples, bananas, and oranges in the same bag. Similarly, a Python list stores multiple items in one variable.

# 1. How to create a list?
# We use square brackets [] to create a list.

fruits = ["apple", "banana", "mango"]
print(fruits)

# Important features of a list
# Ordered	
# Items maintain their order	
# ["A", "B", "C"]


# Mutable	:
# We can change items	
# Change "A" to "D"

# Allows duplicates:
# Same value can appear multiple times	
# [10, 10, 20]

# Different data types:
# Can store different types together
# [10, "Hello", 3.5]

# Indexed	:
# Each item has an index	
# First item has index 0

# Accessing list elements using indexing

# Python indexing starts from 0, not 1.

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[2])

# Negative indexing is also possible:

fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])

# Changing elements in a list
# Lists are mutable, which means we can change their values.

fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"

print(fruits)



