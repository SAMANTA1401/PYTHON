# class MethodOverloading:
#     def method1(self):
#         print('method without argument')
#     def method1(self,x):
#         print("method only with single argument")
#     def method1(self,x,y):
#         print("method with two argument")
# obj1 = MethodOverloading()
# obj1.method1()
# obj1.method1(2)
# obj1.method1(4, 4)


# method overriding

# class University:
#     def UnivName(self):
#         print('Ignou university')

#     def course(self):
#         print('bca')
# class student(University):
#     def course(self):  #overridded method
#         print('mca')

# stud1 = student()
# stud1.UnivName()
# stud1.course()

#using super() keyword

class University:
    def UnivName(self):
        print('Ignou university')

    def course(self):
        print('bca')
class student(University):
    def course(self):  #overridded method
        super().course()
        print('mca')

stud1 = student()
stud1.UnivName()
stud1.course()


