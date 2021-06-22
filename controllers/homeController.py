from views.homeView import HomeView
from controllers.studentController import StudentController
from controllers.attendanceController import AttendanceController
from controllers.courseController import CourseController
class HomeController:
    def __init__(self, LoginController):
        self.loginController = LoginController
        self.view = HomeView()
    def run(self):
        self.view.add_St1.bind("<Button-1>", self.addStGUI)
        self.view.add_St2.bind("<Button-1>", self.addStGUI2)
        self.view.add_St3.bind("<Button-1>", self.addStGUI3)
        self.view.add_St4.bind("<Button-1>", self.addStGUI4)
        self.view.root.mainloop()
    def addStGUI(self, event):
        self.view.root.withdraw()
        studentController = StudentController(HomeController)
        studentController.run()

    def addStGUI2(self, event):
        self.view.root.withdraw()
        attController = AttendanceController(HomeController)
        attController.run()
    def addStGUI3(self, event):
        self.view.root.withdraw()
        courseController = CourseController(HomeController)
        courseController.run()
    def addStGUI4(self, event):
        self.view.root.withdraw()
        