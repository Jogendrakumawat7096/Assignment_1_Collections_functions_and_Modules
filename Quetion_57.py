# Write a Python program to read a random line from a file. 
import random

file = open("random.txt","w")
file.write("jogendra kumawat ")
file.close()




file =open("random.txt","r")
r = file.readlines()
random.choice(r)
print(r)
