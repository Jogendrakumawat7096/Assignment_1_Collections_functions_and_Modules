# Write a Python program to get unique values from a list 

list = [1,2,4,5,3,1,3,4,5]

def unique_value(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_value(list)) 