import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier("cascades\data\haarcascade_frontalface_default.xml")

def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is():
        return None
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count = count + 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        filenamepath = "dataset/"+"18IT049_"+str(count)+'.jpg'
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