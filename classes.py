# class Rectangle:
#     def setsides(self,x,y):
#         self.height=x
#         self.width=y
#         print(f'The sides of the rectangle are {self.height} and {self.width}')
#     def area(self):
#         return(self.height*self.width)
#     def parameter(self):
#         return 2*(self.height+self.width)

# recta1 = Rectangle()  #recta1(rectangle1) is a object of class Rectangel
# recta1.setsides(4, 5)
# print(recta1.area())
# print(recta1.parameter())

# programe to call constructor

class Rectangel:
    def __init__(self):
        print("method envoke without call")
obj1 = Rectangel()
obj2 = Rectangel()
