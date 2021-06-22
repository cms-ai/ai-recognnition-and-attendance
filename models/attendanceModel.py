
import mysql.connector
from config.connect import connection

class AttendanceModel:
    def getKhoa(self):
        khoaList = []
        mydb = connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT name from courses")
        results = my_cursor.fetchall()
        for x in results:
            khoaList.append(x[0])

        return khoaList
    # def getStudent(self, mssv, thoigian, monhoc):
        