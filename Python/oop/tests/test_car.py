import pytest
from Python.oop.src.car import Car

def test_car():
    testCar = Car("Toyota", "Corolla", 2020, 4, 15000)
    assert testCar.getRepairCost() == 200



