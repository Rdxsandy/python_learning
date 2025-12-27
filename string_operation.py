

# we can  contcatenated string with the help of + operator and multiply with *

# s = 'hello'
# s1 = '*'
# print(s+s1)=hello*
# print(s1*10)=**********

# print('Mubai'>'Pune')==False
# print('Hello'=='Hello')==True
# all comparision operator works here ==,!=,<=,>=<,>
# comparision happens lexographically
# for the empty strings python treated as false and the strings which is not empty python treated as true

# common function in string len() min() max() sorted()
# len() gives the length of string
# min() gives the min value of string based on ascii value
# max() gives the max value of string based on ascii value
# sorted() sort the  function based on ascii value
#  sorted(string,reverse=True) sort in acending order based on ascii value

## functions which is only valid on strings

#  capitalize()

# s ='it is raining today'
# p= s.capitalize()
# print(p)=It is raining today
# print(s)=it is raining today
# clearly we can see that capitalize does the change the original string

# title()

# s ='it is raining today'
# p=s.title()
# print(p)=It Is Raining Today
# print(s)=it is raining today

# upper()

# s ='it is raining today'
# p = s.upper()
# print(s)=it is raining today
# print(p)=IT IS RAINING TODAY

# lower

# s ='It Is Raining Today'
# p = s.lower()
# print(s)=It Is Raining Today
# print(p)= it is raining today

# s='It Is Nothing'
# p = s.swapcase()
# print(s)=It Is Nothing
# print(p)=iT iS nOTHING

# count(str)=> it basically tells us how many times a substring is present in the string

# s= ' it is is now is'
# print(s.count('is'))=3

# find(str) gives us the index of starting character of the substring

# s = ' it is raining'
# print(s.find('raining'))=7

# endswith(str) and startswith(str) return true and false 

# string formate

# name = "Sundeep"
# age = 21

# print(f"My name is {name} and I am {age} years old")
# output=My name is Sundeep and I am 21 years old

# s ='sandeep'
# s.isalnum()== check for alphanumeric
# s.isalpha()== is alphabetic
# s.isdecimal()
# s.isidentifier()

# split convert the string into list based on some parameter by default space

# s.split(',')

# join function is just opposite of split function
# "/"join(list)  joining based on /

# Replace()
# strip function remove the trailing ans leading spaces
print()