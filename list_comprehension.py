nums=[1,2,3,4,5,6,7,8,9,10]

my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list=[n*n for n in nums]
print(my_list)

even=[n for n in nums if   n%2==0]
print(even)

a=[]
for letter in 'abcd':
    for num in range(4):
        a.append((letter,num))
print(a)

a=[(letter,num) for letter in 'abcd' for num in range(4)]
print(a)

names=['bruce','clark','peter','logan','wade']
heros=['batman','superman','spiderman','wolvernine','deadpool']

my_dic={}
for name,hero in zip(names,heros):
    my_dic[name]=hero
print(my_dic)

my_dict={name:hero for name,hero in zip(names,heros) if name !='peter'}
print(my_dict)
