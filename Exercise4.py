# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

# For Example:

# remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.

# Note: n must be less than the length of the string.

a=input("enter string = ")
n=int(input("enter number = "))
if n<len(a):
  print(a[n:])
else:
  print("Error !!..more than the length of the string")
