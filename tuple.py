#  What is a Tuple?

# Ordered

# Immutable (cannot change after creation)

# Allows duplicate values

# Can store mixed data types

# Faster than lists 

#  Tuple Creation
# t1 = ()                     # empty tuple
# t2 = (10, 20, 30)           # normal tuple
# t3 = 10, 20, 30             # tuple without parentheses
# t4 = (5,)                   # single-element tuple (comma is MUST)
# t5 = tuple([1, 2, 3])       # from list


# ❗ t = (5) → ❌ not a tuple
# ✔ t = (5,) →  tuple

#  Tuple Addition (Concatenation)
# a = (1, 2)
# b = (3, 4)

# c = a + b
# print(c)


#  Output:

# (1, 2, 3, 4)


#  Creates a new tuple (original tuples remain unchanged)

#  Tuple Repetition
# t = (1, 2)
# print(t * 3)


# Output:

# (1, 2, 1, 2, 1, 2)

#  Accessing Elements
# t = (10, 20, 30, 40)

# print(t[0])     # 10
# print(t[-1])    # 40
# print(t[1:3])   # (20, 30)

#  Tuple is Immutable
# t = (1, 2, 3)
# t[0] = 10


# ❌ Error:

# TypeError: 'tuple' object does not support item assignment

#  Tuple Unpacking
# t = (10, 20, 30)
# a, b, c = t

# print(a, b, c)

#  Common Tuple Methods
# t = (1, 2, 2, 3)

# t.count(2)   # 2
# t.index(3)   # 3


# Only 2 methods (because tuples are immutable)

#  Looping Through Tuple
# t = (1, 2, 3)

# for i in t:
#     print(i)

#  Tuple ↔ List Conversion
# t = (1, 2, 3)
# lst = list(t)        # tuple → list
# t2 = tuple(lst)      # list → tuple

#  Why Use Tuple?

# Data should not change

# Faster than list

# Used as dictionary keys

# Safer for fixed data (coordinates, records)