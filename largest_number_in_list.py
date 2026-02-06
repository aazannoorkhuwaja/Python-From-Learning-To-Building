lt=[10,29,121,3,1,34,12,4,5,21,2,1,424,35,3,53,5,41]
largest=lt[0]
for i in lt[:]:
    if(i>largest):
        largest=i
print(f"The largest : {largest}")
