"""if-elif-else"""
var1 = 6
var2 = 56
# input() alwyas take as string
# var3 = int(input())
#
# if var3>var1: #if condition
#     print("greater")
# # if var3==var1:
# elif var3==var1:
#     print("equal")
# else:
#     print("lesser")

# list = [3,5,8,9,10]
# print(15 in list)
# element = int(input())
# if element in list:
#     print("yes it is in the list")
# else:
#     print("it is not in the list")

# print("enter your age:", end="")
# age = int(input())
#
# if age in range(10,100):
#     if age>=18:
#         print("you are eligible")
#     else:
#         print("you are not eligible")
# else:
#     print("enter a valid age")

print("enter 1st no:", end="")
n1 = input()
print("enter 2nd no:", end="")
n2 = input()
print("enter operation:", end="")
opr = input()
try:
    if int(n1)==45 and int(n2)==3 and opr=="*":
        print(n1,"*",n2,"=",555)
    elif int(n1)==56 and int(n2)==9 and opr=="+":
        print(n1,"+",n2,"=",77)
    elif int(n1)==56 and int(n2)==6 and opr=="/":
        print(n1,"/",n2,"=",14)
    else:
        if opr=="+":
            print(n1,opr,n2,"=",int(n1)+int(n2))
        elif opr=="-":
            print(n1,opr,n2,"=",int(n1)-int(n2))
        elif opr=="*":
            print(n1,opr,n2,"=",int(n1)*int(n2))
        elif opr=="/":
            print(n1,opr,n2,"=",int(n1)/int(n2))
        else:
            print("please enter valid operation.")
except Exception as e:
    print(e)

"""for-loop"""
list1 = [["Harry",1], ["larry",2],["carry",3],["marry",4]]
# list1 = ("Harry", "larry","carry","marry")
# we can not iterate all type of datatypes
# for item in list1:
#     print(item)
# dict1 = dict(list1)
# print(dict1)
# for item,lollypop in list1:
#     if lollypop>2:
#          print(item, "and lolly is ", lollypop)
# # print key and values from dict
# for item,lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)
# print only keys from dict
#
# items = [int, float, "harry", 5,6,7,34,56,12]
# for item in items:
#     if str(item).isnumeric() and item>6:
#         print(item)

"""WHILE LOOP"""

# i = 0
# while (i<20):
#     print(i)
#     i += 1
"""break and continue"""

# i = 0
# # while (i<20):
# #     print(i+1, end=" ")
# #     i += 1
# while (True):
#     if i+1<5:
#         i += 1
#         continue
#     print(i+1, end=" ")
#     if (i==44):
#         break #stop the loop
#     i += 1

# while(True):
#     inp = int(input("Enter a Number: "))
#     if inp>100:
#         print("Congrats you have entered a number greater than 100")
#         break
#     else:
#         print("try again")
#         continue
"""
i = 1
no_of_guess = 6
ex_no = 25

while(no_of_guess != 0):
    in_no = input("Enter a Number: ")
    try:
        if int(in_no)>50:
            print("you enter too large")
            no_of_guess -= 1
            i += 1
            print("guess left:",no_of_guess)
            continue

        elif 50>int(in_no)>30:
            print("you enter large no")
            no_of_guess -= 1
            i += 1
            print("guess left:", no_of_guess)
            continue
        elif int(in_no)<20:
            print("you enter small no")
            no_of_guess -= 1
            i += 1
            print("guess left:", no_of_guess)
            continue
        elif int(in_no)<0:
            print("you enter too small no")
            no_of_guess -= 1
            i += 1
            print("guess left:", no_of_guess)
            continue
        elif 30>int(in_no)>25:
            print("you enter large no, about to near")
            no_of_guess -= 1
            i += 1
            print("guess left:", no_of_guess)
            continue
        elif 20<int(in_no)<25:
            print("you enter small no, about to near")
            no_of_guess -= 1
            i += 1
            print("guess left:", no_of_guess)
            continue
        elif in_no==ex_no:
            print("weldone , you complete in", i , "guess!")
            break
        else:
            print("please enter valid number")
            continue
    except Exception as e:
        print(e)
while(no_of_guess==0):
    print("you exhust your guess no")
    print("game over")
    break
"""
""" OPERATOR"""
"""arithmatics operator: +,-,*,/,**,//,%"""
"""asignment operator: =,+=,-=,*=,/=,%="""
"""comparison operator: ==,<=,>=,!="""
"""ligical operator: True,False"""
"""identity operator: is not!=, is =="""
"""membership operator: in, not in"""
"""bitwise operator:binary"""
# i=5
# print(i==5)
# print(5 == 5)
# list2 = [3,4,7,9,4,2,8]
# print(34 in list2)
# print(34 not in list2)
# print(0 & 1)
# print(0 | 1)
"""shorthand if else"""
"""one liner"""
# a=7
# b=3
# if a>b: print("a greater than  b ")
# print("a greater than b") if a<b else print("a less than b")



