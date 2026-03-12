#add 2 numbers
def add(a,b):
    return a+b
print(add(5,10))
#sub 2 numbers
def sub(a,b):
    return a-b
print(sub(56,32))
#multiply 2 numbers
def mul(a,b):
    return a*b
print(mul(12,5))
#div 2 numbers
def div(a,b):
    return a/b
print(div(50,2))
#square of number
def square(n):
    return n*n
print(square(12))
#odd or even
def odd_even(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
num=int(input("enter a number:"))
odd_even(num)
#largest of two numbers
def largest(a,b):
    if a>b:
        print(a,"is a largest number")
    else:
        print(b,"is a largest number")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
largest(num1,num2)
#count vowels in a string
def count_vowel(text):
    count=0
    for i in text:
        if i in "aeiouAEIOU":
            count+=1
    return count
string=input("enter a string:")
print(count_vowel(string))
#reverse a string
def reversing(text):
    reverse=""
    for i in text:
        reverse=i+reverse
    return reverse
string=input("enter a string to reverse:")
print(reversing(string))
#factorial of number
def factorial(value):
    fact=1
    for i in range(1,value+1):
        fact=fact*i
    return fact
result=int(input("enter a number:"))
print(factorial(result))
#sum of list elements
def list_sum(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum
my_list=[1,2,3,4,5]
print(list_sum(my_list))
#maximum num in list
def max_list(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
num_list=[23,78,47,32,98]
print(max_list(num_list))
#prime or not
def check_prime(value):
    if value <= 1:
        print(value, "is not a prime number")
        return
    for i in range(2, value):
        if value % i == 0:
            print(value, "is not a prime number")
            return
    print(value, "is a prime number")
number = int(input("Enter a number: "))
check_prime(number)
#count character in string
def count_char(string):
    count=0
    for i in string:
         count+=1
    return count
my_str=input("enter a string:")
print(count_char(my_str))
#multipication table
def mul_table(num):
    for i in range(1,11):
        print(i,"*",num,"=",i*num)
num=int(input("enter a number:"))
mul_table(num)
#fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
num = int(input("Enter number of terms: "))
fibonacci(num)
#second largest
def second_largest(list):
    list.sort()
    print("Second largest:", list[-2])
numbers = [10, 5, 8, 20, 15]
second_largest(numbers)
#average of number in a list
def average(list):
    total = 0
    for i in list:
        total = total + i
        avg = total / len(list)
    print("Average:", avg)
numbers = [10, 20, 30, 40]
average(numbers)
#even number from list
def even_numbers(list):
    for i in list:
        if i % 2 == 0:
            print(i)
numbers = [1,2,3,4,5,6,7,8]
even_numbers(numbers)
#sum of digit
def sum_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    print("Sum of digits:", total)
number = int(input("Enter number: "))
sum_digits(number)
#remove duplicates
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
numbers = [1,2,2,3,4,4,5]
remove_duplicates(numbers)
#frequency of character
def char_frequency(text):
    for i in text:
     print(i, ":", text.count(i))
string = input("Enter a string: ")
char_frequency(string)
#max and min val in list
def max_min(list):
    print("Maximum:", max(list))
    print("Minimum:", min(list))
numbers = [5,10,2,20,8]
max_min(numbers)
#check palindrome or not
def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
word = input("Enter a word: ")
palindrome(word)
#Function to sort list without using sort()
def sort_list(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print(list)
numbers = [5,2,8,1,9]
sort_list(numbers)


