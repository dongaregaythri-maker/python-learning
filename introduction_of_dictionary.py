# Introduction to Dictionary
# A dictionary in Python is a collection of data stored in key-value pairs.

# Each key is used to access its corresponding value.

student = {
    "name": "Gaythri",
    "age": 22,
    "city": "Pune"
}

print(student)

# Output:
# {'name': 'Gaythri', 'age': 22, 'city': 'Pune'}

# 2. Understanding key-value pairs


# Key         Value
# "name"       "Gaythri"

# Key           Value
# 22            "age"

# Key            Value
# "city"         "Pune"

# - Key: The name or identifier used to access data.
# - Value: The actual data associated with that key.
# Real-life example: Think of a student record. "name" is the key, and "Gaythri" is its value.

# 3. How to create a dictionary
# We use curly braces {} and separate each key-value pair with a colon :.
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}


# 4. How to access a value
# We can access a value using its key.

student = {"name": "Rahul", "age": 21}

print(student["name"])
print(student["age"])

# 6. Quick difference between List, Tuple, Set, and Dictionary

# Data structure	    Syntax        	Main feature
# List	                 [ ]	     Ordered and mutable
# Tuple	                 ( )	     Ordered and immutable
# Set	                {1, 2, 3}	      Unique elements
# Dictionary	          {"name": "Rahul"}	   Key-value pairs

# Important: An empty dictionary is {}, but an empty set is set().

