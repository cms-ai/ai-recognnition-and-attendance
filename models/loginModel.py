from config.connect import connection
import mysql.connector

class LoginModel:
    def getDataUser(self, username, password):
        sql = "SELECT * FROM users WHERE username = %s and password = %s"
        val = (username, password)
        mydb = connection()
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        result = mycursor.fetchall()
        return result
