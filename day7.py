'''#if else (odd or even)
a=int(input("enter the value of a:"))
b=2
if(a%b==0):
    print("a is even")
else:
    print("a is odd")
#----------------------------------------------------------------------------------------------------------
#check the number div by both 5 and 3
a=int(input("enter the value of a:"))
if(a%5==0 and a%3==0):
    print("yes, this number is divided by both 5 and 3")
else:
    print("no,it is not divided by both 5 and 3")
#-----------------------------------------------------------------------------------------------------------
#username login
a=input("enter your password:")
if(a=="sudar2308"):
    print("you are allowed to entered into the site")
else:
    print("your password is wrong")
#-----------------------------------------------------------------------------------------------------------
#traffic sign speed
speed=int(input("enter your vehicle speed:"))
if(speed>=90):
    print("you are going in a high speed")
else:
    print("your speed is good")
#--------------------------------------------------------------------------------------------------------
#check password length
a=input("enter the password:")
if(len(a)>8):
    print("your password is strong")
else:
    print("your password is weak")
#----------------------------------------------------------------------------------------------------------
#ecommerce discount
a=int(input("enter the price:"))
if(a>=5000):
    print("wow! you got 10% discount for your purchase")
else:
    print("sorry!😥 you won't got discount")
#------------------------------------------------------------------------------------------------------------
#elif(calculator)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=input("enter the operator or operation to perform:")
if(c=="+" or c=="add"):
    print(a+b)
elif(c=="-" or c=="sub"):
    print(a-b)
elif(c=="*" or c=="mul"):
    print(a*b)
elif(c=="/"or c=="div"):
    print(a/b)
elif(c=="%" or c=="mod"):
    print(a%b)
else:
    print(a**b)
#----------------------------------------------------------------------------------------------------------------
#Traffic signal system
a=input("enter the color:")
if(a=="red"):
    print("you are allowed to walk")
elif(a=="yellow"):
    print("walk fast!!vehicles are get ready to move")
else:
    print("you are not allowed to walk")
#------------------------------------------------------------------------------------------------------------
#season find
season=input("enter the season:")
if(season=="rain"):
    print("it is a rainy season")
elif(season=="hot"):
    print("it is a summer season")
elif(season=="snow"):
    print("it is a winter season")
else:
    print("it is a spring season")
#-------------------------------------------------------------------------------------------------------------------
#nested if(3 numbers which is greater)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print("c is greater")
else:
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")
#-----------------------------------------------------------------------------------------------------
#checking username and password
username=input("enter the username:")
password=input("enter the password:")
if(username=="Sudarmathi"):
    if(password=="sudar2308"):
        print("you are allowed")
    else:
        print("enter valid password")
else:
    print("enter valid username")
#-------------------------------------------------------------------------------------------------------
#ATM pin and balance
pin= int(input("enter your pin:"))
amount=int(input("enter the amount:"))
if(pin==2308):
    if(amount>=1000):
        print("collect your amount")
    else:
        print("Insufficient account balance")
else:
    print("pin is incorrect,enter valid pin")
#----------------------------------------------------------------------------------------------
#job eligibility
age=int(input("enter your age:"))
Degree=input("enter the degree:")
if(age==21):
    if(Degree=="BE"):
        print("you are eligible")
    else:
        print("your degree is not eligible for this job")
else:
    print("you are not eligible")'''
#----------------------------------------------------------------------------------------
#checking the number if it is positive,even,div by3
num=int(input("enter the number:"))
if(num>=0):
    print("it is positive number")
    if(num%2==0):
        print("it is a even number")
    else:
        print("it is a odd number")
    if(num%3==0):
        print("it is divisible by 3")
    else:
        print("it is not divisible by 3")
else:
    print("it is negative number")
    if(num%2==0):
        print("it is a even number")
    else:
        print("it is a odd number")
    if(num%3==0):
        print("it is divisible by 3")
    else:
        print("it is not divisible by 3")




