
# Number Pattern Programs in Python

# 1. Increasing Number Pattern
# Output:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 2. Repeated Number Pattern
# Output:
# 1
# 22
# 333
# 4444
# 55555

for i in range(1, 6):
    print(str(i) * i)


# 3. Inverted Number Pattern
# Output:
# 12345
# 1234
# 123
# 12
# 1

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 4. Same Number in Each Row
# Output:
# 1
# 22
# 333
# 4444
# 55555

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


# 5. Reverse Number Pattern
# Output:
# 54321
# 4321
# 321
# 21
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
