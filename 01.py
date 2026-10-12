# Nested For Loop in Python

# Example 1: Simple Nested For Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Example 2: Print a Star Pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Example 3: Print a Number Pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Example 4: Print a Square Pattern
for i in range(1, 4):
    for j in range(1, 5):
        print("*", end=" ")
    print()

# Example 5: Multiplication Table
for i in range(1, 4):
    for j in range(1, 6):
        print(i, "x", j, "=", i * j)
    print()

#     Remember this concept
# A nested for loop means a for loop inside another for loop.
# - Outer loop (i) controls the rows.
# - Inner loop (j) controls the work done in each row.
# - print() moves to the next line.
# - end=" " prints on the same line.
# For example, the star pattern has 4 rows, and each row prints as many stars as its row number.