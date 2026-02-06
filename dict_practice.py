number=input("Number:")
dic={
    "1":"one",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"
}
output=""
for ch in number:
    output+=dic.get(ch,'!')+' '
    
print(output)