from Python.oop.src.car import Car
from garage import Garage
from truck import Truck
from motorbike import Motorbike
from driver import Driver

# Example Usage
garage = Garage()
car = Car("Toyota", "Corolla", 2020, 4, 15000)
bike = Motorbike("Yamaha", "R3", 2021, 300, 5000)
truck = Truck("Ford", "F-150", 2019, 1000, 30000)

garage.addVehicle(car)
garage.addVehicle(bike)
garage.addVehicle(truck)

driver = Driver("John")
driver.drive(car, 100)
driver.drive(bike, 50)

garage.getAllBills()
garage.getAllMileage()
garage.fixVehicle(car.id)
garage.displayDrivingHistory(car.id)
garage.removeVehicleByID(bike.id)
garage.emptyGarage()