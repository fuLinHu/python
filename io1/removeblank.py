f = open("E:\domin文件1","r",encoding="utf-8")
for i in f:
    li = list(i)
    str0 = ""
    for j in li:
        if j.isspace() != True:
            str0+=j
    print(str0)