class Animal_Dog:
    def execute(self):
        print("bow bow")    

class Bird_Duck:
    def execute(self):
        print("Quak quak")

class Animal:
    def code(self,ide):
        ide.execute()       

# ide =Bird_Duck()
ide =Animal_Dog()

obj=Animal()
obj.code(ide)