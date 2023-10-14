lst = ["Jogendra","kumawat","Tops","Technolgy","window","stories","eye"]

count = 0
for i in lst:
    if len(i)>2 and i[0]==i[-1]:
        count = count+1

print(count)