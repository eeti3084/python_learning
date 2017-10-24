import os
print(os.getcwd())

os.chdir('D:\python\plantes')
print(os.getcwd())


for f in os.listdir():

    file_name,file_ext=os.path.splitext(f)
    f_name,f_ext=file_name.split('.')
    f_title,f_course,f_num=f_name.split('-')
    f_title=f_title.strip()
    f_name=f_name.strip()
    f_num=f_num.strip()[1:].zfill(2)
    f_course=f_course.strip()
    new_name='{}-{}.{}'.format(f_num,f_title,f_ext)

    os.rename(f,new_name)
