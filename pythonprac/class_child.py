# Create a child class Bus that will inherit all of the variables and methods of the
# Vehicle class

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)
print(school_bus.name, school_bus.max_speed, school_bus.mileage)