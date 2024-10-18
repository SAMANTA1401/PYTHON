# class Student:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
# s1=Student(45, 67)
# s2=Student(78, 76)
# s3=s1+s2

# operator overloading add

# class Student:
#     def __init__(self,n1): #class constructor
#         self.n1=n1
#     def __add__(self,other): #overloaded operator add
#         return (self.n1 + other.n1)

# s1=Student("Ignou ")
# s2=Student("University")
# s3=s1+s2
# print(s3)

# overloading comparison operator

class Student:
    def __init__(self,n1):
        self.n1=n1

    def __gt__(self,other):  #overloading operator12qw
            p1=self.n1
            p2=other.n1
            if p1>p2:
                return True
            else:
                return False
s1=Student(10)
s2=Student(20)
if s1>s2:
    print('s1 win')
else:
    print('s2 win')





    

