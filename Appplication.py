from tkinter import*
from PIL import ImageTk
from tkinter import messagebox, filedialog, ttk
import pandas as pd
import mysql.connector
import numpy as np
from config.connect import connection
import os
import cv2
import face_recognition
from datetime import datetime
import shutil

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        # BG Images
        self.bg = ImageTk.PhotoImage(file="images/login1.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame

        Frame_Login = Frame(self.root, bg="white")
        Frame_Login.place(x=150, y=150, height=340, width=500)

        titleLabel = Label(Frame_Login, text="Login Here",font=("Impact",32,"bold"),fg="#d77337",bg="white").place(x=90,y=30)

        lbl_user = Label(Frame_Login, text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=100)
        self.txt_user = Entry(Frame_Login, font=("times new roman",15), bg="lightgray")
        self.txt_user.place(x=90, y= 140, width=350, height=35)

        lbl_pass = Label(Frame_Login, text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=180)
        self.txt_pass = Entry(Frame_Login, font=("times new roman",15), bg="lightgray")
        self.txt_pass.place(x=90, y= 210, width=350, height=35)

        forget = Button(Frame_Login, text="Forget Password?", bg="white",bd=0, fg="#d77337", font=("times new roman", 12)).place(x=90, y=250)
        Login_btn = Button(self.root, command=self.login_vertify, text="Login", fg="white", bg="#d77337", font=("times new roman", 18,"bold")).place(x=300, y=440, width=180, height=40)

    
    def login_vertify(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        sql = "SELECT * FROM users WHERE username = %s and password = %s"
        val = (username, password)

        mydb = connection()
        mycursor = mydb.cursor()
            # messagebox.showerror("Welcome", f"Welcome {self.txt_user}\nYour Password: {self.txt_pass}", parent=self.root)
            # self.root.withdraw()
            # topLevel = Toplevel(self.root)
            # app = Register(topLevel)
        
        if username != "":
            if password != "":
                mycursor.execute(sql,val)
            else:
                print("Vui lòng nhập mật khẩu")
        else:
            messagebox.showerror("Error", "All field are required")
    
        result = mycursor.fetchall()
        if result:
            # messagebox.showinfo("Welcome",f"Username: {username}\nPassword:{password}")
            self.root.withdraw()
            topLevel = Toplevel(self.root)
            app = Home(topLevel)
        else:
            print("Đăng nhập thất bại") 
            
class Home:
    def __init__(self,root):
        self.root = root
        self.root.title("Trang chủ-Author Trần Công Ái")
        self.root.geometry("1000x600+100+50")
        self.root.resizable(False, False)
        # BG Images
        frame_home = Frame(self.root,bg="white")
        frame_home.place(x=0,y=0, width=1000, height=600)

        self.lbl_ad = Label(frame_home, text="Admin", fg="black", bg ="white",font=("Goudy old style",12,"bold")).place(x=0, y=0)
        self.logout = Button(frame_home, text="Đăng xuất", bg="white", bd=0)
        self.logout.place(x=80, y=5)

        self.add_St = Button(frame_home, command=self.add_student_window, text="Thêm sinh viên", font=("times new roman",18,"bold"))
        self.add_St.place(x=100, y=400,width=170, height=80)

        self.add_St1 = Button(frame_home,command=self.add_attandance_window, text="Điểm danh", font=("times new roman",18,"bold"))
        self.add_St1.place(x=300, y=400,width=170, height=80)

        self.add_St = Button(frame_home,command=self.add_management_window, text="Quản lý", font=("times new roman",18,"bold"))
        self.add_St.place(x=500, y=400,width=170, height=80)

        self.add_St = Button(frame_home, text="Báo cáo", font=("times new roman",18,"bold"))
        self.add_St.place(x=700, y=400,width=170, height=80)
        self.bg1 = ImageTk.PhotoImage(file="images/vku.png")
        self.bg_image1 = Label(frame_home, image=self.bg1, bg="white").place(x=0, y=100, relwidth=1)
    def add_student_window(self):
        self.root.withdraw()
        topLevel = Toplevel(self.root)
        app = Student(topLevel)
    
    def add_attandance_window(self):
        self.root.withdraw()
        topLevel1 =  Toplevel(self.root)
        app1 = Attandance(topLevel1)

    def add_management_window(self):
        self.root.withdraw()
        topLevel1 =  Toplevel(self.root)
        app1 = Course(topLevel1)

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm sinh viên-Author Trần Công Ái")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False, False)

        left_Frame = Frame(self.root, bg="white")
        left_Frame.place(x=0,y=0,width=500, height=600)


        lbl_1 = Label(left_Frame, text="Thêm sinh viên",fg="red", bg="white", font=("times new roman",28,"bold"))
        lbl_1.place(x=0, y=30, relwidth=1)

        lbl_2 = Label(left_Frame, text="Họ và tên", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_2.place(x=50, y=150)

        self.nameEntry = Entry(left_Frame,bg="#e0dede", bd=1, font=("times new roman",12))
        self.nameEntry.place(x=50, y=180, height=30, width=180)

        lbl_3 = Label(left_Frame, text="MSSV", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_3.place(x=250, y=150)

        self.MSVEntry = Entry(left_Frame,bg="#e0dede",  font=("times new roman",12))
        self.MSVEntry.place(x=250, y=180, height=30, width=180)

        lbl_4 = Label(left_Frame, text="Lớp", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_4.place(x=50, y=230)

        self.gradeEntry = Entry(left_Frame,bg="#e0dede",  font=("times new roman",12))
        self.gradeEntry.place(x=50, y=260, height=30, width=180)

        lbl_5 = Label(left_Frame, text="Khoa", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_5.place(x=250, y=230)
        khoaList = ["Khoa khoa học máy tính","Quản trị kinh doanh", "Công nghệ kỹ thuật máy tính"]
        self.value_inside = StringVar(root)
        self.value_inside.set("Chọn ngành học")
        self.khoaMenu =  OptionMenu(left_Frame, self.value_inside, *khoaList)
        self.khoaMenu.config(font=("times new roman",12), bg="#e0dede", bd=0)
        self.khoaMenu.place(x=250, y=260, width=180)
        
        self.addPhoto = Button(left_Frame,command=self.addImage, text="Thêm hình ảnh", padx=30, pady=10) 
        self.addPhoto.place(x=150, y= 350)

        self.valueImage = StringVar()

        self.txtImg = Label(left_Frame,textvariable=self.valueImage)
        self.txtImg.place(x=150, y=400)
        
        btn_Submit = Button(left_Frame, command=self.addStudent, text="Lưu vào CSDL", font=("times new roman",13,"bold"))
        btn_Submit.place(x=80, y=450, height=50, width=300)

        #Right Frame
        right_frame = Frame(self.root,bg="lightgray")
        right_frame.place(x=500, y=0, width=500, height=600)

        self.bg1 = ImageTk.PhotoImage(file="images/vku.png")
        self.bg_image1 = Label(right_frame, image=self.bg1, bg="white").place(x=1, y=0, height=600, width=500)



    def addImage(self):
        filename = filedialog.askopenfilename(filetypes=(("image files","*.jpg"),("All files","*.*")))
        self.valueImage.set(filename)
        return filename
    def saveImage(self, filename,name):

        head_tail = os.path.split(filename)
        new_head = name + "-" + head_tail[1] 
        targetFolder = "F:/Tài liệu/tutorial/ai-recogation/ImagesAttandance/" + new_head 
        # print(targetFolder)


        try:
            shutil.copyfile(filename, targetFolder)    
            print(f"Thành công {new_head}")   

        except:
            print("Lỗi thất bại") 
    
        return new_head
    def addStudent(self):
        # ten, mssv, lop, khoa
        ten = self.nameEntry.get()
        mssv = self.MSVEntry.get()
        lop = self.gradeEntry.get()
        khoa = self.value_inside.get()
        filename = self.valueImage.get()
        print(filename)
        images = self.saveImage(filename,mssv)
        # images
        if ten == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập tên")
        elif mssv == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập mã sinh viên")
        elif lop == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập lớp")
        elif mssv == "" or khoa=="Chọn ngành học":
            messagebox.showerror("Thông báo", "Vui lòng chọn khoa")
        else:
            try:
                mydb = connection()
                mycursor = mydb.cursor()

                sql = "INSERT INTO students (ten, mssv, lop, khoa, hinhanh) VALUES (%s, %s, %s, %s, %s)"
                val = (ten, mssv, lop, khoa, images)

                mycursor.execute(sql, val)

                result = mydb.commit()
                return 1
            except mysql.connector.Error as error:
                return error   
        # GUI


class Attandance:
    def __init__(self, root):
        self.root = root
        self.root.title("Trang điểm danh-Author Trần Công Ái")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False, False)

        left_Frame = Frame(self.root, bg="white")
        left_Frame.place(x=0,y=0,width=350, height=600)

        lbl_1 = Label(left_Frame, text="Điểm danh",fg="red", bg="white", font=("times new roman",28,"bold"))
        lbl_1.place(x=0, y=30, relwidth=1)

        lbl_2 = Label(left_Frame, text="Tên môn học", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_2.place(x=80, y=100)
        
       
        khoaList = []
        mydb = connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT name from courses")
        results = my_cursor.fetchall()
        for x in results:
            khoaList.append(x[0])
        # for course in my_cursor:
        #     print(my_cursor[course])
        #     khoaList.append(course)
        
        # print(khoaList)
        self.value_inside1 = StringVar(root)
        self.value_inside1.set(khoaList[0])
        self.dayMenu =  OptionMenu(left_Frame, self.value_inside1, *khoaList)
        self.dayMenu.config(font=("times new roman",12), bg="#e0dede")
        self.dayMenu.place(x=80,y=130, width=200, height=40)

        # lbl_3 = Label(left_Frame, text="MSSV", bg="white",fg="gray", font=("times new roman",12,"bold"))
        # lbl_3.place(x=280, y=100)
        
        x = datetime.now()
        day = x.strftime("%d")
        month = x.strftime("%m")
        year = x.strftime("%Y")
        self.timeNow = "{}/{}/{}".format(day, month, year)

        lbl_3 = Label(left_Frame, text="Thời gian", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_3.place(x=80, y=200)

        lbl_3 = Label(left_Frame, text=self.timeNow, bg="lightgray",fg="black", font=("times new roman",12,"bold"))
        lbl_3.place(x=80, y=230, height=40, width=200)

        self.btnDiemDannh = Button(left_Frame, command=self.Attendance, text="Điểm danh", font=("times new roman",12))
        self.btnDiemDannh.place(x=80,y=300, width=200, height=40)

        self.btnBack = Button(left_Frame, command=self.returnPage, text="Thoát", font=("times new roman",12))
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

    def findEncode(self,images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    # def markAttendance(self,name):
    #     with open('Attendance.csv', 'r+', encoding='utf8') as f:
    #         myDataList = f.readlines()
    #         nameList = []
    #         newList =  []
    #         for line in myDataList:
    #             entry = line.split(',')
    #             nameList.append(entry[1])
    #         print(nameList)
            
    #         infoAttList = []
    #         newInfoArray = []
    #         newInfoArray =name.upper().split('-')

    #         mssv = newInfoArray[0]
    #         # print("mảng thông tin ")
    #         mydb = connection()
    #         mycursor = mydb.cursor()
    #         sql = "SELECT * FROM students WHERE mssv = %s"
    #         val = (mssv, )
    #         mycursor.execute(sql, val)
    #         myresult = mycursor.fetchall()
    #         for x in myresult:
    #             i =0 
    #             while i < len(x):
    #                 newList.append(x[i])
    #                 i+=1
            
    #         print(nameList, mssv)
    #         if mssv  not in nameList:
    #             now = datetime.now()
    #             dtString = now.strftime('%H:%M:%S')
    #             f.writelines(f'\n{newList[1]},{newList[2]},{newList[3]},{newList[4]},{dtString}')
            
    def uploadDBAttandance(self, name, mssvList, thoigian, monhoc):
        newList = []
        mssv = name.upper().split('-')[0]
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
        else:
            print("Đã điểm danh")

    def Attendance(self):
        path = 'ImagesAttandance'
        images = []
        classNames = []
        myList = os.listdir(path)
        mssvList = []
        thoigian = self.timeNow
        monhoc = self.value_inside1.get()

        mydb = connection()
        my_cursor = mydb.cursor()
        sql = "SELECT mssv FROM attendance WHERE thoigian=%s AND monhoc=%s"
        val = (thoigian,monhoc)
        my_cursor.execute(sql, val)
        results =  my_cursor.fetchall()
        for x in results:
            mssvList.append(x[0])
        print(mssvList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            # print(curImg)
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])

        encodeListKnown = self.findEncode(images)
        print('Encoding Complete')

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1,x2,y2,x1 = faceLoc
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, name, (x1 + 6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    # self.markAttendance(name)
                    self.uploadDBAttandance(name, mssvList, thoigian, monhoc)
            cv2.imshow('Webcam', img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        self.showData(thoigian, monhoc)
        
       
    def showData(self, thoigian, monhoc):
        print(thoigian, monhoc)
        mydb = connection()
        my_cursor = mydb.cursor()
        sql = "SELECT * FROM attendance WHERE thoigian= %s AND monhoc = %s"
        val =  (thoigian, monhoc)
        my_cursor.execute(sql, val)
        i = 0
        
        for i in self.tree1.get_children():
            self.tree1.delete(i)
        for course in my_cursor:
            self.tree1.insert("",'end', values=(course[1],course[2],course[3],course[4]))

    def returnPage(self):
        self.root.withdraw()
        topLevel1 =  Toplevel(self.root)
        app1 = Home(topLevel1)  
            

    

# GUI Quản lý
class Course:
    def __init__(self, root):
        self.root = root
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
        self.value_inside1 = StringVar(root)
        self.value_inside1.set("Chọn ngày học")
        self.dayMenu =  OptionMenu(right_frame, self.value_inside1, *khoaList)
        self.dayMenu.config(font=("times new roman",12), bg="#e0dede", bd=0)
        self.dayMenu.place(x=70, y=330, width=200)
       
        self.btnAddCourse = Button(right_frame,command=self.addCourse, text="Thêm", font=("times new roman",12))
        self.btnAddCourse.place(x=70,y=400, width=200)

        self.btnReturn = Button(right_frame,command=self.returnPage, text="Quay lại", font=("times new roman",12))
        self.btnReturn.place(x=70,y=400, width=200)

    def returnPage(self):
        self.root.withdraw()
        topLevel1 =  Toplevel(self.root)
        app1 = Home(topLevel1)        

    def showData(self):
        mydb = connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM courses limit 0,10")
        i = 0
        
        for i in self.tree.get_children():
            self.tree.delete(i)
        for course in my_cursor:
            self.tree.insert("",'end', values=(course[0],course[1],course[2],course[3]))

    def addCourse(self):
        nameCourse = self.nameCourse.get()
        startAt = self.startAtCourse['text']
        dayLearn = self.value_inside1.get()
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

    
            





root = Tk()
obj = Home(root)
root.mainloop()