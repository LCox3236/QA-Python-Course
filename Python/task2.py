import math
def ageCheck():
    age = int(input("Enter Age: "))
    if age >= 18:
        print(f"You are in catagory A")
    elif age >16:
        print(f"You are in catagory B")
    else:
        print(f"You are in catagory C")


def calc():
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    symbol = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\nEnter Number matching operation you want: "))
    if symbol == 1:
        print(f"Addition: {num1+num2}")
    elif symbol == 2:
        print(f"Subtraction: {num1-num2}")
    elif symbol == 3:
        print(f"Multiplication: {num1*num2}")
    elif symbol == 4:
        print(f"Division: {num1/num2}")
    elif symbol == 5:
        print(f"Power: {num1**num2}")

def grade():
    score = int(input("Enter Score: "))
    if score >= 100 or score <= 1:
        print("Error: Score not within range")
    elif score > 70:
        print("Distinction")
    elif score > 60:
        print("Merit")
    elif score > 49:
        print("Pass")
    else:
        print("Fail")

def grade2():
    score = int(input("Enter Score: "))
    if score >= 100 or score <= 1:
        print("Error: Score not within range")
    level = int(input("Enter Level 1 or 2:"))
    if level > 2 or level < 1:
        print("Error: Level not within range")
    if level == 1:
        if score > 60:
            print("Distinction")
        elif score > 50:
            print("Merit")
        elif score > 39:
            print("Pass")
        else:
            print("Fail")
    
    elif level == 2:
        if score > 60:
            print("Distinction")
        elif score > 50:
            print("Merit")
        elif score > 39:
            print("Pass")
        else:
            print("Fail")

    
def pythag():
    type = int(input("1. Find the length of A given B and C\n2. Find the length of B given A and C\n3. Find the length of C given A and B\nEnter Number matching operation you want: "))
    match type:
        case 1:
            B = int(input("Enter Side B:"))
            C = int(input("Enter Side C:"))
            print(f"A = {round(math.sqrt((C**2)-(B**2)),2)}")
        case 2:
            A = int(input("Enter Side A:"))
            C = int(input("Enter Side C:"))
            print(f"B = {round(math.sqrt((C**2)-(A**2)),2)}")
        case 3:
            A = int(input("Enter Side A:"))
            B = int(input("Enter Side B:"))
            print(f"C = {round(math.sqrt((A**2)+(B**2)),2)}")
