# weight=input('Weight: ')
# print(type(weight))
# weight=int(weight)
# print(type(weight))
# weight=int(weight/2.2)
# print('The Weight is:',weight,'Kg.')

weight=input('Weight:')
char=input("(L)bs or (K)g's :" )

if(str(char)=='l' or str(char)=='L'):
    print('The weight in Pound is:', int(weight)*2.2 ,'lbs')
elif(str(char)=='k' or str(char)=='K'):
    print('The weight in Kg is :' , int(int(weight)/2.2),'kg')
else:
    print('Not a valid option!\n Try again..')