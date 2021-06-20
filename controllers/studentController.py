from views.studentView import StudentView

class StudentController:
    def __init__(self):
        self.view = StudentView()
    def run(self):
        self.view.root.mainloop()