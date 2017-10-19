# def hello_function():
#     pass
# print(hello_function())

# def hello_func(greeting,name = 'You'):
#     return '{} ,{}'.format(greeting,name)

# print(hello_func('hi',name="shanmukha"))

courses=['Mathns','arts']
info={'name':'John','age':22}
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info(*courses,**info)
# student_info('math','art',name='john',age=22)
