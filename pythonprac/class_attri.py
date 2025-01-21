# : How to Modify attributes in class

class Car():
    """A simple attempt to create a car"""
    def __init__(self, make, model, year): # __init__ : means it will run qutomatically
        self.make = make
        self.model = model
        self.year = year
        
        #fuel capacity and level in gallons
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """ fill the tank to capacity"""
        # self.fuel_level = self.fuel_capacity
        if self.fuel_level==0:
            print("tank is empty")
        elif self.fuel_level==self.fuel_capacity:
            print("tank is full")
        else:
            fuel = self.fuel_level
            print(f"fuel level is {fuel} gallon.")


    def drive(self):
        """stimulate driving"""
        print("The car is moving")

#let create object of car class
my_car = Car("audi","a4",2020)
#accessing attributes values
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)

#calling methods


#modify the attributes
# my_car.fuel_level=5
# print(my_car.fuel_level)

#writing a method to update an attributes values
# In some programming languages, such as Python, it is possible to add methods to a class from outside the
# class definition. This is known as "monkey patching" or "dynamic class modification.

def update_fuel_level(self,new_level):
    """Update the fuel level """
    if new_level<=self.fuel_capacity:
        self.fuel_level = new_level
    else:
        print("the tank can't hold that much")

#adding above function to original class as method from outside
Car.update_fuel_level = update_fuel_level
my_car.update_fuel_level(12)
print(my_car.fuel_level)


my_car.fill_tank()
my_car.drive()


#writing a method to increment an attributes values

def add_fuel(self,amount):
    """add fuel to the tank"""
    if (self.fuel_level+amount)<=self.fuel_capacity:
        self.fuel_level += amount
        print("added fuel")
    else:
        print("the tank can't hold that much")

Car.add_fuel=add_fuel

print(my_car.add_fuel(1))
