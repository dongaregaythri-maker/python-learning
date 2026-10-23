# 1. count()
# Meaning: Counts how many times a particular value appears in a tuple.

# Example:
tup1 = (10, 20, 10, 30, 10)
print(tup1.count(10))

# Output:
# 3
# Explanation: The value 10 appears 3 times in the tuple, so count(10) returns 3.


# 2. index()

# Meaning: Returns the index (position) of the first occurrence of a value in a tuple.

# Example:
tup1 = (10, 20, 30, 20, 40)
print(tup1.index(20))
# Output:
# 1
# Explanation: The value 20 first appears at index 1, because Python indexing starts from 0.
# Quick revision
# Method	Use
# count()	Counts occurrences of a value
# index()	Returns the index of the first occurrence

# Remember: Tuple has only two methods: count() and index().