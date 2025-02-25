import sys
from time import sleep

class Calculator:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mult(self, x, y):
        return x * y
    def div(self, x, y):
        if y != 0:
            return x + y
        else:
            return ("Error: Cannot divide by 0")

class Student:
# instance attributes
    def __init__(self, name:str, age:int, subject:str):
        self.__name:str = name
        self.__age = age
        self.__subject = subject
        
    def calcAverage(self, score1:int, score2:int, score3:int):
        return ((score1+score2+score3)/3)

class Bird:
    def __init__(self, name, can_fly):#
        self.name = name
        self.can_fly = can_fly
    def describe(self):
        ability = "can fly" if self.can_fly else "cannot fly"
        return f"{self.name} is a bird that {ability}."

# child class
class Owl(Bird):
    def __init__(self, name):
        super().__init__(name, can_fly=True)
    def hoot(self):
        return f"{self.name} Says Hoot Hoot!"
         
class Dodo(Bird):
    def __init__(self, name):
        super().__init__(name, can_fly=False)

    def extinct_message(self):
        return f"Sadly, {self.name} is extinct."








def main():
    # stu2 = Student("twodent", 55)
    # print(stu.name)
    # stu2.name="tester"
    # print(stu2.name)

    stu = Student("student one",25,"Science")
    print(stu.calcAverage(1,2,3))
    
    owl = Owl("Snowy Owl")
    dodo = Dodo("Mauritius Dodo")

    print(owl.describe())  # Snowy Owl is a bird that can fly.
    print(owl.hoot())      # Snowy Owl says: Hoot hoot!

    print(dodo.describe()) # Mauritius Dodo is a bird that cannot fly.
    print(dodo.extinct_message()) # Sadly, Mauritius Dodo is extinct.
    
    ##callCalc()
    
    
    
    
    
    
    
    
    
def callCalc():
    c = Calculator()
    running = True
    while running:
        select = int(input("Select From:\n1. Addition\n2. subtraction\n3. multiplication\n4. division\n5. Exit\n-  "))
        if select == 5:
            running = False
            exit
        else:
            num1 = int(input("Enter First Number: "))
            num2 = int(input("Enter Second Number: "))
            match select:
                case 1:
                    print(f"Result of {num1} + {num2} = {c.add(num1,num2)}")
                case 2:
                    print(f"Result of {num1} - {num2} = {c.sub(num1,num2)}")
                case 3:
                    print(f"Result of {num1} * {num2} = {c.mult(num1,num2)}")
                case 4:
                    print(f"Result of {num1} / {num2} = {c.div(num1,num2)}")
            print("-------------------------------------------------")
            sleep(2)






if __name__ == "__main__":
    sys.exit(int(main() or 0))