import mysql.connector

def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="test"
    )
    return mydb

    
