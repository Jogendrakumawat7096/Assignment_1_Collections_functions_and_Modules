# Write a Python program to remove duplicates from a list. 

list = [1,6,5,7,1,8,5]

def remove_duplicates(list1):
  l = []
  for x in list1:
    if x not in l:
      l.append(x)
  return l


print(remove_duplicates(list))