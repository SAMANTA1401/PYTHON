# Given a list, write a Python program to convert the given list to string.
lis = ['sourav ','khanra ', 'weds ','sudipta ', 'maity']

def list_to_string(list1):
    str1= ""                  #initialize a empty string
    # for el in list1:
    #     str1 += el
    str2 = str1.join(list1)
    
    return str2

# print(list_to_string(lis))

# In this program, we will try to convert a given string to a list, 
# where spaces or any other special characters, according to the users choice,
#  are encountered. To do this we use the split(
str2 = "sourav khanra weds sudipta maity"
def string_to__list(st):
    # li = st.split(" ")
    li = [i for i in st]
    print(li)

# string_to__list(str2)

def Convert(string):
    list1=[]
    list1[:]=string
    return list1
# Driver code
str1="ABCD"
# print(Convert(str1))

# : Using re.findall() method This task can be performed using regular expression. We can used the pattern to matched all the alphabet and make list with all the matched elements. 

# Python3
import re
def Convert(string):
    return re.findall('[a-zA-Z]', string)
str1="ABCD"
print(Convert(str1))


s="geeks"
x=[i for a,i in enumerate(s) ]
print(x)