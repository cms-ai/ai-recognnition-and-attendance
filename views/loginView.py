from tkinter import *
import tkinter as tk
from PIL import ImageTk
class LoginView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login View") 
        self.root.geometry("1000x600+100+50")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="images/login1.jpg")
        print(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frameLogin = tk.Frame(self.root, bg="white")
        frameLogin.place(x=150, y=150, height=340, width=500)

        titleLabel = tk.Label(frameLogin, text="Login Here",font=("Impact",32,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        self.username = StringVar()
        self.password = StringVar()
        lbl_user = tk.Label(frameLogin, text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=100)
        self.txt_user = Entry(frameLogin, textvariable=self.username, font=("times new roman",15), bg="lightgray")
        self.txt_user.place(x=90, y= 140, width=350, height=35)

        lbl_pass = tk.Label(frameLogin, text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=180)
        self.txt_pass = tk.Entry(frameLogin, textvariable=self.password, font=("times new roman",15), bg="lightgray")
        self.txt_pass.place(x=90, y= 210, width=350, height=35)

        self.forget = tk.Button(frameLogin, text="Create a new account?", bg="white",bd=0, fg="#d77337", font=("times new roman", 12)).place(x=90, y=250)
        self.btnLogin = tk.Button(self.root, text="Login", fg="white", bg="#d77337", font=("times new roman", 18,"bold"))
        self.btnLogin.place(x=300, y=440, width=180, height=40)

        
