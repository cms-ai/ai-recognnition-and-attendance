from tkinter import *
import tkinter as tk
from PIL import ImageTk
class HomeView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Trang chủ-Author Trần Công Ái")
        self.root.geometry("1000x600+100+50")
        self.root.resizable(False, False)
        # BG Images
        frame_home = tk.Frame(self.root,bg="white")
        frame_home.place(x=0,y=0, width=1000, height=600)

        self.lbl_ad = tk.Label(frame_home, text="Admin", fg="black", bg ="white",font=("Goudy old style",12,"bold")).place(x=0, y=0)
        self.logout = tk.Button(frame_home, text="Đăng xuất", bg="white", bd=0)
        self.logout.place(x=80, y=5)

        self.add_St1 = tk.Button(frame_home, text="Thêm sinh viên", font=("times new roman",18,"bold"))
        self.add_St1.place(x=100, y=400,width=170, height=80)

        self.add_St2 = tk.Button(frame_home, text="Điểm danh", font=("times new roman",18,"bold"))
        self.add_St2.place(x=300, y=400,width=170, height=80)

        self.add_St3 = tk.Button(frame_home, text="Quản lý", font=("times new roman",18,"bold"))
        self.add_St3.place(x=500, y=400,width=170, height=80)

        self.add_St4 = tk.Button(frame_home, text="Thoát", font=("times new roman",18,"bold"))
        self.add_St4.place(x=700, y=400,width=170, height=80)
        self.bg1 = ImageTk.PhotoImage(file="images/vku.png")
        self.bg_image1 = tk.Label(frame_home, image=self.bg1, bg="white").place(x=0, y=100, relwidth=1)