class Myclass:
    def __init__(self,a1,b2,c3): #constructor
        self.a1=a1
        self.b2=b2
        self.c3=c3
    def avg(self):  #instace method
        return (self.a1+self.b2+self.c3)/3
obj1=Myclass(3, 3, 6)
print(obj1.avg())
