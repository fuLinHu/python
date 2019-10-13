import pickle

print(str("你好 ！"))
print(repr("你好 ！"))

print("{},你是哪里来的{}".format("小红","丫头"))

# str = input("请输入：：")
# print(str)
f=open("E:\pythonwork\work1\python\entity\meone.txt","w",encoding="utf-8")
value = ("中华人民共和国",14)
value=str(value)
print(value)
f.write(value)
f.close()

f1=open("E:\pythonwork\work1\python\entity\metwo.txt","rb+")
f1.write(b'0123456789abcdef')

print(f1.seek(14))
print(f1.read(1))

