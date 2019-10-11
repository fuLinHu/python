
def myFun(n):
    a,b,couter=0,1,0
    while couter<n:
        a,b=b,a+b
        couter+=1
        yield a


fun = myFun(10)
flag = True
while flag:
    try:
        print(next(fun))
    except StopIteration:
        flag = False

