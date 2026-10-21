# What is a Set?
# A set in Python is a collection of unique elements. It does not allow duplicate values, and it is unordered, meaning elements do not have fixed positions or indexes.

# Example:
numbers = {10, 20, 30, 20, 10}
print(numbers)

# {10, 20, 30}

# A set automatically removes duplicate values, so 10 and 20 appear only once.

# Sets are useful when you need to remove duplicates or find common and different elements between collections.
# 3. Important characteristics of sets
# - Unique: Duplicate elements are removed automatically.
# - Unordered: Elements have no guaranteed order.
# - Mutable: You can add or remove elements.
# - No indexing: You cannot access elements using set[0].
# - Mixed data types: A set can contain integers, strings, and other allowed immutable values.
# - Empty set: Use set(), not {}, because {} creates an empty dictionary.

# How to create a set

# Creating a set
fruits = {"apple", "banana", "mango"}
print(fruits)

# Creating an empty set
empty_set = set()
print(empty_set)

# Output (the order of fruit names may vary):
# {'apple', 'banana', 'mango'}
# set()

# Difference between a list, tuple, and set
# Feature	       List	     Tuple	    Set
# Brackets	        []	      ()	    {}
# Ordered	        Yes	      Yes	    No
# Duplicates	  Allowed	Allowed	  Not allowed
# Changeable	    Yes	      No	    Yes
# Indexing	         Yes	  Yes	     No

