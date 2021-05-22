f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\删除概念.txt","r",encoding="utf-8")
k = "in ("
for i in f:
    s = str(i).rstrip("\n")
    k+="'"+s+"',"

k+=")"

print(k)