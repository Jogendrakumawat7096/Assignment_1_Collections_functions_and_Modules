# Write a Python program to combine two dictionary adding values for
# common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 

d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400}


d3= {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1) | set(d2)}

print(d3)