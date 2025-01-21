import sklearn as sk
# print(sk.__version__)

from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())


import sys
# print(sys.path)

# import harry
# print(harry.a)
#
# print(harry.printjoke("this is me"))

"""join function"""
"""
lis = ["John","cena","Randy","orton","Sheamus","khali","jion"]

for item in lis:
    print(item,"and ", end="")


a = " and ".join(lis)

print(a,"other wwe superstars")
"""
"""map function: mrmory location"""

# numbers = ["3","5","73"]
# print(map(int,numbers))
# numbers = list(map(int,numbers))
#
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# numbers[2] = numbers[2] + 1
# # print(numbers[2])

# def sq(a):
    # return a*a

# num = [2,3,4,5,6,8,7]
# squre = list(map(sq, num))
# print(squre)

# num = [2,3,4,5,6,8,7]
# squre = list(map(lambda x: x*x, num))
# print(squre)


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square,cube]
#
# num = [2,3,5,5,8,7]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

"""filter"""

# list_1 = [1,2,4,5,7,8]
#
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)

"""reduce"""
from functools import reduce

# list1 = [1,2,3,4]
# num = 0
# for i in list1:
#     num = num + i
# print(num)

# list1 = [1,2,3,5]
# num = reduce(lambda x,y:x+y,list1)
# print(num)

"""game"""
import random
no_of_choice = 5
nc = 5
i=0
p = 0
cp = 0
lst = ["s","g","w"]
print("s for snake")
print("g for gun")
print("w for water")
while i<no_of_choice:
    let = input("enter your guess: ")
    mgs = random.choice(lst)
    print("machine guess:",mgs)
    if let==mgs:
        print("Tie no point")
        print("your total point is:", p)
        print("machine totla point is:", cp)
        nc -= 1
        print("your guding left:", nc)
        i += 1
        continue
    elif let=="s" and mgs=="w":
        print("you win 1 point")
        p += 1
        print("your total point is: ", p)
        print("machine point is:", cp)
        nc -= 1
        print("your guding left:", nc)
        i += 1
        continue
    elif let=="g" and mgs=="s":
        print("you win 1 point")
        p += 1
        print("your total point is: ", p)
        print("machine point is:", cp)
        nc -= 1
        print("your guding left:", nc)
        i += 1
        continue
    elif let=="w" and mgs=="g":
        print("you win 1 point")
        p += 1
        print("your total point is: ", p)
        print("machine point is:", cp)
        nc -= 1
        print("your guding left:", nc)
        i += 1
        continue
    else:
        print("machine win 1 point")
        cp += 1
        print("your total point is:",p)
        print("machine totla point is:", cp)
        nc -= 1
        print("your guding left:", nc)
        i += 1
        continue



