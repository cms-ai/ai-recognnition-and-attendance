from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import ImageTk
# import mysql.connector
from datetime import datetime
from models.attendanceModel import AttendanceModel
# from config.connect import connection

class AttendanceView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.model = AttendanceModel()
        self.root.title("Trang điểm danh-Author Trần Công Ái")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False, False)

        left_Frame = tk.Frame(self.root, bg="white")
        left_Frame.place(x=0,y=0,width=350, height=600)

        lbl_1 = tk.Label(left_Frame, text="Điểm danh",fg="red", bg="white", font=("times new roman",28,"bold"))
        lbl_1.place(x=0, y=30, relwidth=1)

        lbl_2 = tk.Label(left_Frame, text="Tên môn học", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_2.place(x=80, y=100)
        
        khoaList =  []
        results = self.model.getKhoa()
        for x in results:
            khoaList.append(x)
        
        self.value_inside1 = StringVar()
        self.value_inside1.set(khoaList[0])
        self.dayMenu =  tk.OptionMenu(left_Frame, self.value_inside1, *khoaList)
        self.dayMenu.config(font=("times new roman",12), bg="#e0dede")
        self.dayMenu.place(x=80,y=130, width=200, height=40)

        # lbl_3 = Label(left_Frame, text="MSSV", bg="white",fg="gray", font=("times new roman",12,"bold"))
        # lbl_3.place(x=280, y=100)
        
        x = datetime.now()
        day = x.strftime("%d")
        month = x.strftime("%m")
        year = x.strftime("%Y")
        self.timeNow = "{}/{}/{}".format(day, month, year)

        lbl_3 = tk.Label(left_Frame, text="Thời gian", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_3.place(x=80, y=200)

        lbl_3 = tk.Label(left_Frame, text=self.timeNow, bg="lightgray",fg="black", font=("times new roman",12,"bold"))
        lbl_3.place(x=80, y=230, height=40, width=200)

        self.btnDiemDannh = tk.Button(left_Frame, text="Điểm danh", font=("times new roman",12))
        self.btnDiemDannh.place(x=80,y=300, width=200, height=40)

        self.btnBack = tk.Button(left_Frame, text="Thoát", font=("times new roman",12))
        self.btnBack.place(x=80,y=350, width=200, height=40)

        right_Frame = Frame(self.root, bg="lightgray")
        right_Frame.place(x=351,y=0,width=670 ,height=600)

        tableFrame = Frame(right_Frame, bg="white")
        tableFrame.place(x=0, y=0, width=670, height=600)

        
        self.tree1 = ttk.Treeview(tableFrame, selectmode='browse')
        self.tree1.place(x=20, y=30, height=500)

        vsb =  Scrollbar(tableFrame, orient="vertical", command=self.tree1.yview)
        vsb.place(x=30+600+2, y=30, height=500)

        self.tree1.configure(yscrollcommand=vsb.set)

        self.tree1["columns"] = ("1", "2", "3", "4")
        self.tree1['show'] = 'headings'
        self.tree1.column("1", width=200, anchor='c')
        self.tree1.column("2", width=100, anchor='c')
        self.tree1.column("3", width=100, anchor='c')
        self.tree1.column("4", width=200, anchor='c')
        self.tree1.heading("1", text="Tên")
        self.tree1.heading("2", text="MSSV")
        self.tree1.heading("3", text="Lớp")
        self.tree1.heading("4", text="Khoa")