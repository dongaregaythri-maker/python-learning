# Find the length of a tuple
# Question: Write a program to count the number of elements in a tuple.

tup = (10, 20, 30, 40, 50)
print(len(tup))

# Output:
# 5

# Explanation: len() returns the total number of elements.


# 2. Find the largest and smallest elements

tup = (15, 8, 25, 3, 12)
print("Maximum:", max(tup))print("Minimum:", min(tup))


# Output:
# Maximum: 25
# Minimum: 3

# Explanation: max() finds the largest value, and min() finds the smallest.

# 3. Count how many times a value appears

tup = (10, 20, 10, 30, 10, 40)
print(tup.count(10))

# Output:
# 3
# Explanation: The value 10 appears three times.

# 4. Find the index of an element

tup = (5, 10, 15, 20, 10)
print(tup.index(10))

# Output:
# 1
# Explanation: index() returns the position of the first occurrence of 10.

# 5. Print only integer values from a mixed tuple
# Question: Print integers while excluding Boolean values.

tup = (11, "pune", 22, "hello", True, 99.99, 33, 55)for value in tup:  
  if type(value) == int:        
    print(value)

# Output:
# 11
# 22
# 33
# 55
# Explanation: type(value) == int selects values whose exact type is integer, excluding True and False.

# 6. Convert a tuple into a list

tup = (10, 20, 30)result = list(tup)print(result)

# Output:
# [10, 20, 30]
# Explanation: list() converts the tuple into a list.

# 7. Reverse a tuple
tup = (10, 20, 30, 40)
print(tup[::-1])

# Output:
# (40, 30, 20, 10)
# Explanation: The slice step -1 reads the tuple in reverse order.

# 8. Find the sum of all elements
tup = (10, 20, 30, 40)
print(sum(tup))
# Output:
# 100
# Explanation: sum() adds all numeric elements.

# 9. Find common elements between two tuples
tup1 = (10, 20, 30, 40)tup2 = (30, 40, 50, 60)for value in tup1:   
 if value in tup2:       
    print(value)
# Output:
# 30
# 40
# Explanation: The in operator checks whether each element of tup1 also exists in tup2.

# 10. Remove duplicates from a tuple
tup = (10, 20, 10, 30, 20, 40)
result = tuple(set(tup))
print(result)
# Possible output:
# (40, 10, 20, 30)
# Explanation: set() removes duplicate values. The order is not guaranteed, so the output order may differ.

# 11. Find the second-largest distinct value
tup = (10, 50, 30, 50, 20)values = sorted(set(tup))print(values[-2])
# Output:
# 30
# Explanation: set() removes duplicates, sorted() sorts the values, and [-2] selects the second-largest value.

# 12. Swap two variables using tuple unpacking
a = 10
b = 20a, b = b, aprint(a, b)
# Output:
# 20 10
# Explanation: Tuple unpacking assigns the old value of b to a and the old value of a to b.

# 1. Print the even numbers from a tuple.

# Example: (10, 15, 20, 25, 30)
# Show hint

# 2. Find the second element from the end of a tuple.

# Example: (5, 10, 15, 20)
# Show hint

# 3. Check whether a tuple is empty.

# Example: ()
# Show hint

# 4. Create a new tuple containing only strings.

# Example: (10, "apple", 20, "mango")
# Show hint

# 5. Merge two tuples into one tuple.

# Example: (1, 2) and (3, 4)
# Show hint

# 6. Find all elements that occur more than once.

# Example: (1, 2, 3, 2, 4, 1)
# Show hint

# My recommendation: Start with questions 1–8, then practise the six unsolved problems. These will help you build confidence with tuples before moving to more advanced coding problems.