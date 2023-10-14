# Write a Python script to concatenate following dictionaries to create a
# new one.


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

# Concatenate dictionaries
new_dict = {**dict1, **dict2, **dict3}
print('New dictionary:', new_dict)
