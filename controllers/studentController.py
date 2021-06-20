from views.studentView import StudentView
from models.studentModel import StudentModel
from config.connect import connection
from tkinter import messagebox, filedialog, ttk

class StudentController:
    def __init__(self):
        self.view = StudentView()
        self.model = StudentModel()
    def run(self):
        self.view.btnSubmit.bind("<Button-1>", self.addStudent)
        self.view.root.mainloop()

    def addStudent(self, event):
        ten = self.view.nameEntry.get()
        mssv = self.view.MSVEntry.get()
        lop = self.view.gradeEntry.get()
        khoa = self.view.value_inside.get()
        if ten == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập tên")
        elif mssv == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập mã sinh viên")
        elif lop == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập lớp")
        elif  khoa =="Chọn ngành học":
            messagebox.showerror("Thông báo", "Vui lòng chọn khoa")
        else:
            result = self.model.setStudent(ten, mssv, lop, khoa)  
            if result:
                messagebox.showinfo("Thành công", "Thêm sinh viên thành công")
            else:
                messagebox.showerror("Thất bại", f"Lỗi {result}")
