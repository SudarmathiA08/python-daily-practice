#method 1
'''var1="Dhoni"
print(var1,"is my captain")
#-------------------------------------------
var1="Dhoni"
var2=150
print(var1,"scored",var2,"runs")
#----------------------------------------------
var1="Ramesh"
var2="suresh"
print(var1,"and",var2,"are best friends")'''
from ast import iter_child_nodes
from ipaddress import summarize_address_range

#----------------------------------------------
#method2
var1="Dhoni"
print("%s is my captain"%(var1))
#---------------------------------------------
#method 3
var1="Dhoni"
print("{} is my captain".format(var1))
#-------------------------------------------------
var1="Dhoni"
var2=150
print("{} scored {} runs".format(var1,var2))
#-------------------------------------------------
var1="Suresh"
var2="Ramesh"
print("{} and {} are best friends".format(var1,var2))
#.......................
#India Scored 350 runs in 50 overs against Pakistan in 1996
var1="India"
var2=350
var3=50
var4="Pakistan"
var5=1996
print(var1,"Scored",var2,"runs in",var3,"overs against",var4,"in",var5)
#----------------------------------------------------------------
var1="India"
var2=350
var3=50
var4="Pakistan"
var5=1996

#-----------------------------------------------------------------
var1="Besant Tech"
print(var1[3:9])
print(var1[-8:-2])
print(var1[3:-2])
print(var1[-8:9])
 #------------------------------------------------------------
a=123
print(type(a))
#--------------------------------
a=("Besant")
print(type(a))
print(len(a))
#---------------------------------
num1=1234
print(type(num1))
num2=str(num1)
print(type(num2))
print(len(num2))
#-------------------------------------
a="1234"
print(type(a))
b=int(a)
print(type(b))
#-----------------------------------
nam1="BESANT TECH"
nam2="BeSant Tech"
print(nam1.lower())
print(nam2.lower())
print(nam1.title())
print(nam2.title())
print(nam1.capitalize())
print(nam2.capitalize())
print(nam1.upper())
print(nam2.upper())
print(nam1.swapcase())
print(nam2.swapcase())




