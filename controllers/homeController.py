from views.homeView import HomeView
from controllers.studentController import StudentController
from controllers.attendanceController import AttendanceController
class HomeController:
    def __init__(self):
        self.view = HomeView()
    def run(self):
        self.view.add_St1.bind("<Button-1>", self.addStGUI)
        self.view.add_St2.bind("<Button-1>", self.addStGUI2)
        self.view.root.mainloop()
    def addStGUI(self, event):
        self.view.root.withdraw()
        studentController = StudentController(HomeController)
        studentController.run()

    def addStGUI2(self, event):
        self.view.root.withdraw()
        attController = AttendanceController(HomeController)
        attController.run()