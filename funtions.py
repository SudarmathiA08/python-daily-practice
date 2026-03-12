#positional arg
def student(name,age):
    print(name,age)
student("Sudar",21)
#---------------------------------------------------------------
#keyword arg
def student(name,age):
    print(name,age)
student(age=21,name="sudar")
#--------------------------------------------------------------
#default arg
def student(name="Sudar"):
    print("Saro",name)
student()
#------------------------------------------------------------------
#variable length arg
def course(*degree):
    print(degree)
course("BE","BCA","BA","BSC")
#---------------------------------------------------------------------------
#**kwargs
def student(**details):
    print(details)
student(name="sudar",age=21,course="python")
#----------------------------------------------------------------------------------
#combined arg
def details(name,age,*marks,**info):
    print(name,age,marks,info)
details("sudar",21,97,85,93,degree="BE",Bloodgroup="A+",dept="CSE",Mail="sudarmathi487@gmail.com")
#---------------------------------------------------------------------------------------------------------------------------------
for i in range(10):
    for j in range(10):
        print(i,j)
