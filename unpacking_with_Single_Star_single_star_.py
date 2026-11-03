# First, understand the meaning of Unpacking.

# Unpacking means taking values from a collection and assigning them to separate variables.

# For example, we have a list:

numbers = [10,20,30,40]
# We want to separate these values into variables.
a , b ,c ,d = numbers
print(a)
print(b)
print(c)
print(d)

# Output:
# 10
# 20
# 30
# 40
# Here, Python assigns each value to a separate variable.

# But what is the use of *?
# Suppose we have five values, but we want to store the first value separately and all remaining values together.

numbers = [10, 20, 30, 40, 50]

a, *b = numbers

print(a)
print(b)

numbers = [10,20,30,40,50]

a, *b, c = numbers

print(a)
print(b)

# Understand this table:

# Variable	                            Value
# a	                                     10
# *b	                              [20, 30, 40, 50]

# Important points:
# - a receives the first value.
# - *b collects all remaining values.
# - The starred variable always receives a list.
# - You can use single-star unpacking with lists and tuples.


#  understand Unpacking of List, Tuple and Dictionary in Python using the single star * and double star **.

# We will learn each one separately with examples.

# 1. Unpacking a List

# A list stores multiple values inside square brackets [].

numbers = [10, 20, 30, 40]
a, b, c, d = numbers
print(a)
print(b)
print(c)
print(d)



# Output:
# 10
# 20
# 30
# 40


# How does it work?

# Python assigns each list element to a variable according to its position.


# List unpacking with *

numbers = [10, 20, 30, 40, 50]
a, *b = numbers
print(a)
print(b)



# Output:
# 10
# [20, 30, 40, 50]
# Here, *b collects all remaining elements into a list.

# 2. Unpacking a Tuple

# A tuple stores multiple values inside parentheses ().

numbers = (10, 20, 30)
a, b, c = numbers
print(a)
print(b)
print(c)



# Output:
# 10
# 20
# 30


# The unpacking process is the same as a list.

# Tuple unpacking with *

numbers = (10, 20, 30, 40, 50)
a, *b = numbers
print(a)
print(b)



# Output:
# 10
# [20, 30, 40, 50]

# Important: Even though the original collection is a tuple, the starred variable b receives a list.

# 3. Unpacking a Dictionary

# A dictionary stores data in key-value pairs.

student = {  
      "name": "Gaythri",   
      "age": 22, 
      "city": "Barshi"}



# A. Unpacking dictionary using *

student = {    "name": "Gaythri",    "age": 22,    "city": "Barshi"}
a, *b = student
print(a)
print(b)



# Output:
# name
# ['age', 'city']


# Why?

# When we unpack a dictionary using a single *, Python takes its keys by default, not its values.
# B. Unpacking dictionary using **
# Double star ** unpacks dictionary key-value pairs.

student = {    "name": "Gaythri",    "age": 22}
def display(name, age): 
       print(name)   
       print(age)
       display(**student)



# Output:
# Gaythri
# 22


# This is equivalent to:
# display(name="Gaythri", age=22)




# Final comparison

# Collection	                  Single *                  	Double **
# List	                     Unpacks elements	   Not used directly for list unpacking
# Tuple	                       Unpacks elements  	Not used directly for tuple unpacking
# Dictionary	                   Unpacks keys	           Unpacks key-value pairs

# Remember these three things:
# 1. List → []
# 2. Tuple → ()
# 3. Dictionary → {key: value}
# And:
# - * → Collects remaining elements into a list during unpacking.
# - ** → Unpacks dictionary key-value pairs, commonly into keyword arguments or another dictionary.

# Let's practise – Question 1
# numbers = [10, 20, 30, 40]
# a, *b = numbers
# print(b)



# What will be the output?

# A) [10, 20, 30]


# B) [20, 30, 40]


# C) (20, 30, 40)


# Check answer

# We'll practise list, tuple and dictionary unpacking until you're confident.