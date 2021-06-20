from tkinter import *
import tkinter as tk
from PIL import ImageTk
import mysql.connector
import numpy as np
from config.connect import connection
from tkinter import messagebox, filedialog, ttk
from models.loginModel import LoginModel
from views.loginView import LoginView
from controllers.homeController import HomeController


class LoginController:
    def __init__(self):
        self.view = LoginView()
        self.model = LoginModel()
    def run(self):
        self.view.btnLogin.bind("<Button-1>", self.btnClicked)
        self.view.root.mainloop()
    
    def btnClicked(self, event):
        username = self.view.username.get()
        password = self.view.password.get()     
            # messagebox.showerror("Welcome", f"Welcome {self.txt_user}\nYour Password: {self.txt_pass}", parent=self.root)
            # self.root.withdraw()
            # topLevel = Toplevel(self.root)
            # app = Register(topLevel) 
        if username != "":
            if password != "":
                result = self.model.getDataUser(username, password)
                if result:
                    # messagebox.showinfo("Welcome",f"Username: {username}\nPassword:{password}")
                    self.view.root.withdraw()
                    homeController = HomeController()
                    homeController.run()
                else:
                    messagebox.showerror("Lỗi","Tài khoản hoặc mật khẩu không chính xác")
            else:
                print("Vui lòng nhập mật khẩu")
        else:
            messagebox.showerror("Error", "All field are required")
    
        
            
