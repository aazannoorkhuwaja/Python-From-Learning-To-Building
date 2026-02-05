string1="Iam son of Mr's Mother/..."
string2=' "My name Is KHan " '
print('1.:',string1 , '\n','2.:',string2)
print('3.:',string2[0:3],'\n','4.:',string1[:5],'\n','5.:',string1[1:-1],'\n','6.:',string1[-10:-4])


#string methods
course='Today we are learninig python and our instructor is Mosh..'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('M'))
print(course.replace('learninig','Learning'))
print(course.replace('python','Github'))
print('our' in course)