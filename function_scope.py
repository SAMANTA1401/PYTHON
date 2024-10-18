x=1             #global variable
# def test():
    # y=2         #local variable
#     print("global variable",x )
#     print("local variable",y)
# test()

# print("global variable",x)
# print("local variable",y) #show error as y is a local variable inside test() function


def test1():
    global y
    global x
    x=x+2
    y=2
test1()
print("locaL Variable ",y)
print("global variable",x)




