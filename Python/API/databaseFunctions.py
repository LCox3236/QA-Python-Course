import sqlite3

def readData(sql):
    try:
        conn = sqlite3.connect('Python\\API\\database\\ApiTaskDB.db')
        result = conn.execute(sql).fetchall()
        conn.close()
        return result
    except Exception as e:
        print(f"exception: {str(e)}")
        return None

def upsertQuotesToDB(data):
    try:
        if isinstance(data, list):
            for quote in data:            
                query =f"""
                    INSERT OR IGNORE INTO quotes
                    (quote_id, quote_text, author)
                    VALUES
                    ({quote["id"]},"{quote["quote"]}","{quote["author"]}")
                    """        
                conn = sqlite3.connect('Python\\API\\database\\ApiTaskDB.db')
                conn.execute(query)
                conn.commit()
                conn.close()
        
        else:
            query =f"""
                INSERT OR IGNORE INTO quotes
                (quote_id, quote_text, author)
                VALUES
                ({data["id"]},"{data["quote"]}","{data["author"]}")
                """        
            conn = sqlite3.connect('Python\\API\\database\\ApiTaskDB.db')
            conn.execute(query)
            conn.commit()
            conn.close()
    except Exception as e:
        print(f"exception: {str(e)}")
    
    
def getTopFiveFromTable(table):
    res = readData(f"SELECT * FROM {table} LIMIT 5")
    if res != None:
        for row in res:
            print(f"ID: {row[0]}\n'{row[1]}'\n- {row[2]}\n")
            
def getQuotesByAuthor():
    name = str(input("Enter Author to search database for: "))
    res = readData(f"SELECT * FROM quotes WHERE author = '{name}'")
    if res != None:
        for row in res:
            print(f"ID: {row[0]}\n'{row[1]}'\n- {row[2]}\n")
            
def removeQuoteFromQuotesByID():
    try:
        id = int(input("Enter ID to delete\n: "))
        query = f"DELETE FROM quotes WHERE quote_id={id}"
        conn = sqlite3.connect('Python\\API\\database\\ApiTaskDB.db')
        conn.execute(query)
        conn.commit()
        conn.close()
        print("Row Deleted Successfully")
    except Exception as e:
        print(f"exception: {str(e)}")
    
    
def updateRowInTable(table):
    try:
        test = input(f"Updating ,Enter the ID, Column Name and New Value to update to\nin format ID:Col:Value;\n-- ")
        id, col, value = test.split(":")
        query = f"UPDATE {table} SET {col} = '{value}' WHERE id = {id}"
        conn = sqlite3.connect('Python\\API\\database\\ApiTaskDB.db')
        conn.execute(query)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"exception: {str(e)}")
    
    
    
def dbQutotesFunctions(table):
    select = int(input("Select:\n1: Get Top 5 from Table\n2: Get Quotes By Author\n3. Update Row\n4. Remove Row from Table by ID\n-- "))
    match select:
        case 1:
            getTopFiveFromTable(table)
        case 2:
            getQuotesByAuthor()
        case 3:
            updateRowInTable(table)
        case 4:
            removeQuoteFromQuotesByID()

def dbTableSelector():
    select = int(input("Select Which Table to Interact With;\n1. Quotes\n-- "))
    match select:
        case 1:
            dbQutotesFunctions("quotes")
