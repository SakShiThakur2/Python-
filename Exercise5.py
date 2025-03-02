# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.


def f_l_same(n_list):
    print("given list = ",n_list)
    first=n_list[0]
    last=n_list[-1]

    if first==last:
        return True
    else:
        return False
    
a=[78,96,45,78]
print(f_l_same(a))
b=[12,45,78]
print(f_l_same(b))
    
