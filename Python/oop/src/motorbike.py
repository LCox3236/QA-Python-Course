from vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, make, model, year, helmet_provided, mileage = 0):
        super().__init__(make, model, year, mileage)
        self.__helmet_provided = helmet_provided
    def getRepairCost(self):
        return 100