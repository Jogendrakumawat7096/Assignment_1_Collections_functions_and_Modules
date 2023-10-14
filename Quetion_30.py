# Write a Python program to convert a list of tuples into a dictionary

tuples_list = [(10, 20), (40, 50), (70, 80)]

def convert_to_dict(input_list):
    return dict(input_list)

print(convert_to_dict(tuples_list))