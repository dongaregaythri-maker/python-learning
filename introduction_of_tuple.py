# # 1. What is a Tuple?
# # A tuple is a built-in data structure in Python used to store multiple elements in a single variable. A tuple is ordered and immutable, which means its elements cannot be changed after creation.
# # Example:

# student = ("Gaythri", 22, "MCA")print(student)

# # Output:
# # ('Gaythri', 22, 'MCA')

# # Explanation: Here, the tuple student stores three values: a name, an age, and a course.

# # 2. Syntax of a Tuple

# # Tuples are generally created using round brackets () with elements separated by commas.

# # variable_name = (element1, element2, element3)
# # Example:

# numbers = (10, 20, 30, 40)print(numbers)

# # Output:
# # (10, 20, 30, 40)


# # 3. Real-life example
# # Imagine storing a student's fixed details:

# student = ("Rahul", 21, "MCA")
#  "Rahul" — student name
#  21 — student age
#  "MCA" — course name
# # A tuple is useful when you want to keep related information together and do not need to change the collection itself.
# # 4. Important points about tuples
# # - Ordered: Elements maintain their order.
# # - Immutable: Elements cannot be directly changed, added, or removed.
# # - Duplicates allowed: The same value can appear more than once.
# # - Different data types: Can store strings, integers, floats, and other allowed values.
# # - Indexing and slicing: Elements can be accessed using indexes.
# # - Single-element tuple: A comma is required, as in (10,).
# # 5. Example of immutability
# # numbers = (10, 20, 30)numbers[0] = 100
# # Output: TypeError

# # Reason: Tuples do not support changing an element through assignment.
# # Definition to write in an exam
# # A tuple is a built-in data structure in Python used to store multiple elements in an ordered collection. It is immutable, allows duplicate elements, and is created using round brackets ().