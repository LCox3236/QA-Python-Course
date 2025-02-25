from Python.oop.src.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, doors, mileage = 0):
        super().__init__(make, model, year, mileage)
        self.__doors = doors
    def getRepairCost(self):
        return 200