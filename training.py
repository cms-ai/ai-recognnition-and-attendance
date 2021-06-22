import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import os

data_path = 'dataset/'
TrainingData = []
Labels = []
for folders in listdir(data_path):
    folder_path = data_path + f"{folders}/"
    onlyfiles = [f for f in listdir(folder_path) if f.endswith("png") or f.endswith("jpg")]
    for i, files in enumerate(onlyfiles):
        image_path = os.path.join(folder_path, onlyfiles[i])
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        TrainingData.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(TrainingData), np.asarray(Labels))

print("Dataset Model Training Completed ")
face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_default.xml')


def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if faces is():
        return img, []

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
        return img, roi
cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))



        if confidence > 82:
            cv2.putText(image, "Trần Công Ái", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow('Face Cropper', image)

        else:
            cv2.putText(image, "Unknown", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)


    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image)
        pass

    if cv2.waitKey(1)==13:
        break


cap.release()
cv2.destroyAllWindows()