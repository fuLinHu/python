from functools import reduce

def f(x):
    return x**2


i = map(f, [1, 2, 3, 4])
print(type(i))
print(list(i))
def f(x,y):
    return x+y;
print(reduce(f,range(101)))


from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        print(x,str="x的值为")
        print(y,str="y的值为")
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int("3"))


def char2num(s):
    return DIGITS[s]

print(list(map(char2num, "3")))


def fn(x, y):
    print("----------------")
    print(x)
    return x * 10 + y

print(reduce(fn,[5]))

def f(n):
    def fn():
        k = 0
        for i in n:
            k+=i
        return k
    return fn

f=f(range(101))
print(f())
