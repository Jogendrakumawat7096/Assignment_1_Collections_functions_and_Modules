'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'''


s = 'w3resource'


counts = {}


for letter in s:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1


print(counts)