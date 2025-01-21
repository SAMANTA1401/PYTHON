class Vehicle:
    def __init__ (self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

maruti=Vehicle(240,18)
print(maruti.max_speed, maruti.mileage)