
# Write a Python program to calculate the area of a parallelogram

def parallelogram_area(base,height):
    area = base*height
    return area
base = 5
height = 7  

area = parallelogram_area(base,height)
print(f"The area of the parallelogram is : " ,area)