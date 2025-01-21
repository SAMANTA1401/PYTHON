# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
# a default value of 50.

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def sitting_capacity(self,capacity):
        return f"sitting capacity of bus {self.name} is {capacity}"

class Bus(Vehicle):
    #assign default value to capacity argument
    def sitting_capacity(self,capacity=50):
        return super().sitting_capacity(capacity=50)
    

school_bus = Bus("School Volvo", 180, 12)
print(school_bus.sitting_capacity())