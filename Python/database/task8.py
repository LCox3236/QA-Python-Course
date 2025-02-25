import pyodbc
import sqlite3
#connectionString = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=temp.db;Trusted_connection=yes"

def executeQuery(sql):
    #conn = pyodbc.connect(connectionString)
    conn = sqlite3.connect('test.db')
    cur = conn.cursor() 
    conn.execute(sql)
    conn.commit()
    conn.close()
    
def readData(sql):
    try:
        #conn = pyodbc.connect(connectionString)
        conn = sqlite3.connect('test.db')
        cur = conn.cursor() 
        result = conn.execute(sql).fetchall()
        conn.close()
        return result
    except Exception as ex:
        print("Error Recieved: ", ex)
        return None

qryOne="""
    DROP TABLE IF EXISTS Student
    """
executeQuery(qryOne)
#-------------------------------------------------------------
qryTwo="""
    CREATE TABLE IF NOT EXISTS Student (
    StudentID int NOT NULL,
    FirstName nvarchar(40) NOT NULL,
    Surname nvarchar(30) NULL,
    Course nvarchar(30) NULL,
    City nvarchar(15) NULL)
    """
executeQuery(qryTwo)
#-------------------------------------------------------------
qryThree ="""
    INSERT INTO Student
    (StudentID, Firstname, Surname, Course, City)
    VALUES
    (0,"Lewis","Cox","Cyber Security","Portsmouth")
    """
executeQuery(qryThree)

#--------------------------------------------------------------
qryFour = """
    UPDATE Student
    SET Course="Computer Science"
    WHERE StudentID=0
    """
executeQuery(qryFour)
#--------------------------------------------------------------

    
res = readData("SELECT * FROM Student WHERE StudentID = 0")
if res != None:
    for row in res:
        print(row)