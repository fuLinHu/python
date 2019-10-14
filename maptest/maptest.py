def f(x):
    return x**2


i = map(f, [1, 2, 3, 4])
print(type(i))
print(list(i))
