# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

def check(g_list):
    print("given list = ",g_list)
    for i in g_list:
        if i%5==0:
            print(i,end=" ")

s=[12,78,45,12,15,5,105]
print(check(s))
