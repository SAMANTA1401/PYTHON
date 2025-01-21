import static_method

"""
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


harry = Employee("harry",455,"Instructor")
rohan = Employee("rohan",855,"trainer")

# harry.no_of_leaves = 10
# Employee.no_of_leaves = 9

harry.change_leaves(12)
# Employee.change_leaves(12)


# print(harry.no_of_leaves)
# print(Employee.no_of_leaves)
"""

"""alternative constructor"""


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
# to create a new object through classmethod
    @classmethod
    def from_str(cls, string):#parse alternative constructor
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    # static_method
    @staticmethod
    def printgood(string):
        print("this is good" + string)


harry = Employee("harry",455,"Instructor")
rohan = Employee("rohan",855,"trainer")
kiran = Employee.from_str("rohan-685-mentor")


print(kiran.salary)
kiran.printgood("harry")