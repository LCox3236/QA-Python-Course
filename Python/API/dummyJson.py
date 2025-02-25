import requests
from databaseFunctions import *

quoteURL = "https://dummyjson.com/quotes/random"
recipeURL = 'https://dummyjson.com/recipes'


def apiOptions():
    select = int(input("Select which API to interact with:\n1: Quotes\n2: Recipies\n-- "))
    match select:
        case 1:
            apiQuoteOptions()
        case 2:
            apiRecipeOptions()

def apiRecipeOptions():
    select = int(input("Select:\n1: One Random Recipie\n2: Search Recipe\n-- "))
    match select:
        case 1:
            response = requests.get(f"{recipeURL}/meal-type/snack")
            data = response.json()
            print(data)

def apiQuoteOptions():
    select = int(input("Select:\n1: Get One Quote\n2: Get Multiple Quotes\n-- "))
    match select:
        case 1:
            response = requests.get(quoteURL)
            processResponse(response)
        case 2:
            tries = 0
            while tries < 3:
                quantity = int(input("How many Quotes? (Between 1 and 10) : "))
                if quantity < 1 or quantity > 10:
                    tries += 1
                    print("Plese make sure the nuber is between 1 and 10\n\n")
                else:
                    response = requests.get(f"{quoteURL}/{quantity}")
                    processResponse(response)
                    break
            else:
                ("Too many tries.")
        case 3:
            response = requests.get(quoteURL)
            processResponse(response)           

def processResponse(response):
    if response.status_code == 200:
        data = response.json()
    elif response.status_code == 400:
        print(f"Bad request, check your request syntax")
    elif response.status_code == 500:
        print(f"Server error, chill out it's not your fault, you tired.")
    else:
        print(f"Another error {response.status_code}")

    select = int(input("Would you like to:\n1. View the quotes\n2. Save the quotes to the databse\n3. View quotes and save to databse\n: "))
    match select:
        case 1: 
            for quote in data:
                print(f"{quote["id"]} {quote["quote"]}\n{quote["author"]}\n")
            
        case 2:
            try:
                upsertQuotesToDB(data)
            except Exception as e:
                print(f"exception: {str(e)}")
                