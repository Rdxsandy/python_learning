# Difference between Array and List (Python)
# Array

# Homogeneous → all elements must be of the same data type

# Stores elements in continuous memory locations

# Faster for numerical operations

# Less flexible compared to lists

# Needs to be imported (array module or NumPy)

# Example:

# from array import array
# arr = array('i', [1, 2, 3, 4])

# List

# Heterogeneous → can store different data types

# Memory may not be continuous

# Slightly slower than arrays

# Very flexible and dynamic

# Built-in in Python

# Example:

# l = [1, "hello", 3.5, True]

# List Creation
# l = []                  # empty list
# l = [1, 2, 3, 4, 5]     # integer list
# l = [1, 'hello', 34, 7.0]  # mixed data types
# l = [[2, 3]]            # nested list
# l = [[[23], [[[[4, 5]]]]]]  # deeply nested list

# Accessing List Elements
# l = [1, 2, 3, 4, 5]

# print(l[0])        # 1
# print(l[1:3])      # [2, 3]
# print(l[-1])       # 5
# print(l[-3:-1])    # [3, 4]
# print(l[::-1])     # reverse the list

# Accessing Nested Lists
# l = [[1, 2], [3, 4], [4, 5], [5, 6]]
# x = l[0][0]
# print(x)           # 1

# Mutability of List

# ✔ Lists are mutable (can be changed after creation)

# l = [1, 2, 3]
# l[0] = 100
# print(l)           # [100, 2, 3]

# Adding Elements to a List
# 1. append() – add one element at the end
# l.append(6)

# 2. extend() – add multiple elements
# l.extend([7, 8, 9])

# 3. insert(index, item) – add at specific index
# l.insert(1, 50)

# Deleting Elements from a List
# 1. del
# del l[2]     # delete element at index 2
# del l        # delete entire list

# 2. remove(item) – when index is unknown
# l.remove(50)

# 3. pop() – removes and returns last element
# l.pop()

# 4. clear() – removes all elements but keeps list
# l.clear()

# Other Important List Functions
# l.sort()        # sort list
# l.reverse()    # reverse list
# l.index(3)     # index of element
# len(l)         # length of list
# sum(l)         # sum of elements (numeric)
# max(l)         # maximum value
# min(l)         # minimum value