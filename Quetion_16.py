# Write a Python program to check whether a list contains a sub list 


list1 = [1,5,6,2,4,6,7,8]
list2 = [1,5,6]

print()

if set(list2).issubset(set(list1)):
    print("")
    