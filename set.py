# 🔹 What is a Set in Python?

# A set is a built-in data type used to store a collection of unique elements.

# Unordered

# Mutable (can be changed)

# No duplicate values

# my_set = {1, 2, 3, 3}
# print(my_set)   # {1, 2, 3}

# 🔹 Key Characteristics

# ❌ No indexing or slicing

# ✅ Automatically removes duplicates

# ✅ Fast membership testing (in)

# ❌ Cannot contain mutable items (like lists or dictionaries)

# Valid:

# {1, "a", 3.5}


# Invalid:

# {1, [2, 3]}   # Error

# 🔹 Creating Sets
# s1 = {1, 2, 3}
# s2 = set([4, 5, 6])
# empty_set = set()     # {} creates a dictionary

# 🔹 Common Set Operations
# A = {1, 2, 3}
# B = {3, 4, 5}

# Operation	Syntax	Result
# Union	`A	B`
# Intersection	A & B	{3}
# Difference	A - B	{1,2}
# Symmetric Difference	A ^ B	{1,2,4,5}
# 🔹 Important Set Methods
# A.add(10)            # add element
# A.remove(2)          # remove (error if not found)
# A.discard(5)         # remove (no error)
# A.pop()              # removes random element
# A.clear()            # empty the set

# 🔹 Membership Testing
# if 3 in A:
#     print("Present")


# 👉 Faster than lists (uses hashing)

# 🔹 Frozen Set

# An immutable version of set:

# fs = frozenset([1, 2, 3])


# Cannot add or remove elements

# Can be used as dictionary keys