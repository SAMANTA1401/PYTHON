"""*args,  **kwargs """

# def function(a,b,c,d):
#     print(a,b,c,d,e)

# def funargs(*args):
#     # print(type(args))
#     # print(args[0])
#     for item in args:
#         print(item)

# def funargs(normal, *args):
#     print(normal)
#     for item in args:
#         print(item)
#
# normal = "this is normal"
# har = ["harry","carry","charry","marry"]
# # har = ["harry","carry","charry","marry","larry"]
#
# funargs(normal,*har)
"""
def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, values in kwargs.items():
        print(key,values)



normal = "this is normal"
har = ["harry","carry","charry","marry"]
# har = ["harry","carry","charry","marry","larry"]
kw = {"rohan":"monitor","harry":"fittness triner","sary":"programmer"}
funargs(normal,*har,**kw)

"""

"""enumarate"""
l1 = ["Bhindi", "Aloo", "chopstic", "chowmin"]

i = 1
for item in l1:
    if i%2 != 0:
        print(f"Jarvis please buy {item}")

for index , item in enumerate(l1):
    if i%2==0:
        print(f"Jarvis please buy {item}")

"""list"""
grocery = ["lolipoop","kitkat","matshmello","pie",57,67,23]
# print(grocery)
# print(grocery[4])

numbers = [3,6,9,2,5,0,4]
# numbers.sort()
# numbers.reverse()
# print(numbers)
"""slicing"""
# print(numbers[:])
# print(numbers[1:4])
# print(numbers)
# print(numbers[::2])
# print(numbers[::3])
# print(numbers[::-2])
# # Exception
# print(numbers[1:6:-2])
# print(numbers[::-1])
"""append"""
# numbers.append(7)
# numbers.append(7)
# numbers.remove(9)
# numbers.pop()
# print(numbers)
# numbers2 = []
# numbers2.append(3)
# numbers2.append(8)
# numbers2.insert(1,67 )
# print(numbers2)
"""change the value in lisr"""
# numbers[3] = 56
# print(numbers)
"""Mutable"""
# can change like list
"""immutable"""
# can not change like tupple
"""tupple"""
tp = (4,5,7,8)
# can not change
# tp[2] = 9
# tp2 = (4)
# tp2 = (4,)
# print(tp2)
"""change the variable value"""
a = 3
b = 8
# print(a,b)
# temp = a
# a = b
# b = temp
# print(a,b)

# a, b = b, a
# print(a,b)
"""dictionary"""

d1 = { }
# print(type(d1))
d2 = {"harry":"burger", "rohan":"fish", "pk":"chicken", "subham":{"a":"fg", "b":546,"c":"yu"}}
# print(d2)
# print(d2["subham"])
# print(d2["subham"]["b"])

# d2["ankit"] = "junk food"
# d2[45] = "arpan"
# del d2["pk"]
# print(d2)

"""Copy"""

print(d2.copy())

"""time module"""
import time

initial = time.time()
print(initial)

# for i in range(45):
#     print("this is harry bhai")
#     time.sleep(2)
# print("for loop ran time", time.time()-initial, "seconds")
# # initial2 = time.time()
# # k=0
# while(k<45):
#     print("this is harry bhai")
#     k+=1
# print("while loop ran time ", time.time()-initial2, "seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)



"""enumarate function"""
"""
l1 = ["bhindi","aloo","chopstics","chowmein"]

i = 1
for  item in l1:
    if i%2 != 0:
        print(f"Jarvice please buy {item}")
    i += 1

b
for index, item in enumerate(l1):
    if i%0 ==0:
"""

"""decorator"""


@dec1
def who_is_harry():
    print("harry is a good boy")


# who_is_harry = dec1(who_is_harry)

who_is_harry()




