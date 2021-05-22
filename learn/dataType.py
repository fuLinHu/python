#!/usr/bin/python3
'''

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。


与Python字符串不一样的是，列表中的元素是可以改变的：

1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。


可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
str = "flh"
print(str[0])

list = [1,2,"3","5",0.4,True]

print(list[0])
print(type(list[0:2]))
print(type(list[-1]))
print(list*2)
print(list+list)
#list[0:3] = []
print(list[1:5:2])
print(list[1:])

print(list[0::-1])

tuple = (1.2,'3',True,0.4)

tuple = ()
tuple = (1,)
print(tuple[0:])

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)
print(student)

a=set("'a'bcdf")
b=set("abcdf66")

print(a)

a= {"name":"flh","age":30,"sex":True}
print(a["name"])
print(a["age"])

a=dict([("name","fulinhu"),("age",30)])
a= dict(name="fulinhu",age=30)
a={x: x**2 for x in (2, 4, 6)}

print(a)

"""
"""

a='uejklll'
b='uejklll'
print(id(a) == id(b))
b=dict([(1,2),(3,4),(5,6)])
print(b)



