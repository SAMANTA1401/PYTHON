import json
from json import JSONEncoder



class vehicle:
    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price

class vehicleEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__
    


vehicle = vehicle("tata","2.5L",3430000)

#object to json
vehicleJson =json.dumps(vehicle,indent=4,cls=vehicleEncoder)
print(vehicleJson)