"""File to Basics"""
"""
"r"-open file for reading
"w"-open a file for 
"x"-Creates file if not exists
"a"-Add more content to a file
"t"-text mode
"b"-binary mode
"+"-read and write
"""

# f = open("harry.txt", "r")
# f = open("harry.txt", "rb")
# f = open("harry.txt", "rt")
#
# content = f.read()
# print(content)
# content = f.read(3)
# print("1",content)
# for line in content:
    # print(line)


# for line in f:
#     print(line)
#
# print(f.readline())
# print(f.readline())

# list of line
# print(f.readlines())
# f.close()


# f1 = open("harry1.txt", "w")
# f1 = open("harry1.txt", "a")
#
# a = f1.write("i am a good boy\n")
# print(a)

# f1.close()

"""handle read and write both"""

# f2 = open("harry2.txt", "r+")
# print(f2.read())
# f2.write("thank you")
# print(f2.read())

"""pattern printing"""

# print("*")
# """

a = int(input())
print(a)
b = int(input())
print(b)
c = bool(b)
print(c)
# i=0
if c==True:
    # for i in range(a):
        # print("* "*(i+1))
        # i += 1
    # for i in range(0,a+1):
    #     print("* "*i)
    count = 1
    while (count<=a):
        print("*"*count, end="")
        print("\n", end="")
        count = count +1
elif c==False:
    # for i in range(a):
    #     print("* "*a)
    #     a -= 1
    # for i in range(a,0,-1):
    #     print("* "*i)
    count = a
    while (count != 0):
        print("*" * count, end="")
        print("\n", end="")
        count = count - 1
else:
    print("invalid input")

# """
"""
f5 = open("harry.txt")
f5.seek(5)
print(f5.tell())
print(f5.readline())
print(f5.tell())
"""
# to find file pointer
"""
f5.seek(0)
print(f5.readline())
f5.close()
"""
#
# with open("harry.txt") as f:
#     a = f.read(4)
#     print(a)

"""Health management system for 3 clients"""

def getdate():
    import datetime
    return datetime.datetime.now()
