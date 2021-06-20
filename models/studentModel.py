from config.connect import connection
import mysql.connector

class StudentModel:
    def setStudent(self, ten, mssv, lop, khoa):
        try:
            mydb = connection()
            mycursor = mydb.cursor()

            sql = "INSERT INTO students (ten, mssv, lop, khoa) VALUES (%s, %s, %s, %s)"
            val = (ten, mssv, lop, khoa)
            mycursor.execute(sql, val)
            result = mydb.commit()
            return 1
        except mysql.connector.Error as error:
            return error


