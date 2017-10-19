# from mymodule import find_index,test
# import sys
import random as r
#stand library modules
import math
import datetime
import calendar
import os

print(os.__file__)
print(os.getcwd())
today=datetime.date.today()
print(today)
# #if you want to add module in another lcoation just add tha locaiton to sys.path
# # sys.path.append('/users/shanmukha/desktop/mymodule')
courses=['History','Math','Physics','Compsci']

# # index=find_index(courses,'Math')
# # print(index)
# # print(test)

# print(sys.path)
randome_course=r.choice(courses)
print(randome_course)
