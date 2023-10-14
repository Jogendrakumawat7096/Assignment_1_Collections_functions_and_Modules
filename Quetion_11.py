# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.


def unique_number(l):
    
    list=set(l)
    print(list)
    
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_number(numbers)