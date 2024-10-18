class Parent:
    def methodAl():
        print("method 1 of parent class")
    def methodA2():
        print("method 2 of parent class")

        
class Child(Parent):
    def methodB1():
        print("method 1 of parent class")
    def methodB2():
        print("method 2 of parent class")

class C2(Parent,Child):
    def methodC1():
        print("child 2")



obj1 = Parent
obj1.methodAl()
# obj1.methodA2()

obj2 = Child
obj2.methodA2()
obj2.methodB2()

obj3 = C2
obj3.methodAl()
obj3.methodB1()
obj3.methodC1()
