numbers=[1,2,3,1,5,63,21,2,45,2]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)        