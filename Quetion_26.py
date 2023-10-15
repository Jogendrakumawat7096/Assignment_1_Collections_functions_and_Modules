# Write a Python program to replace last value of tuples in a list


def replace_last_value(tuples_list, value):
    new_list = []
    for t in tuples_list:
        new_t = t[:-1] + (value,)
        new_list.append(new_t)
    return new_list

tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(tuples_list)

value = 100
print("replacing last value with :", replace_last_value(tuples_list, value))