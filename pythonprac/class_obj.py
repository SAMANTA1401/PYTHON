# Define a property that must have the same value for every class instance
# (object)

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass

school_bus = Bus("School Volvo", 12, 50)
print(school_bus.color)   # Output: white
maruti = Car("Maruti 800", 180, 12)
print(maruti.color)      
