student={'name':'john','age':25,'courses':['MATH','ENGLISH']}
print(len(student))
student['phone']='5555-5555'
student['name']='jane'
student.update({'name':'jhansi','age':26,'phone':'555-5555'})
age=student.pop('age')
print(student.get('phone','Not found'))
print(age)
print(student.keys())
print(student.values())
print(student.items())
for key,value in student.items():
    print(key,value)




