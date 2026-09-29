# Create two lists with the same elements
list_a = [1, 2, 3]
list_b = [1, 2, 3]

# Assign list_a to a new variable (creates a reference to the same object)
list_c = list_a

# --- Equality Check ---
print(list_a == list_b)  # True (Their content/values are identical)

# --- Identity Check ---
print(list_a is list_b)   # False (They are different objects in memory)
print(list_a is list_c)   # True (They point to the exact same object)
print(list_a is not list_b) # True (They occupy different memory locations)

# You can verify this by printing their actual memory addresses using id()
print(id(list_a))  # e.g., 140237482937920
print(id(list_b))  # e.g., 140237482937792 (Different ID)
print(id(list_c))  # e.g., 140237482937920 (Same ID as list_a)