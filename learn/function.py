''''
    你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''

def myhelllo(a):
    print("我和【"+a+"】say")
myhelllo("付林虎")

def mutiParam(a):
    for i in a:
        print(i)

a=[2,3,"77","oo"]
mutiParam(a)

def returnfun(n):
    n = n**2
    return n
print(returnfun(7))

sum = lambda par1,par2:par1+par2
print(sum(2,3))

'''
参数
以下是调用函数时可使用的正式参数类型：
    必需参数
    关键字参数
    默认参数
    不定长参数
'''
#必需参数

def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
printme("str")
#关键字参数

def printme(x,y):
    if x=="你好":
        print("x是："+x)
    if y=="你":
        print("y是："+y)


printme(y="你",x="你好")

#默认参数
def printme(x,y="20"):
    print("x是："+x)
    print("y是：" + y)

printme("2");

#不定长参数
#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printme(arg1,*args):
    print(arg1)
    print(args)

printme(3,(4,5,6),(56,"i"))
printme(3)

#加了两个星号 ** 的参数会以字典的形式导入。
def printme(arg1,**args):
    print(arg1)
    print(args)
printme(3,c=3,b="7")

#声明函数时，参数中星号 * 可以单独出现，例如:

def f(a,b,*,c):
    return a+b+c

print(f(1,2,c=5))