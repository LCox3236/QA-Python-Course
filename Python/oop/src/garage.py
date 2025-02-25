class Garage:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def removeVehicleByID(self, v_id):
        self.vehicles = [x for x in self.vehicles if x.id != v_id]
    def removeVehicleByType(self, type):
        self.vehicles = [x for x in self.vehicles if not isinstance(x, type)]    
    
    def fixVehicle(self, v_id):
        for v in self.vehicles:
            if v.id == v_id:
                cost = v.getRepairCost()
                print(f"Repaied Vehicle {v.getMake()} {v.getModel()} for £{cost}")
                return
        print(f"Vehicle with ID: {v_id} Not found.")  
          
    def getAllBills(self):
        total = 0
        for v in self.vehicles:
            cost = v.getRepairCost()
            print(f"Repaied Vehicle {v.getMake()} {v.getModel()} for £{cost}")
            total += cost
        print(f"Total bill for all vehicles: ${total}")
                  
    def getAllMileage(self):
        for v in self.vehicles:
            print(f"{v.getMake()} {v.getModel()} has {v.getMileage()} miles on the clock")
    
    def emptyGarage(self):
        self.vehicles.clear()
        
    def displayDrivingHistory(self, v_id):
        for v in self.vehicles:
            if v_id == v.id:
                print(f"Driving History for: {v.getMake()} {v.getModel()}")
                for record in v.getDrivingHistory():
                    print(f"{record['timestamp']}: {record['driver']} drove {record['miles']} miles")
                return
        print("Vehicle not found!")
