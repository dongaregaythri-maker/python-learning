# 1. Ordered
# Meaning: A dictionary maintains the insertion order of its key-value pairs in Python 3.7 and later.

student = {
    "name": "Rahul",
    "age": 21,
    "city": "Pune"
}

print(student)

# 2. Mutable
# Meaning: We can add, update, and delete dictionary entries after creating the dictionary.

student = {"name": "Rahul", "age": 21}

student["age"] = 22
student["city"] = "Pune"

print(student)

# 3. Keys Must Be Unique
# Meaning: A dictionary cannot keep separate entries with the same key. 
# If the same key is assigned more than once, the later value replaces the earlier value.

student = {
    "name": "Rahul",
    "age": 20,
    "age": 22
}

print(student)

# 4. Values Can Be Duplicated
# Meaning: Different keys can have the same value.

student = {
    "name": "Rahul",
    "city": "Pune",
    "college_city": "Pune"
}

print(student)

# 5. Stores Data in Key-Value Pairs
# Meaning: Every dictionary entry contains a key and its associated value, separated by a colon :.

student = {"name": "Rahul", "age": 21}

print(student["name"])

# 6. Keys Must Be Hashable
# Meaning: Dictionary keys must be hashable. Common examples are strings, integers, and tuples containing only hashable elements. Lists and sets cannot be used as dictionary keys.

data = {
    "name": "Rahul",
    101: "Student",
    (1, 2): "Coordinates"
}

print(data[101])

# Invalid example:
data = {[1, 2]: "Hello"}

# 7. Values Can Have Different Data Types
# Meaning: Dictionary values can be strings, integers, floats, Booleans, lists, or even other dictionaries.

student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85.5,
    "passed": True,
    "subjects": ["Python", "Java"]
}

print(student)

