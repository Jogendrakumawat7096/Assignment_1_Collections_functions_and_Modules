# Write a Python program to find the repeated items of a tuple. 

t = (1,8,4,5,9,1,6,5,6)

def find_repeated_items(t):
    return {i for i in t if t.count(i) > 1}
        
print("repeated item in tuple :",find_repeated_items(t))