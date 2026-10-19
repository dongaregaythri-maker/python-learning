# Python Tuples
# Tuples are a natural next topic after lists. You'll learn how they differ from lists, how to access elements, and which operations and methods they support.
# What you'll learn

# Theory + complete Python script + examples + practice questions + GitHub commands



# 1. What is a tuple?
# A tuple is a collection of elements stored in a single variable. Tuples are ordered and immutable, which means you cannot change their elements after creating them.

# Real-life example: Think of a date of birth. Once recorded, it normally stays the same. A tuple can represent fixed information like this.
# student = ("Gaythri", 22, "MCA")print(student)print(student[0])print(student[1])



# Output:
# ('Gaythri', 22, 'MCA')
# Gaythri
# 22


# 2. List vs tuple
# Feature	List	Tuple
# Brackets	[]	()
# Ordered	Yes	Yes
# Change elements	Yes	No
# Add/remove elements	Yes	No
# Example	[10, 20, 30]	(10, 20, 30)


# ==========================================
# Topic: Python Tuples
# Description: Learning tuple operations
# ==========================================

# 1. Creating a tuple
print("1. Creating a Tuple")

numbers = (10, 20, 30, 40, 50)
print(numbers)

# 2. Accessing tuple elements
print("\n2. Accessing Elements")

print(numbers[0])
print(numbers[2])
print(numbers[-1])

# 3. Slicing a tuple
print("\n3. Tuple Slicing")

print(numbers[1:4])
print(numbers[:3])
print(numbers[::-1])

# 4. Tuple with different data types
print("\n4. Different Data Types")

student = ("Gaythri", 22, "MCA", 85.5)
print(student)

# 5. Single element tuple
print("\n5. Single Element Tuple")

single = (10,)
print(single)
print(type(single))

# Note: The comma is necessary for a single-element tuple.

# 6. Tuple is immutable
print("\n6. Tuple Immutability")

colors = ("red", "green", "blue")
print("Original tuple:", colors)

# Tuple elements cannot be changed directly.
# colors[0] = "yellow"  # This causes TypeError.

# 7. Tuple concatenation
print("\n7. Tuple Concatenation")

a = (1, 2, 3)
b = (4, 5, 6)

result = a + b
print(result)

# 8. Repeating a tuple
print("\n8. Tuple Repetition")

values = (1, 2)
print(values * 3)

# 9. Using count()
print("\n9. Count Method")

items = (10, 20, 10, 30, 10)
print(items.count(10))

# 10. Using index()
print("\n10. Index Method")

fruits = ("apple", "banana", "mango", "orange")
print(fruits.index("mango"))

# 11. Finding the length
print("\n11. Length of Tuple")

print(len(fruits))

# 12. Checking membership
print("\n12. Membership Operators")

print("apple" in fruits)
print("grapes" in fruits)

# 13. Looping through a tuple
print("\n13. Loop Through Tuple")

for number in numbers:
    print(number)

# 14. Tuple packing and unpacking
print("\n14. Packing and Unpacking")

person = ("Rahul", 21, "Python")

name, age, skill = person

print("Name:", name)
print("Age:", age)
print("Skill:", skill)

# 15. Converting list to tuple and tuple to list
print("\n15. Type Conversion")

my_list = [10, 20, 30]
my_tuple = tuple(my_list)

print(my_tuple)

new_list = list(my_tuple)
new_list.append(40)

print(new_list)

# ==========================================
# Practice Questions
# ==========================================

# Q1. Create a tuple containing five numbers.
# Q2. Print the first and last elements.
# Q3. Print the tuple in reverse order.
# Q4. Count how many times 5 occurs in a tuple.
# Q5. Find the index of "Python".
# Q6. Check whether 50 exists in a tuple.
# Q7. Unpack a tuple containing your name, age,
#     and course into three variables.
# Q8. Convert a list into a tuple.
# Q9. Explain why tuple elements cannot be changed.
# Q10. Find the length of a tuple.

print("\nAll tuple examples completed!")
