import uuid
from datetime import datetime

class Vehicle:
    def __init__(self, make:str, model:str, year, mileage = 0):
        self.id = str(uuid.uuid4())
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._driving_history = []
    
    def getMake(self):
        return self._make
    
    def getModel(self):
        return self._model
    
    def addMiles(self, miles):
        self._mileage += miles
        
    def getMileage(self):
        return self._mileage
    
    def recordTrip(self, driver_name, miles):
        self._mileage += miles
        self._driving_history.append({
            "driver": driver_name,
            "miles": miles,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
    def getDrivingHistory(self):
        return self._driving_history