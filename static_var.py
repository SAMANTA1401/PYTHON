class check:
    a=100 #static variable
    def __init__(self):
        self.b=200
obj1=check()
print(obj1.a,obj1.b)
check.a=888
print(obj1.a)
obj1.a=222
print(obj1.a)