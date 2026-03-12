#IF
#positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print(" is a Positive number")
else:
    print(" is a Negative number")
#odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#largest of 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)
#largest of 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest number is:", a)
elif b > a and b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
#divisble by 5 and 11
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11")
else:
    print("Number is not divisible by both 5 and 11")
#leap or not
year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
#vowel or consonant
ch = input("Enter character: ")
if ch in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")
#multiple of 3 and 7
num = int(input("Enter number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of 3 and 7")
else:
    print("Not multiple of 3 and 7")
#3 digit number
num = int(input("Enter number: "))
if num >= 100 and num <= 999:
    print("Three digit number")
else:
    print("Not three digit number")
#greater than 100
num = int(input("Enter number: "))
if num > 100:
    print("Greater than 100")
else:
    print("Not greater than 100")