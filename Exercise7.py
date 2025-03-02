# Exercise 7: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

def number(n):
  for i in range(n):
      for j in range(i):
          print(i,end=" ")
      print(" ")

number(6)
