#  Write a Python program to unzip a list of tuples into individual lists.

tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for tup in tuples_list:
    print(list(tup))