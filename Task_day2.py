#print 1 to 10
for i in range(1,11):
    print(i)
#print even number 1 to 50
for i in range(1,51):
    if i%2==0:
      print("Even numbers are:",i)
#print odd number 1 to 50
for i in range(1,51):
    if i%2!=0:
      print("odd numbers are:",i)
#sum of numbers 1 to 100
sum=0
for i in range(1,101):
    sum+=i
print("sum of numbers are:",sum)
#multiplication table of number
table=int(input("enter a number:"))
for i in range(1,11):
    print(i,"*",table,"=",i*table)
#count numbers in a list
Numbers=[10,20,30,40,50,60,65]
count=0
for i in Numbers:
    count+=1
print("count of numbers are:",count)
#print all elements in a list
list=[5,10,15,20,25]
for i in list:
 print(i)
#count vowels in a string
name = input("Enter a string: ")
count = 0
for ch in name:
    if ch in "aeiouAEIOU":
        count += 1
print("Number of vowels:", count)
#print number in reverse
for i in range(10,0,-1):
    print(i)
#factorial
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial is:", fact)
#largest number in a list
values = [10, 45, 23, 89, 12]
largest = values[0]
for i in values:
    if i > largest:
        largest = i
print("Largest number:", largest)
#count digits in a number
num = int(input("Enter number: "))
count = 0
for i in str(num):
    count += 1
print("Number of digits:", count)
#print squares from 1 to 10
for i in range(1,11):
    print(i,"square is",i*i)
#print cube from 1 to 10
for i in range(1,11):
  print(i,"cube is",i*i*i)
#sum of number in a list
num=[2,3,4,5,6]
sum=0
for i in num:
    sum+=i
print("sum of numbers in a list:",sum)


