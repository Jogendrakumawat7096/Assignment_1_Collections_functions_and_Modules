# Write a Python script to sort (ascending and descending) a dictionary by
# value.


def sort_dict_asc(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Function to sort dictionary in descending order by value
def sort_dict_desc(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

# Test the functions
d = {'apple': 3, 'banana': 2, 'cherry': 1}

print("Original dictionary:", d)
print("Dictionary sorted in ascending order by value:", sort_dict_asc(d))
print("Dictionary sorted in descending order by value:", sort_dict_desc(d))


print(sorted(d.items()))