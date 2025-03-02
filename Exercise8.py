# Exercise 8: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

def number(n):
  for i in range(n):
      for j in range(n-i):
          print("*",end=" ")
      print(" ")

number(6)
