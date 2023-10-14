# Write a Python program to calculate the area of a trapezoid 

def trapezoide_area(base1,base2,height):
    area = ((base1 + base2)/2) * height
    return area
base1 = 5 
base2 = 10 
height = 7  

area = trapezoide_area(base1, base2, height)
print(f"The area of the trapezoid is : " ,area)