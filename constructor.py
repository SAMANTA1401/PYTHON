class C1:
    def __init__(self): #constructor of class c1
        print("constructor of c1")
    def methodC1():
        print("m1 of c1")
# class C2(C1):
    # def __init__(self): #constructor of class c2
        # print("constructor of c2")
# obj1=C1()
# obj2=C2()

# 
# class C2(C1):
#     def __init__(self): #constructor of class c2
#         super().__init__() #calling parent class c1 constructor
#         print("constructor of c2")

class C2:
    def __init__(self): #constructor of class c1
        print("constructor of c1")
    def methodC1():
        print("m1 of c1")

class C3(C1,C2):
    def __init__(self):
        super().__init__()
        print("constructor of c3")


# obj2=C2()

obj3=C3()
# obj2=C2()
