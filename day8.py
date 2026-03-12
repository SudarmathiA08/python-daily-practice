#odd even using for
'''a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in a:
    if(i%2==0):
        print("even number:",i)
    else:
        if(i%2!=0):
            print("odd number:",i)
#----------------------------------------------------------------------
#multipication table
for i in range(1,11,1):
    print(i,"* 2 =",i*2)
#------------------------------------------------------------------------------------------------
#factorial of 5
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)'''
#---------------------------------------------------------------------------------------------------
#prime number
num=7
for i in range(2,num):
    if(num%i==0):
        print("not prime")
        break
else:
    print("prime")














