#interacting with file objects

with open('job description.txt','r') as f:

    size_to_read=10
    f_contents=f.read(size_to_read)

    # while len(f_contents)>0:
    #     print(f_contents,end='')
    #     f_contents=f.read(size_to_read)
    print(f.tell())

# import os
# print(getcwd())
# f=open('test.txt','r')
# print(f.name)
# f.close()
