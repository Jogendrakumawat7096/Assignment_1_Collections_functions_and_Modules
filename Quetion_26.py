# Write a Python program to replace last value of tuples in a list

# List of tuples
tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100

for t in tuples_list:
    new_list = [t[:-1]+]