import mysql.connector

# Creating a DB connection

def db():

    conn = mysql.connector.connect(
        host = "localhost", 
        user = "root", 
        password = "123456789", 
        database = "student"
    )
    # defining dbCrursor

    dbcursor = conn.cursor()

    return dbcursor, conn