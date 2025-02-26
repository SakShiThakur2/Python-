# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
previous=0
for i in range (10):
    
    print("current  = ",i,"previous = ",previous,"sum =",i+(previous))
    previous=i
