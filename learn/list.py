for x in [1, 2, 3]:
    print(x, end=" ")

list = [[1,23,4],['5','6','7'],[10.0,20.0,True]]
print()
print(list[0][1])
print(len(list))
print(max(list[0]))

newList = list.copy()

print(newList)
print(newList is list)