import functools

'''
def log(fun):
    def wrapper(*args,**kwargs):
        print("call {}():".format(fun.__name__))
        return fun(*args,**kwargs)
    return wrapper

@log
def now():
    print("2019-10-15")

now()
'''

print("-----------------------------------------")



def log(param):
    def run(fun):
        @functools.wraps(fun)
        def warpper(*args,**kwargs):
            print(param+"call {}()".format(fun.__name__))
            return fun(*args,**kwargs)
        return warpper
    return run


@log("fulinhu---")
def now():
    print("现在的时间：2019-10-15")

now()
print(now.__name__)
