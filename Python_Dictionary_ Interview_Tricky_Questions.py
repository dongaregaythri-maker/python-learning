# 1. What happens when the same key is assigned twice?

d = {1: "Python", 2: "Java"}
d[1] = "C++"

print(d)

# What is the difference between d[key] and d.get(key)?

d = {"name": "Amit"}

print(d["age"])
print(d.get("age"))

# Output: The first statement raises KeyError, so the second statement is never executed.

# Explanation:
# - d["age"] raises an error because the key is missing.
# - d.get("age") would return None if executed separately.
# Interview point: get() is useful when a key may not exist.

# 3. Is a dictionary copied when we assign it to another variable?

a = {"x": 10}
b = a

b["x"] = 50

print(a)
print(b)

# Output
# {'x': 50}{'x': 50}



# Explanation: b = a does not create a new dictionary. Both variables refer to the same dictionary object. Changing it through b also affects what you see through a.

# To make a shallow copy, use b = a.copy().

# 4. What is the output of copy()?

a = {"x": 10, "y": 20}
b = a.copy()

b["x"] = 100

print(a)
print(b)

# Output
# {'x': 10, 'y': 20}{'x': 100, 'y': 20}



# Explanation: copy() creates a separate, shallow copy of the dictionary. Updating a top-level value in b does not change a.

# Tricky point: If a dictionary contains nested dictionaries or lists, a shallow copy still shares those nested objects.

# 5. Can two different keys have the same value?

d = {"a": 10, "b": 10, "c": 20}

print(len(d))
print(d.values())

# Output
# 3
# dict_values([10, 10, 20])


# Explanation: Dictionary keys must be unique, but values can repeat. There are three key-value pairs even though two values are the same.

# 6. What happens when True and 1 are used as keys?

d = {True: "Hello", 1: "Python"}
print(d)
print(len(d))



# Hide answerOutput
# {True: 'Python'}1



# Explanation: In Python, True == 1 and they have the same hash, so they refer to the same dictionary key. The later assignment updates the value to "Python".

# Remember: False and 0 behave similarly as dictionary keys.

# 7. Does in check keys or values?
d = {"name": "Amit", "age": 22}
print("Amit" in d)

print("name" in d)
print(22 in d.values())



# Hide answerOutput
# False
# True
# True


# Explanation:
# - "Amit" in d checks the keys, so it is False.
# - "name" in d checks the keys, so it is True.
# - 22 in d.values() checks the values, so it is True.
# Interview point: in checks dictionary keys by default.

# 8. What happens with a nested dictionary and a shallow copy?

a = {"student": {"marks": 80}}
b = a.copy()
b["student"]["marks"] = 95
print(a["student"]["marks"])



# Hide answerOutput
# 95


# Explanation: a.copy() copies only the outer dictionary. The nested dictionary is shared by a and b, so modifying its marks value affects both.

# To create an independent copy of nested objects, Python provides copy.deepcopy() from the copy module.


# What you should prepare for interviews
# Priority	Dictionary topic
# Very important	get() vs [], pop(), update()
# Very important	Reference vs copy, shallow copy vs deep copy
# Important	Key uniqueness and key types
# Important	in, keys(), values(), items()
# Advanced	Nested dictionaries, hashable keys, True vs 1

# My suggestion: master Questions 2, 3, 4, 6 and 8 first. They test the reasoning that makes dictionary output questions tricky.