# class Employee:
#     pass

# emp1=Employee()
# emp2=Employee()

# print(emp1)
# print(emp2)
import os
os.getcwd()
os.chdir('D:/python/wesmckinney/')
for dirpath,dirnames,filenames in os.walk('D:/python/wesmckinney/'):
    print('CURRENT PATH:',dirpath)
    print('Directory Names:',dirnames)
    print('filenames:',filenames)


