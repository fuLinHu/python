#set={2,4,5}
#print(type(set))
set1=set("78yttru")
print(set1)

a={x for x in ("a","e","3") if x != "3"}
print(a)

b=set()
b.add(1)
b.add(2)
b.add("4")
b.add("5")
print(b.discard(2))
print(b)

a,b=0,1
while b<1000:
    a,b=b,a+b
    print(a,end=",")

