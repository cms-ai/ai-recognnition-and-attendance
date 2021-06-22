from views.studentView import StudentView
from models.studentModel import StudentModel
from config.connect import connection
from tkinter import messagebox, filedialog, ttk
import cv2
import numpy as np
from PIL import Image
import pickle
import time
import os


class StudentController:
    def __init__(self, HomeController):
        self.view = StudentView()
        self.homeController = HomeController
        self.model = StudentModel()
    def run(self):
        self.view.btnSubmit.bind("<Button-1>", self.addStudent)
        self.view.btnAddPhoto.bind("<Button-1>", self.addPhotoTrain)
        self.view.btnReturn.bind("<Button-1>", self.returnPage)
        self.view.root.mainloop()
    def returnPage(self, event):
        self.view.root.withdraw()
        homeController = self.homeController()
        homeController.run()
        
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
    def face_extractor(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        face_classifier = cv2.CascadeClassifier("cascades\data\haarcascade_frontalface_default.xml")
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        if faces is():
            return None
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    
        # print(y_labels)
        # print(x_train)

    def TrainData(self):
        BASE_DIR = r"f:\Tài liệu\tutorial\vkuattendance"
        image_dir = os.path.join(BASE_DIR, "dataset")

        face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_id = 0
        label_ids = {}
        y_labels = []
        x_train = []

        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()
                    # print(label, path)
                    
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1
                    
                    id_ = label_ids[label]
                    # print(label_ids)
                    # y_labels.append(label)
                    # x_train.append(path)


                    pil_image = Image.open(path).convert("L") #grayscale
                    size = (550, 550)
                    final_image = pil_image.resize(size, Image.ANTIALIAS)
                    image_array = np.array(pil_image, "uint8")
                    # print(image_array)
                    faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
                    for (x,y,w,h) in faces:
                        roi = image_array[y: y + h, x: x+w]
                        x_train.append(roi)
                        y_labels.append(id_)
        # print(y_labels)
        # print(x_train)

        with open("labels.pickle", 'wb') as f:
            pickle.dump(label_ids, f)

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("trainer.yml")

    
    def addPhotoTrain(self, event):
        mssv = self.view.MSVEntry.get().upper()
        face_classifier = cv2.CascadeClassifier("cascades\data\haarcascade_frontalface_default.xml")
        
        cap = cv2.VideoCapture(0)
        count = 0
        os.mkdir(f"dataset/{mssv}")

        while True:
            ret, frame = cap.read()
            if self.face_extractor(frame) is not None:
                count = count + 1
                face = cv2.resize(self.face_extractor(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                filenamepath = f"dataset/{mssv}/{mssv}_"+str(count)+'.jpg'
                cv2.imwrite(filenamepath, face)
                cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Face Cropper", face)
            else:
                print("Not found")
            
            if cv2.waitKey(1)==13 or count==30:
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Completed")
