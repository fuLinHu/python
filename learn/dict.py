"""
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例


2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
"""

dic = {"name":"fulinhu",'age':30}
dic["fu"]="fulinhu"
print(dic)
#dic.clear()
print(dic)
del dic["fu"]
print(dic)
del dic
#print(dic)
dict2 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("dict2['Name']: ", dict2['Name'])

#2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
dict2 = {('Name',"age"): 'Runoob', 'Age': 7}

dict1 = {('Name',"age"): 'Runoob', 'Age': 7}

print(type(dict2.values()))
print("----------------")
list(dict2.values())[0]
print(dict2.values())
print(list(dict2.values()))
print(list(dict2.values())[0])
#print(dict1[])
print("----------------")
print("dict2['Name']: ", dict2[('Name',"age")])
print("--------key--------")
keys = dict2.keys()
l = list(keys)

print(dict1[l[0]])
tup=(3,"4",6,True)
print(dict1.fromkeys(tup))
print(type(None))
print(dict1.get("kkkk") == None)
print(1==1)
print(1 is 2)
print(list(dict1.items())[0][0][0])

d=dict(a=2,c=4,d=5)
print(d)
c=dict([("a",2),("c",4),("d",5)])
print(c)
d = {x:x**2 for x in (2,3,4)}
print(d)
items = c.items()

for i,j in items:
    print(i,end=":")
    print(j,end=",")

print("------------------------------------------")
li= ["t","e","y","k"]
d=enumerate(li)
for i,j in d:
    print(i, end=":")
    print(j, end=",")


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# for i in reversed(questions):
#     print(i)

for i in sorted(questions):
    print(i)




k=zip(answers,questions)
print(list(k))


