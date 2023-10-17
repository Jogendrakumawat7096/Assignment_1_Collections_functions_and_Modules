# Write a Python program to read a random line from a file. 
import random

file = open("random.txt","w")
file.write("jogendra kumawat \n kumawt \n tops Technolgy \n Ahmedabad \n python")
file.close()





file =open("random.txt","r")
lines = file.readlines()
if not lines:
    print("File is empty.") 

random_line = random.choice(lines)
print(random_line)