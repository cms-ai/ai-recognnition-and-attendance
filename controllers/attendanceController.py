from views.attendanceView import AttendanceView
from models.attendanceModel import AttendanceModel
import numpy as np
import cv2
import mysql.connector
from config.connect import connection
import os
import pickle
class AttendanceController:
    def __init__(self, HomeController):
        self.view = AttendanceView()
        self.model = AttendanceModel()
        self.homeController = HomeController
    def run(self):   
        self.view.btnDiemDannh.bind("<Button-1>", self.attendanceSV)
        self.view.btnBack.bind("<Button-1>", self.returnPage)
        self.view.root.mainloop()
    def attendanceSV(self, event):
        mssvList = []
        mydb = connection()
        my_cursor = mydb.cursor()
        thoigian = self.view.timeNow
        monhoc = self.view.value_inside1.get()
        sql = "SELECT mssv FROM attendance WHERE thoigian=%s AND monhoc=%s"
        val = (thoigian,monhoc)
        my_cursor.execute(sql, val)
        results =  my_cursor.fetchall()
        for x in results:
            mssvList.append(x[0])

        cap = cv2.VideoCapture(0)
        

        face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
        eye_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_eye.xml')
        smile_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_smile.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer.yml")

        labels = {"person_name": 1}
        with open("labels.pickle","rb") as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}

        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for(x, y ,w, h) in faces:
                # print(x, y,w, h)
                roi_gray = gray[y:y+h, x:x+w] #[cord1 - height, cord2-height]
                roi_color = frame[y: y+h, x:x+w]
                # img_item = "images/7.png"

                id_, conf = recognizer.predict(roi_gray)

                if conf >= 45:
                    # print(id_)
                    # print(labels[id_])
                    
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    mssv = labels[id_]
                    
                    self.uploadDBAttandance(mssv, mssvList, thoigian, monhoc)

                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, mssv, (x, y), font, 1, color, stroke, cv2.LINE_AA)

                color = (255, 0, 0) #RGB 0-255
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
                
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        self.showData(thoigian, monhoc)

    def showData(self, thoigian, monhoc):
        mydb = connection()
        my_cursor = mydb.cursor()
        sql = "SELECT * FROM attendance WHERE thoigian= %s AND monhoc = %s"
        val =  (thoigian, monhoc)
        my_cursor.execute(sql, val)
        i = 0
        
        for i in self.view.tree1.get_children():
            self.view.tree1.delete(i)
        for course in my_cursor:
            self.view.tree1.insert("",'end', values=(course[1],course[2],course[3],course[4]))   
    def uploadDBAttandance(self, mssv, mssvList, thoigian, monhoc): 
        newList = []
        mssv = mssv.upper()
        mydb = connection()
        my_cursor = mydb.cursor()
        sql = "SELECT * FROM students WHERE mssv = %s"
        val = (mssv, )
        my_cursor.execute(sql, val)
        results =  my_cursor.fetchall()
        for x in results:
            i = 0
            while i < len(x):
                newList.append(x[i])
                i+=1
        if mssv not in mssvList:
            mssvList.append(mssv)
            sql1 = "INSERT INTO attendance (ten, mssv, lop, khoa, monhoc, thoigian) VALUES (%s, %s, %s, %s,%s,%s)"
            val1 = (newList[1], newList[2], newList[3], newList[4], monhoc, thoigian)

            my_cursor.execute(sql1,val1)
            result = mydb.commit()
            print("Điểm danh")
        else:
            print("Đã điểm danh")     
        
    def returnPage(self, event):
        self.view.root.withdraw()
        homeController = self.homeController()
        homeController.run()
    