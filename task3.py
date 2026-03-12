'''#odd number
for i in range(1,52):
    if(i%2==0):
        continue
    print(i)
#---------------------------------------------------------------------------------------
#skip vowels
a = "python programming"
for i in a:
    if i in "aeiou":
        continue
    print(i)
#-----------------------------------------------------------------------------------
#skip negative numbers in a list
a = [10, -5, 20, -3, 30, -90]
for i in a:
    if i < 0:
        continue
    print(i)
#-----------------------------------------------------------------------------------------------
#divisible by 5 from 1 to 50
for i in range(1, 51):
    if i % 5 != 0:
        continue
    print(i)
#------------------------------------------------------------------------------------------------
#number is prime or (not using break)
num = 7
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
#------------------------------------------------------------------------
#stop when user enters 0 using while
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    print("You entered:", num)
#------------------------------------------------------------------
#stop when number is found
a = [10, 20, 30, 40, 90, 80, 70]
search = 90
for i in a:
    if i == search:
        print("Number Found")
        break
else:
    print("Number Not Found")'''
#---------------------------------------------------------
num=981
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)
























































