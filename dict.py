# Python Dictionary — Quick Summary

# A dictionary in Python is a mutable, unordered collection of data stored as key–value pairs.

# 🔹 Syntax
# my_dict = {"name": "Sundeep", "age": 21, "branch": "CSE"}

# 🔹 Key Features

# Keys are unique (no duplicates)

# Values can repeat

# Keys must be immutable (string, number, tuple)

# Values can be any data type

# Written using curly braces {}

# 🔹 Accessing Values
# my_dict["name"]      # 'Sundeep'
# my_dict.get("age")   # 21

# 🔹 Adding / Updating
# my_dict["college"] = "ABC University"   # add
# my_dict["age"] = 22                     # update

# 🔹 Removing Elements
# del my_dict["age"]
# my_dict.pop("branch")

# 🔹 Common Dictionary Methods

# keys() → returns all keys

# values() → returns all values

# items() → returns key-value pairs

# update() → merges dictionaries

# clear() → removes all items

# 🔹 Looping Through Dictionary
# for key, value in my_dict.items():
#     print(key, value)

# 🔹 Example
# student = {
#     "roll": 101,
#     "name": "Amit",
#     "marks": 85
# }

# 🔹 Use Cases

# Storing structured data

# Fast lookup operations

# Representing JSON / API data