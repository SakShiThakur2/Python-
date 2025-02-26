# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

enter = input("enter string = ")
length_enter = len(enter)
for i in range(length_enter):
  if i%2==0:
    print(enter[i])
