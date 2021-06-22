from views.courseView import CourseView
from config.connect import connection
from tkinter import messagebox, filedialog, ttk
import cv2
import mysql.connector
import numpy as np
from PIL import Image
import pickle
import time
import os


class CourseController:
    def __init__(self, HomeController):
        self.view = CourseView(CourseController)
        self.homeController = HomeController
    def run(self):
        self.view.btnAddCourse.bind("<Button-1>", self.addCourse)
        self.view.btnReturn.bind("<Button-1>", self.returnPage)

        self.view.root.mainloop()
    def returnPage(self, event):
        self.view.root.withdraw()
        homeController = self.homeController()
        homeController.run()
    
    def showData(self):
        mydb = connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM courses limit 0,10")
        i = 0
        
        for i in self.view.tree.get_children():
            self.view.tree.delete(i)
        for course in my_cursor:
            self.view.tree.insert("",'end', values=(course[0],course[1],course[2],course[3]))

    def addCourse(self, event):
        nameCourse = self.view.nameCourse.get()
        startAt = self.view.startAtCourse['text']
        dayLearn = self.view.value_inside1.get()
        # print(nameCourse,startAt, dayLearn)

        if nameCourse.strip() == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập tên khóa học")
        elif dayLearn == "Chọn ngày học":
            messagebox.showerror("Thông báo", "Vui lòng chọn ngày học")
        else:
            try:
                mydb = connection()
                mycursor = mydb.cursor()

                sql = "INSERT INTO courses (name, startAt, dayLearn) VALUES (%s, %s, %s)"
                val = (nameCourse, startAt, dayLearn)

                mycursor.execute(sql, val)

                result = mydb.commit()

                messagebox.showinfo("Thành công", "Thêm sinh viên thành công")   

                self.showData()
            except mysql.connector.Error as error:
                messagebox.showerror("Thất lại", "Không thể thêm dữ liệu vào DB")  
                print(error) 
    
    
    
