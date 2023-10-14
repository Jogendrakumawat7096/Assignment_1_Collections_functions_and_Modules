# Write a Python program to check multiple keys exists in a dictionary

dict = {'a': 1, 'b': 2,'c': 3, 'd': 4}


key_check = ['a','b']


if all(key in dict for key in key_check):
    print("All keys are present in the dictionary.")
else:
    print("Not all keys are present in the dictionary.")