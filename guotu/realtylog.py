#
# f=open("F:\\real\\realtykngraph.log","r",encoding="utf-8")
#
# for i in f:
#     j=str(i)
#     #print(j)
#     if '上传图片开始-------' in j:
#         print(j)
#     if '上传图片耗时-------' in j:
#         print(j)


# f=open("C:\\Users\\12056\\Desktop\\文件下载蚁坊\\019b7e004145dcdcfd0c6e26e34d8035\\019b7e004145dcdcfd0c6e26e34d8035.csv","r",encoding="utf-8")
# k = 0
# for i in f:
#     if k % 300 == 0:
#         nam = "bb"+str(k)
#         fd = open("C:\\Users\\12056\\Desktop\\文件下载蚁坊\\019b7e004145dcdcfd0c6e26e34d8035\\"+nam+".csv", mode="w", encoding="utf-8")
#         print(nam)
#     fd.write(i)
#     k = k +1


f=open("C:\\Users\\12056\\Desktop\\文件下载蚁坊\\yifang.log","r",encoding="utf-8")
k = 0
for i in f:
  j = str(i)
  if "写入mq【process_in】中等待算法加工:" in j:
      k = k+1;
print(k)

