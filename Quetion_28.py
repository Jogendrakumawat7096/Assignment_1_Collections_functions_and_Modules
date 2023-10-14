# Write a Python program to remove an empty tuple(s) from a list of tuples.

tuples_list = [(10, 20, 40), (), (70, 80, 90)]
new_list = [tup for tup in tuples_list if len(tup) > 1]
print(new_list)

        