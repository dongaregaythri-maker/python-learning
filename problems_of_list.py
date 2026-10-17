# Basic list method problems
# Problem 1: Add an element using append()
# Question: Add 60 at the end of the list.
# numbers = [10, 20, 30, 40]numbers.append(60)print(numbers)



# Output:
# [10, 20, 30, 40, 60]


# Reason: append() adds one element at the end of the list.
# Problem 2: Insert an element using insert()
# Question: Insert 25 at index 2.
# numbers = [10, 20, 30, 40]numbers.insert(2, 25)print(numbers)



# Output:
# [10, 20, 25, 30, 40]


# Reason: insert(index, value) adds an element at the specified index.
# Problem 3: Add multiple elements using extend()
# Question: Add [40, 50] to the existing list.
# numbers = [10, 20, 30]numbers.extend([40, 50])print(numbers)



# Output:
# [10, 20, 30, 40, 50]


# Reason: extend() adds each element from another iterable to the list.
# 2. Remove elements from a list
# Problem 4: Remove an element using remove()
# fruits = ["apple", "banana", "mango", "orange"]fruits.remove("mango")print(fruits)



# Output:
# ['apple', 'banana', 'orange']


# Reason: remove() deletes the first occurrence of the specified value.
# Problem 5: Remove an element using pop()
# numbers = [10, 20, 30, 40]numbers.pop()print(numbers)



# Output:
# [10, 20, 30]


# Reason: pop() removes the last element by default and returns the removed value.
# Problem 6: Clear the entire list
# numbers = [10, 20, 30]numbers.clear()print(numbers)



# Output:
# []


# Reason: clear() removes all elements from the list.
# 3. Other important list methods
# Problem 7: Sort a list
# numbers = [40, 10, 30, 20]numbers.sort()print(numbers)



# Output:
# [10, 20, 30, 40]


# Reason: sort() arranges the list in ascending order by default.
# Problem 8: Reverse a list
# numbers = [10, 20, 30, 40]numbers.reverse()print(numbers)



# Output:
# [40, 30, 20, 10]


# Reason: reverse() reverses the existing order of the elements.
# Problem 9: Count occurrences using count()
# numbers = [10, 20, 10, 30, 10, 40]print(numbers.count(10))



# Output:
# 3


# Reason: count() returns how many times a value appears in the list.
# Problem 10: Find an index using index()
# fruits = ["apple", "banana", "mango", "orange"]print(fruits.index("mango"))



# Output:
# 2


# Reason: index() returns the index of the first occurrence of the specified value.

# 4. Practice problems — try yourself
# Predict the output before opening each answer.
# 1. Add 100 to the end of the list.
# a = [10, 20, 30]
# a.append(100)
# print(a)

# Show answer

# 2. Insert 15 at index 1.
# a = [10, 20, 30]
# a.insert(1, 15)
# print(a)

# Show answer

# 3. Extend the list with [4, 5].
# a = [1, 2, 3]
# a.extend([4, 5])
# print(a)

# Show answer

# 4. What does pop() return here?
# a = [5, 10, 15]
# x = a.pop(1)
# print(x)
# print(a)

# Show answer

# 5. Count how many times 2 appears.
# a = [1, 2, 2, 3, 2]
# print(a.count(2))

# Show answer

# 6. Sort the list in descending order.
# a = [3, 1, 4, 2]
# a.sort(reverse=True)
# print(a)

# Show answer

# 5. Quick revision table
# Method	Purpose
# append(x)	Add one element at the end
# insert(i, x)	Add an element at a specific index
# extend(iterable)	Add multiple elements
# remove(x)	Remove the first matching value
# pop(i)	Remove and return an element
# clear()	Remove all elements
# sort()	Sort the list
# reverse()	Reverse the current order
# count(x)	Count occurrences
# index(x)	Find the first matching index
# copy()	Create a shallow copy of the list
# Important for your class: Remember the difference between append() and extend().
# a = [1, 2]a.append([3, 4])print(a)# [1, 2, [3, 4]]



# a = [1, 2]a.extend([3, 4])print(a)# [1, 2, 3, 4]



# append() adds the whole list as one element, whereas extend() adds its elements individually.