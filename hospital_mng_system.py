#here first we will ask name then age and then confirm new of old
print('Enter Your Name:')
name=input()
print('Enter Your Age:')
age=input()
print('Confirm New/Old Patient..?')
patient=input()

if(patient == 'New' or patient == 'new'):
    print('The Patient Is New!!')
else:
    print('patient is old!!')

