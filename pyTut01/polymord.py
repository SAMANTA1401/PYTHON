"""
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "instance var in class A"
        self.special = "Special"
class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        # super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "instance var in class   B"
        super().__init__()
        print(super().classvar1)
    pass

#make 2 instance variable
a = A()
b = B()

print(b.classvar1)
print(b.special)
print(b.var1)

"""
"""dimend shape problem"""
"""
class A:
    def met(self):
        print("this is a method from class A")

class B(A):
    def met(self):
        print("this is a method from class B")
    pass

class C(A):
    def met(self):
        print("this is a method from class C")
    pass

# class D(B,C):
class D(C,B):
    def met(self):
        print("this is a method from class D")
    pass

a = A()
b = B()
c = C()
d = D()

d.met()
"""
"""operator overloading"""
class Employee:
    no_of_leaves = 8 #property of all  objects class variables properties of  class
    # method
    def __init__(self, aname, asalary, arole): #instance variable
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
# classmethod decorator
    @classmethod
    def change_leaves(cls, newleaves):# cls is class of object running to chamge cladss method atribute not instance atribute also change atribute of another object llike rohan
        cls.no_of_leaves = newleaves

    #dunder method
    #mappping operator to functions
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 = Employee("harry", 456, "Prgrammer")
emp2 = Employee("rohan", 456, " cleaner")

print(emp1+emp2)
print(emp1/emp2)
print(str(emp1))
print(repr(emp1))


