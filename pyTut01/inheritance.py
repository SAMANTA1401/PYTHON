"""inheritance"""

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

# programmer class inherit from employee class: single inheritance

class Programmer(Employee):
    no_of_holidays = 23
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"the programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role} and the language is {self.languages}"




harry = Employee("harry",455,"Instructor")
rohan = Employee("rohan",855,"trainer")
kiran = Employee.from_str("rohan-685-mentor")

shubham = Programmer("Shubham", 908, "Programmer",["python"])
abhi = Programmer("Abhi", 808, "Programmer",["java"])


# print(kiran.salary)
# kiran.printgood("harry")
print(abhi.printprog())
print(abhi.printdetails())
print(abhi.no_of_holidays)
"""
"""multiple inheritance"""

class Employee:
    _protect = 5
    __private = 90
    var =8
    no_of_leaves = 8 #property of all  objects class variables properties of  class
    print(__private)
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

class Player:
    var =9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name}. game is {self.game} "

class CoolProgrammer(Employee, Player):
    # var = 10
    language = "C++"
    def printlanguage(self):
        print(self.language)





harry = Employee("harry",455,"Instructor")
rohan = Employee("rohan",855,"trainer")
kiran = Employee.from_str("rohan-685-mentor")
shubham = Player("subham",["Cricket"])
karan = CoolProgrammer("karan",5677,"CoolProgrammer")

# karan.printlanguage()
# print(karan.printdetails())

# print(karan.var)

print(harry._protect)
print(harry._Employee__private)
