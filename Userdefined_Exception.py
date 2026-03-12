'''try:
    num=int(input("enter no:"))
    if num<0:
        raise ValueError("negative number not allowed")
    print(num)
except ValueError as e:
    print(e)
#--------------------------------------------------------------------------------------
try:
    age=int(input("enter your age:"))
    if age<18:
        raise ValueError("not eligible for vote")
    print("eligible for vote")
except ValueError as e:
    print(e)
#------------------------------------------------------------------------
class AgeError(Exception):
    pass
try:
    age=int(input("enter your age:"))
    if age<18:
        raise AgeError("not eligible")
    print("eligible")
except AgeError as e:
    print(e)'''
#---------------------------------------------------------------------
class BalanceError(Exception):
    pass
try:
    Balance=int(input("Enter the amount:"))
    if Balance<500:
        raise BalanceError("Insufficient balance")
    print("Collect your amount")
except BalanceError as e:
    print(e)
