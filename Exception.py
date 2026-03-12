#method1
try:
    a=10
    b=0
    print(a/b)
except:
    print("Error")
#method2
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
#method3
try:
    a=10
    b=0
    print(a/b)
except Exception as e:
    print(e)
#Multiple Exception
#met 1
try:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    result=a/b
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("please enter numbers only")
#met 2
try:
    a=int(input("enter a num"))
    b=int(input("enter a num"))
    result=a/b
    print(result)
except(ZeroDivisionError,ValueError):
    print("error occured")
#met 3
try:
    num=int("hello")
except ValueError as e:
    print(e)
#met 4
try:
    print(a)
except Exception as s:
    print(s)
try:

    a=int(input("enter no"))
    b=int(input("enter no"))
    result=a/b
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Ivalid Input")
else:
    print(result)
finally:
    print("Completed")

