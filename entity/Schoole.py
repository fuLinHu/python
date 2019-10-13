import Student
from importlib  import reload
Student.runStudent("付林虎")
reload(Student)
num = 0;
def sum():
    print(globals())
    print(locals())
    for i in range(10):
        global num
        num=num+i;
print(num)
sum()
print(num)

print(dir(Student))

