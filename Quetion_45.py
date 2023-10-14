# Write a Python program to find the highest 3 values in a dictionary 

my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}

sorted_dic = sorted(my_dict.values())
sorted_dic.reverse()
print(sorted_dic)

print("highest 3 values :",sorted_dic[:3])