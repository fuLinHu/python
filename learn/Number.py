"""
整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
"""
import random
import math

s = 1.5
b = int(s)
print(b)
b =float(s)
print(b)

print(complex(s))
print(complex(1,2))
print(2/3)
print(5//3)
#b=compile(1,4)
#compile(1,4)
#print(compile(1,4))
x= 2
y=3
print((x>y)-(x<y))

a=random.uniform(x, y)
print(a)


print(math.pi)
print(math.pi)