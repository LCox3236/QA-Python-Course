from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, make, model, year, capacity, mileage = 0):
        super().__init__(make, model, year, mileage)
        self.capacity = capacity
    def getRepairCost(self):
        return 500