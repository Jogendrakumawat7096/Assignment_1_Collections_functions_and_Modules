# Write a Python script to check if a given key already exists in a
# dictionary.

dict1 = {'a': 1, 'b': 2,'c': 3, 'd': 4}

key = input("enter your key : ")

if key in dict1:
    print("key is already exists")
else:
    print("key not in disc")
