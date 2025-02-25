# Part 1: Using Functions
# Objective:
# Create a modular calculator that can perform basic arithmetic operations. Write a separate function for each operation: addition, subtraction, multiplication, and division.
# 
# Instructions:
# 
# Write functions for the following operations:
# addition(num1, num2)
# subtraction(num1, num2)
# multiplication(num1, num2)
# division(num1, num2) (ensure you handle division by zero)
# Create a main calculator() function that:
# Prompts the user to select an operation (choose from +, -, *, /).
# Prompts the user to input two numbers.
# Calls the corresponding function to perform the operation.
# Prints the result.
from time import sleep


addition = lambda a, b: a + b
subtraction = lambda a, b: a - b
multiplication = lambda a, b: a * b
division = lambda a, b: a / b

#filtered_list = list(filter(lambda i: (i % 2 == 1), my_list))

# Defining main function
def main():
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
                    print(f"Result of {num1} + {num2} = {addition(num1,num2)}")
                case 2:
                    print(f"Result of {num1} - {num2} = {subtraction(num1,num2)}")
                case 3:
                    print(f"Result of {num1} * {num2} = {multiplication(num1,num2)}")
                case 4:
                    print(f"Result of {num1} / {num2} = {division(num1,num2)}")
            print("-------------------------------------------------")
            sleep(2)
                    
                

# Using the special variable 
# __name__
if __name__=="__main__":
    main()

