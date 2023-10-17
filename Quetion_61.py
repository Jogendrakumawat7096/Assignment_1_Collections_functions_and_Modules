# Write a Python program to calculate surface volume and area of a
# cylinder 

import math

def surface_valume(radias,height):
    
    v = math.pi*(radias*radias)*height
    return v


radias = 5
height = 7  

valume = surface_valume(radias,height)
print("surface volume cylinder is : " ,valume)

area = valume+2*math.pi*radias*radias
print("area of a cylinder is 1: " ,area)