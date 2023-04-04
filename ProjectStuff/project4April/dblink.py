import mysql.connector

# Creating a DB connection

def dbconnect():

    conn = mysql.connector.connect(
        host = "localhost", 
        user = "root", 
        password = "123456789", 
        database = "students"
    )
    # defining dbCrursor

    dbcursor = conn.cursor()

    return dbcursor, conn

