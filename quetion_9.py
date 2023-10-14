# Write a Python function that takes two lists and returns true if they have
# at least one common member





def common_member(list1,list2):
    for i in list2:
            if i in list1:
                return True
    return  False
l= [1,5,6,7,8,7]
l2= [1,5,6,7,4,7]
print(common_member(l,l2))               