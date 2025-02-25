
class Driver:
    def __init__(self, name):
        self._name = name
        
    def getName(self):
        return self._name
    
    def drive(self, vehicle, miles):
        vehicle.recordTrip(self._name, miles)
        print(f"{self._name} drove the {vehicle.getMake()} {vehicle.getModel()} for {miles} miles. Total mileage: {vehicle.getMileage()}")
            