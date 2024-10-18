# try-Exception

# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     # pass
#     print("Exception raised: ", msg)
# print("welcome")

# try:
#     num1 = int(input("Enter the first number :"))
#     num2 = int(input("Enter the second number :"))
#     print(num1/num2)
# except ZeroDivisionError as msg:
#     print("can't divide by zero :",msg)
# except ValueError as msg2:
#     print("Please enter integer valur only :",msg2)
    

# try:
#     print("inside try")
#     print(56/0)
# except ZeroDivisionError:
#     print("iside except")
# finally:
#     print("finally print")

# nested try

# try:
#      print("outer try block")
#      try:
#         print("Inner try block")
#         print(22/0)
#      except ZeroDivisionError:
#         print("except inner try")
#      finally:
#         print("finally inner try")
# except :
#     print("except outer try")
# finally:
#     print("finally outer try")

# single except block multiple Exception

# try:
#     num1 = int(input("Enter the first number :"))
#     num2 = int(input("Enter the second number :"))
#     print(num1/num2)
# except (ZeroDivisionError,ValueError) as printmsg:
#     print("Invalid number and Error is : ",printmsg)

# default except

# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("ZeroDivisionError:Can't divide with zero")
# except:
#     print("Default Except: Plz provide valid input only")

# user difined Exception

# class EligibleForEntrance(Exception):
#     def __init__(self,arg1):
#         self.msg1=arg1

# class NotEligible(Exception):
#     def __init__(self,arg1):
#         self.msg1=arg1  

# percentage=int(input("Enter your pcm marks percentage : "))
# if percentage>50:
#     raise EligibleForEntrance("you can apply for the entrance examination ")
# else:
#     raise NotEligible("you cant apply for the entrance examination ")

# Program to raise an exception.

