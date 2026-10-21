# A set is a collection of unique elements in Python. Let's understand its important properties with simple examples.
# 1. Sets do not allow duplicate elements
# If you add the same value multiple times, Python stores it only once.

numbers = {10, 20, 30, 20, 10}
print(numbers)

# {10, 20, 30}

# Reason: A set automatically removes duplicate values.
# Real-life example: If the same student registers for an event twice, we can use a set to keep their ID only once.

# 2. Sets are unordered
# A set does not guarantee the position or order of its elements. The order in which elements are displayed may differ from the order in which you wrote them.

fruits = {"apple", "mango", "banana"}
print(fruits)

# {'banana', 'apple', 'mango'}

# Sets are mutable
# Mutable means we can add or remove elements after creating a set.

numbers = {10, 20, 30}

numbers.add(40)
print(numbers)

numbers.remove(20)
print(numbers)

# {10, 20, 30, 40}
# {10, 30, 40}

# Reason: add() inserts an element, and remove() deletes the specified element

# Sets do not support indexing
# We cannot access set elements using indexes such as [0] or [1].

# . Sets can contain different data types

# A set can contain values of different data types, such as integers, strings, and floats.

data = {10, "Python", 25.5, True}
print(data)

# {True, 10, 25.5, 'Python'}

# An empty set is created using set()

a = set()
b = {}

print(type(a))
print(type(b))

# <class 'set'>
# <class 'dict'>

