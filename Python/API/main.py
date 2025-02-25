from dummyJson import apiOptions
from databaseFunctions import dbTableSelector
import sqlite3
def main():
    print("Hello World!")

    running = True
    while running:
        select = int(input("Select From:\n1. Get new JSON from DummyJson.com\n2. Run Database commands\n3. Exit\n-  "))
        if select == 3:
            running = False
            exit
        else:
            match select:
                case 1:
                    apiOptions()
                case 2:
                    dbTableSelector()


if __name__ == "__main__":
    main()