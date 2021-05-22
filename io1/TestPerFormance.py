
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\manage-faqs-200并发(20200605).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\manage-faqs-单个(20200605).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200608\manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200609\manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/202006091\manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200610\/1/manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200610\/3（100）/manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200611\/1(300)/manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200611\/2(200）/manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200611\/3(500)/manage-faqs (2分钟压测).log","r",encoding="utf-8")

#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200611\/4(500)/manage-faqs (2分钟压测).log","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200612\/1/nohup(3).out","r",encoding="utf-8")
#E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\20200518\压测记录\20200611\4(500)
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200612\/2/nohup200-10.out","r",encoding="utf-8") 6d1a58ed-6213-4d08-9316-b898d9ea90ba
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200612\/3(2007年AD7缝洞单元的沉没度是多少)/200-4.out","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200612\/4/200-9.5.out","r",encoding="utf-8") #22e688b9-8ead-4d48-9f29-c317046ffe8a

#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200612\/5/nohup(6).out","r",encoding="utf-8") #e131e0b6-e4cb-408d-86f6-64180e01438f

#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200612\/5/nohup(6).out","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200617/nohup(faq).out","r",encoding="utf-8") #e131e0b6-e4cb-408d-86f6-64180e01438f
#E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\20200518\压测记录\20200617  nohup(faq).out  nohup (2)(1).out
#E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\20200518\压测记录\20200612\5
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200618/manage-faqs.log","r",encoding="utf-8")

#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200620\/1\/faq.log","r",encoding="utf-8")

#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200620\/2/nohup.out","r",encoding="utf-8")

#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200620\/3/242nohup.out","r",encoding="utf-8")
#f = open("E:\项目文件(北明智通)\智能油田\油田文件\开发管理文件\/20200518\压测记录\/20200620\/4/nohup241.out","r",encoding="utf-8")
f = open("F:\/faq日志.txt","r",encoding="utf-8")

handleNewFAQMap = {}
countTimes = {}
totalSecond = {}
maxSecond = {}
threadListcont=[]

threadMapcontMap={}

def groupByThread(threadName,j):
    index=j.find('Thread-name：【')
    if(index!=-1):
        k=j[index+13:index+49]
        if(threadName==k):
            threadListcont.append(j)
        if(k in threadMapcontMap):
            k_ = threadMapcontMap[k]
            k_.append(j)
        else:
            k_=[j]
            threadMapcontMap[k]=k_

def  parseLog(method, j, countTimes, totalSecond):
    if(method in j):
        if(method in handleNewFAQMap):
            if(method in countTimes):
                countTimes[method]=countTimes[method]+1;
            else:
                countTimes[method]=1
            index=j.find('】ms 【')
            endindex=j.rfind('：【')
            endindex_ = j[endindex+2:index]
            if(method in totalSecond):
                if(maxSecond[method]<int(endindex_)):
                    maxSecond[method]=int(endindex_)
                totalSecond[method]=totalSecond[method]+int(endindex_);
            else:
                totalSecond[method] = int(endindex_)
                maxSecond[method]=int(endindex_)
        else:
            handleNewFAQMap[method] = 0


for i in f:
    j=str(i)

    # if( "[GC (Allocation Failure) " in j):
    #     print(j)


    # if("消耗了一个session，剩余：【" in j ):
    #     print(j)
    groupByThread("886c9672-a15a-4f2a-bc37-00fca4761023",j)
    parseLog('【handleNewFAQ】',j,countTimes,totalSecond)
    parseLog('【getConceptNodeList】',j,countTimes,totalSecond)
    parseLog('【getConceptNodeListByDepth】',j,countTimes,totalSecond)
    parseLog('【getEntityNodeList】',j,countTimes,totalSecond)
    parseLog('【getEntityNodeList】',j,countTimes,totalSecond)
    parseLog('【getEntityNodeListByParam】',j,countTimes,totalSecond)
    parseLog('【ifExistResult】',j,countTimes,totalSecond)

    #
    #
    #
    parseLog('【queryBySqlCount】',j,countTimes,totalSecond)
    #
    parseLog('【queryBySql】',j,countTimes,totalSecond)



for key in countTimes:
    total = totalSecond[key]
    count = countTimes[key]
    max = maxSecond[key]
    print(key+"-----一共运行【"+str(count)+"】次")
    print(key+"平均每次的请求时间【"+str(total/count)+"】ms "+"【"+str(total/(count*1000))+"】s")
    print(key+"最大的请求时间【"+str(max)+"】ms "+"【"+str(max/1000)+"】s")
    print("=====================================================================================")
    print()
print("-----------------------------------------------------------------------------------------")
print()
for key in threadListcont:
    print(key)
print("-----------------------------------------------------------------------------------------")
print()
# for key in threadMapcontMap:
#     v = threadMapcontMap[key]
#     for k in v:
#         print(k)
#     print("----------------------"+key+"-------------------------------------------")
#     print()

