class student:

    i = 100
    def run(self):
        pass
    def getName(self,id):
        k=""
        if(id=="1"):
            k="中国"
        elif(id=="2"):
            k = "美国"
        elif(id=="3"):
            k="英国"
        return k

st = student()
print(st.getName(2))