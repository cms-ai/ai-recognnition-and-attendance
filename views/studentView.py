from tkinter import *
import tkinter as tk
from PIL import ImageTk

class StudentView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Thêm sinh viên-Author Trần Công Ái")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False, False)

        left_Frame = tk.Frame(self.root, bg="white")
        left_Frame.place(x=0,y=0,width=500, height=600)


        lbl_1 = tk.Label(left_Frame, text="Thêm sinh viên",fg="red", bg="white", font=("times new roman",28,"bold"))
        lbl_1.place(x=0, y=30, relwidth=1)

        lbl_2 = tk.Label(left_Frame, text="Họ và tên", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_2.place(x=50, y=150)

        self.nameEntry = tk.Entry(left_Frame,bg="#e0dede", bd=1, font=("times new roman",12))
        self.nameEntry.place(x=50, y=180, height=30, width=180)

        lbl_3 = tk.Label(left_Frame, text="MSSV", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_3.place(x=250, y=150)

        self.MSVEntry = tk.Entry(left_Frame,bg="#e0dede",  font=("times new roman",12))
        self.MSVEntry.place(x=250, y=180, height=30, width=180)

        lbl_4 = tk.Label(left_Frame, text="Lớp", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_4.place(x=50, y=230)

        self.gradeEntry = tk.Entry(left_Frame,bg="#e0dede",  font=("times new roman",12))
        self.gradeEntry.place(x=50, y=260, height=30, width=180)

        lbl_5 = tk.Label(left_Frame, text="Khoa", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_5.place(x=250, y=230)
        khoaList = ["Khoa khoa học máy tính","Quản trị kinh doanh", "Công nghệ kỹ thuật máy tính"]
        self.value_inside = StringVar()
        self.value_inside.set("Chọn ngành học")
        self.khoaMenu =  tk.OptionMenu(left_Frame, self.value_inside, *khoaList)
        self.khoaMenu.config(font=("times new roman",12), bg="#e0dede", bd=0)
        self.khoaMenu.place(x=250, y=260, width=180)
        
        self.btnAddPhoto = tk.Button(left_Frame, text="Thêm hình ảnh", padx=30, pady=10) 
        self.btnAddPhoto.place(x=150, y= 350)

        # self.valueImage = StringVar()

        # self.txtImg = tk.Label(left_Frame,textvariable=self.valueImage)
        # self.txtImg.place(x=150, y=400)
        
        self.btnSubmit = tk.Button(left_Frame, text="Lưu vào CSDL", font=("times new roman",13,"bold"))
        self.btnSubmit.place(x=80, y=450, height=50, width=300)

        self.btnReturn = Button(self.root, text="Quay lại", font=("times new roman",12))
        self.btnReturn.place(x=140, y=530, height=30, width=200)

        #Right Frame
        right_frame = tk.Frame(self.root,bg="lightgray")
        right_frame.place(x=500, y=0, width=500, height=600)

        self.bg1 = ImageTk.PhotoImage(file="images/vku.png")
        self.bg_image1 = tk.Label(right_frame, image=self.bg1, bg="white").place(x=1, y=0, height=600, width=500)

