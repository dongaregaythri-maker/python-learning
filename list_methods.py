# Important list methods
# These are useful when solving Python problems and interview questions.

# append()	
# Adds one item at the end	
# a.append(40)

# insert()	
# Adds an item at a specific index
# a.insert(1, 20)

# extend()	
# Adds multiple items from another iterable	
# a.extend([40, 50])

# remove()
# Removes a specified value
# a.remove(20)

# pop()
# Removes and returns an item	a.pop()

# sort()
# Sorts the list
# a.sort()

# reverse()
# Reverses the list in place
# a.reverse()

# clear()	
# Removes all items	
# a.clear()

# 1. list.append() :

# The append() method adds one element at the end of a list.
# Example 1: Adding one element

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print(fruits)

# Simple explanation:
# - Initially, the list contains 3 fruits.
# - fruits.append("Orange") adds "Orange" at the end.
# - Now the list contains 4 fruits.
# Think of a queue of students: a new student joins at the end of the queue.

# Adding a number to a list :

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# important interview and exam point
# What happens if we append a list?

a = [10, 20, 30]

a.append([40, 50])

print(a)

# What is insert() in Python?

# The insert() method adds an element at a specific position (index) in a list.
# Remember the difference:
# - append() → Adds an element at the end.
# - insert() → Adds an element at the position you specify.

# Syntax:
list.insert(index, element)

# Example 1: Insert an element

fruits = ["Apple", "Mango", "Orange"]

fruits.insert(1, "Banana")

print(fruits)

# What is extend() in Python?
# The extend() method adds multiple elements from another iterable (such as a list) to the end of an existing list.
# Example 1: Extending a list

a = [10, 20, 30]
b = [40, 50, 60]

a.extend(b)

print(a)