#Program to use math module (square root, power, factorial)
import math
num = int(input("Enter a number: "))
print("Square root:", math.sqrt(num))
print("Power:", math.pow(num, 2))
print("Factorial:", math.factorial(num))
#Display all functions in math module
import math
print(dir(math))
#Generate random numbers
import random
print("Random number:", random.randint(1, 100))
#Shuffle elements of a list
import random
list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print("Shuffled list:", list1)
#Generate random password
import random
import string
password = ""
for i in range(8):
    password = password + random.choice(string.ascii_letters)
print("Random Password:", password)
#Create user-defined module for arithmetic operations
import Arithmetic
print("Addition:", Arithmetic.add(5,3))
print("Subtraction:", Arithmetic.sub(10,4))
print("Multiplication:", Arithmetic.mul(4,2))
print("Division:", Arithmetic.div(8,2))
#Module to store student information
import Student
Student.student_info("John", 20, "BE")
#Module for area calculations
import Area
print("Area of Circle:", Area.circle(5))
print("Area of Square:", Area.square(4))
print("Area of Rectangle:", Area.rectangle(6,3))
#Use datetime module to display date and time
import datetime
now = datetime.datetime.now()
print("Current Date and Time:", now)
print("Year:", now.year)
print("Date:", now.date())
print("Time:", now.time())