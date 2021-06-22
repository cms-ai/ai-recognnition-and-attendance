from tkinter import *
import tkinter
from PIL import ImageTk
from config.connect import connection
from datetime import datetime

class CourseView:
    def __init__(self, CourseController):
        self.controller = CourseController
        self.root = Toplevel()
        self.root.title("Quản lý-Author Trần Công Ái")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False, False)

            
        left_Frame = Frame(self.root, bg="white")
        left_Frame.place(x=0,y=0,width=600, height=600)


        lbl_1 = Label(left_Frame, text="Quản lý môn học",fg="red", bg="white", font=("times new roman",28,"bold"))
        lbl_1.place(x=0, y=30, relwidth=1)

        tableFrame = Frame(left_Frame, bg="white")
        tableFrame.place(x=0, y=100, width=600, height=600)

        
        self.tree = ttk.Treeview(tableFrame, selectmode='browse')
        self.tree.place(x=20, y=10, height=400)

        vsb =  Scrollbar(tableFrame, orient="vertical", command=self.tree.yview)
        vsb.place(x=30+500+2, y=10, height=400)

        self.tree.configure(yscrollcommand=vsb.set)

        self.tree["columns"] = ("1", "2", "3", "4")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=100, anchor='c')
        self.tree.column("2", width=200, anchor='c')
        self.tree.column("3", width=100, anchor='c')
        self.tree.column("4", width=100, anchor='c')
        self.tree.heading("1", text="Id")
        self.tree.heading("2", text="Name")
        self.tree.heading("3", text="Start At")
        self.tree.heading("4", text="Day Learn")

        self.showData()
        # mydb = connection()
        # my_cursor = mydb.cursor()
        # my_cursor.execute("SELECT * FROM courses limit 0,10")
        # i = 0
        # for course in my_cursor:
        #     self.tree.insert("",'end', values=(course[0],course[1],course[2],course[3]))


        right_frame = Frame(self.root,bg="lightgray")
        right_frame.place(x=600, y=0, width=400, height=600)

        lblAddCourse = Label(right_frame, text="Thêm môn học",fg="red", bg="lightgray", font=("times new roman",20,"bold"))
        lblAddCourse.place(x=0, y=30, relwidth=1)

        lbl_2 = Label(right_frame, text="Tên môn học", bg="lightgray",fg="gray", font=("times new roman",12,"bold"))
        lbl_2.place(x=70, y=150)

        self.nameCourse = Entry(right_frame, bg="white", bd=1, font=("times new roman",12))
        self.nameCourse.place(x=70,y=180, height=30, width=200)

        lbl_3 = Label(right_frame, text="Thời gian bắt đầu", bg="lightgray",fg="gray", font=("times new roman",12,"bold"))
        lbl_3.place(x=70, y=230)

        x = datetime.now()
        day = x.strftime("%d")
        month = x.strftime("%m")
        year = x.strftime("%Y")
        timeNow = "{}/{}/{}".format(day, month, year)

        self.startAtCourse = Label(right_frame,text=timeNow, bg="white", font=("times new roman",12))
        self.startAtCourse.place(x=70,y=260, height=30, width=200)


        lbl_4 = Label(right_frame, text="Ngày học", bg="lightgray",fg="gray", font=("times new roman",12,"bold"))
        lbl_4.place(x=70, y=300)

        # self.endCourse = Entry(right_frame, bg="white", bd=1, font=("times new roman",12))
        # self.endCourse.place(x=0,y=330, height=30, width=200, relx=0.5, anchor=CENTER)

        khoaList = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.value_inside1 = StringVar()
        self.value_inside1.set("Chọn ngày học")
        self.dayMenu =  OptionMenu(right_frame, self.value_inside1, *khoaList)
        self.dayMenu.config(font=("times new roman",12), bg="#e0dede", bd=0)
        self.dayMenu.place(x=70, y=330, width=200)
       
        self.btnAddCourse = Button(right_frame, text="Thêm", font=("times new roman",12))
        self.btnAddCourse.place(x=70,y=400, width=200)

        self.btnReturn = Button(right_frame, text="Quay lại", font=("times new roman",12))
        self.btnReturn.place(x=70,y=450, width=200)
    def showData(self):
        mydb = connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM courses limit 0,10")
        i = 0
        
        for i in self.tree.get_children():
            self.tree.delete(i)
        for course in my_cursor:
            self.tree.insert("",'end', values=(course[0],course[1],course[2],course[3]))
