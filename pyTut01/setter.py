"""srtter"""
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.elmil = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return  f"This employee is {self.fname} {self.lname}"

    def printemail(self):
        pass
    @property #decorator
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set, please set it through setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"
    @email.setter
    def email(self,string):
        print("setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None




hindustani_supporter = Employee("Hindustani", "Supporter")
nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.explain())
# print(hindustani_supporter.email()) #without decorator

hindustani_supporter.fname = "US"

print(hindustani_supporter.email) #with property decorator

hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)
print(hindustani_supporter.email)

del hindustani_supporter.email
print(hindustani_supporter.email)




