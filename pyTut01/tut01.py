# multiline
# line
# coment
"""euiwnjunh"""
# print("harry", end=" ")
# print("hi")
# print("abc","xyz")
"""ESCAPE SEQUENSES"""
# print("abcd\\")
# print("abcd\"")
# print("abcd \n good boy \tbas")
"""VARIABLES"""
# var1 = "Hello world\n
# float
# var2 = 45.5
# var3 = 45
# var4 = " 45"
# var5 = " 67"
# print(type(var3))
# print(var1 +var3) # error different data types
# print(var1+var4)
# print(int(var5)+int(var4))
# print(50*str(int(var5)+int(var4)))
# print(var1*100, "\n")
"""quize"""
# print("enter your first number:")
# var1 = input()
# print("enter your second number:")
# var2 = input()
# sum = int(var1)+int(var2)
# print("the sum of these two number is:",sum)
"""input"""
# print("input your number:")
# inpunum = input()
# #inpunum is string
# print("you enter -", int(inpunum)+10)

"""string"""
myString = "hey you listen to me"
# print(myString[4])
# print(len(myString))
# # 0 to 3 print
# print(myString[0:4])
# # string index 0 to 19
# print(myString[0:19])
# # skip one character
# print(myString[0:19:2])
# # print 0 to all/length
# print(myString[0:])
# # print first\0 to 19
# print(myString[:19])
# # print total length
# print(myString[:])
# print(myString[0:19:1])
# # 0,20,1 default
# print(myString[::])
# # skip 3 character
# print(myString[::3])
# # reverse indexing
# print(myString[-1:])
#
# print(myString[-4:-2])
# print(myString[16:18])
# # reverse the string
# print(myString[::-1])
# print(myString[::-2])
#
# print(myString.isalnum())
# print(myString.isalpha())
# print(myString.endswith("me"))
# print(myString.count("o"))
# print(myString.find("to"))
# print(myString.replace("to","for"))
#
# myString2 = "heyyoulistentome"
# print(myString2.isalnum())
# print(myString2.capitalize())
# print(myString2.upper())
# print(myString2.lower())

"""LIST"""
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

# print(d2.copy())
# d3 = d2
# del d3["pk"]
# print(d2)
# print(d3)

# d4 = d2.copy()
# print(d4)
# del d4["pk"]
# print(d4)
# print(d2)

"""update"""
d2["ankit"] = "junk food"
d2.update({"Leena":"Toffe"})
# print(d2)

"""keys"""
# print(d2.keys())
""":key values"""
# print(d2.items())

"""set, list of well defined object, contain only unique value"""
s = set()
# s_from_list = set([1,3,5,6])
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(1)
s.add(2)
print(s)
s1 = s.intersection({1, 3, 2, 4})
print(s, s1)
print(s.isdisjoint(s1))
s.remove(2)
print(s)





