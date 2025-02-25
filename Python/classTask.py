# Task:

# Using Vehicle as a base class, create three derived classes (Car, Motorbike, etc.). Each derived class should have its own attributes in addition to the normal Vehicle attributes.
# Using a List<> implementation, store all your Vehicles in a Garage class.
# Create a method in Garage that iterates through each Vehicle, calculating a bill for each type of Vehicle in a different way, depending on the type of Vehicle it is (this does not need to be complex).
# Garage should have methods that add a Vehicle, remove a Vehicle by its ID or its type, fix a Vehicle (which calculates the bill), and to empty the Garage.
# Garage should have a method to remove multiple Vehicles by their type.
import uuid
class Vehicle:
    def __init__(self, make, model, year):
        self.id = str(uuid.uuid4())  # Unique identifier
        self.make = make
        self.model = model
        self.year = year
    def calculate_bill(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    def calculate_bill(self):
        return 200

class Motorbike(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity
    def calculate_bill(self):
        return 100

class Truck(Vehicle):
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year)
        self.load_capacity = load_capacity
    def calculate_bill(self):
        return 500

class Garage:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def remove_vehicle_by_id(self, vehicle_id):
        self.vehicles = [v for v in self.vehicles if v.id != vehicle_id]
    
    def remove_vehicle_by_type(self, vehicle_type):
        self.vehicles = [v for v in self.vehicles if not isinstance(v, vehicle_type)]
    
    def fix_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                bill = vehicle.calculate_bill()
                print(f"Fixed {vehicle.make} {vehicle.model} ({vehicle.year}), Bill: ${bill}")
                return bill
        print("Vehicle not found!")
        return None
    
    def empty_garage(self):
        self.vehicles.clear()
    
    def remove_vehicles_by_type(self, vehicle_type):
        self.remove_vehicle_by_type(vehicle_type)
    
    def calculate_all_bills(self):
        total = 0
        for vehicle in self.vehicles:
            bill = vehicle.calculate_bill()
            print(f"{vehicle.make} {vehicle.model} ({vehicle.year}): ${bill}")
            total += bill
        print(f"Total bill for all vehicles: ${total}")

# Example Usage
garage = Garage()
car = Car("Toyota", "Corolla", 2020, 4)
bike = Motorbike("Yamaha", "R3", 2021, 300)
truck = Truck("Ford", "F-150", 2019, 1000)

garage.add_vehicle(car)
garage.add_vehicle(bike)
garage.add_vehicle(truck)

garage.calculate_all_bills()
garage.fix_vehicle(car.id)
garage.remove_vehicle_by_id(bike.id)
garage.empty_garage()




# class A:
#     def greeting(self):
#         print("Hi from A")


# class B(A):
#     def greeting(self):
#         super().greeting()
#         print("Hi from B")


# class C(B):
#     def greeting(self):
#         super().greeting()
#         print("Hi from C")


# class D(C, B):
#     def greeting(self):
#         super().greeting()
#         print("Hi from D")


# d = D()
# d.greeting()
# print(D.mro())

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")

#     def move(self):
#         print(f"{self.name} is moving.")

#     def sleep(self):
#         print(f"{self.name} is sleeping.")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, "Dog")
#         self.breed = breed

#     def speak(self):
#         print(f"{self.name} says Woof!")

#     def fetch(self):
#         print(f"{self.name} is fetching the ball.")