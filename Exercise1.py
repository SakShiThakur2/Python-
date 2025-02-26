# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
a=int(input("enter 1st digit ="))
b=int(input("enter 2nd digit = "))
mul=a*b
sum=a+b
if mul<=1000:
  print("output = ",mul)
else:
  print("output = ",sum)
