#IF
#prime or not using if
num = int(input("Enter number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
#Palindrome or not
num = input("Enter a number: ")
rev = ""
for i in num:
    rev = i + rev
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
#Armstrong
num = int(input("Enter number: "))
a = num % 10
b = (num // 10) % 10
c = num // 100
if a*a*a + b*b*b + c*c*c == num:
    print("Armstrong")
else:
    print("Not Armstrong")
#Second largest
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
if (a>b and a<c) or (a>c and a<b):
    print("Second Largest:", a)
elif (b>a and b<c) or (b>c and b<a):
    print("Second Largest:", b)
else:
    print("Second Largest:", c)
#Perfect number
num = int(input("Enter number: "))
total = 0
for i in range(1, num):
    if num % i == 0:
        total = total + i
if total == num:
    print("Perfect")
else:
    print("Not Perfect")
#check whether character,digit,special character
ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
#check number divisible by 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
#check string start with vowel
string = input("Enter a string: ")
if string[0].lower() in "aeiou":
    print("Starts with vowel")
else:
    print("Does not start with vowel")
#find grade using mark
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
#Number lies between 50 and 100
num = int(input("Enter a number: "))
if 50 <= num <= 100:
    print("Number lies between 50 and 100")
else:
    print("Number does not lie between 50 and 100")
#FOR
#fibonacci series
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#sum of digit of a number
num = input("Enter a number: ")
total = 0
for digit in num:
    total = total + int(digit)

print("Sum of digits:", total)
#Reverse a number
num = input("Enter a number: ")
reverse = ""
for digit in num:
    reverse = digit + reverse
print("Reversed number:", reverse)
#count vowels in a string
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count = count + 1
print("Number of vowels:", count)
#largest element in a list
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest element:", largest)
#second largest number
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
second = numbers[0]
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest:", second)
#Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
newlist = []
for num in numbers:
    if num not in newlist:
        newlist.append(num)
print(newlist)
#count frequency of character
text = input("Enter a string: ")
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq)
#multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
#sum of even numbers
numbers = [10, 15, 20, 25, 30]
total = 0
for num in numbers:
    if num % 2 == 0:
        total = total + num
print(total)
#square of each elements
numbers = [2, 4, 6, 8]
for num in numbers:
    print(num * num)
#common elements in 2 list
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
for num in list1:
    if num in list2:
        print(num)
#maximum and minimum
numbers = [10, 25, 5, 40, 15]
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum:", maximum)
print("Minimum:", minimum)
#Star pyramid
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print("*" * i)
#count words in a sentence
sentence = input("Enter sentence: ")
count = 1
for ch in sentence:
    if ch == " ":
        count = count + 1
print("Number of words:", count)
