# Built-in Functions of Sets in Python
# Python provides built-in functions that work with sets to find their length, maximum, minimum, total, and more.

# 1. len() — Find the number of elements
# Returns the number of elements in a set.

numbers = {10, 20, 30, 40}
print(len(numbers))

# 4

# 2. max() — Find the largest element

numbers = {10, 50, 20, 40}
print(max(numbers))

# 50

# 3. min() — Find the smallest element

numbers = {10, 50, 20, 40}
print(min(numbers))

# sum() — Calculate the sum
numbers = {10, 20, 30, 40}
print(sum(numbers))

# 100

# sorted() — Sort the elements

numbers = {40, 10, 30, 20}
print(sorted(numbers))

# [10, 20, 30, 40]

# any() — Check whether at least one element is true

numbers = {0, 0, 5}
print(any(numbers))

# True

# all() — Check whether every element is true

numbers = {1, 2, 3}
print(all(numbers))

# True

# Reason: All elements are non-zero and therefore truthy.

# If a set contains zero, all() returns False:

# Reason: All elements are non-zero and therefore truthy.

# If a set contains zero, all() returns False:

# False

# list() — Convert a set into a list

numbers = {10, 20, 30}
result = list(numbers)
print(result)

# [10, 20, 30]

# tuple() — Convert a set into a tuple
numbers = {10, 20, 30}
result = tuple(numbers)
print(result)

# (10, 20, 30)


