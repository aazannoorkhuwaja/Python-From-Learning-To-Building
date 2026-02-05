name=input('Enter Your Name:')
if(len(name) < 3):
    print('Name Must Be Greater then 3 char!')
elif(len(name)>50):
    print('Name can be max 50 cha!')
else:
    print('Name Looks Good!')
