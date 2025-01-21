"""classes -Templates"""
# object - isinstance of the clas
# DRY - do not repeat yourself

# def get_no_of_films(srk):
"""
class Student:
    pass



harry = Student()
larry = Student()
print(harry, larry)
"""
# """instance variable"""
"""
harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subject = ["hindi","physics"]

print(harry.section, larry.subject)

"""
"""intances and class variables"""


# class Employee:
#     no_of_leaves = 8 #property of all  objects class variables properties of  class
#     # method
#     def printdetails(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


# object

# harry = Employee()
# rohan = Employee()

# object_own property: instance variable

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 557
# rohan.role = "student"

# print(rohan.role, harry.salary)
# print(rohan.no_of_leaves)
# print(Employee.no_of_leaves)
# print(Employee.__dict__)

# print(rohan.__dict__)

# Employee.no_of_leaves = 9
# print(Employee.no_of_leaves)
# instance variable for rohan
# rohan.no_of_leaves = 10
# print(rohan.no_of_leaves)
# print(harry.no_of_leaves)
# print(rohan.__dict__)
# print(Employee.__dict__)


# method
# print(rohan.printdetails())


# constructor

class Employee:
    no_of_leaves = 8  # property of all  objects class variables properties of  class

    # method
    def __init__(self, aname, asalary, arole):  # instance variable
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("harry", 455, "Instructor")

# rohan = Employee()


# rohan.name = "Rohan"
# rohan.salary = 557
# rohan.role = "student"


print(harry.salary)
print(harry.name)

# print(harry.no_of_leaves)

    