import os 
import cv2 as cv
import numpy as np


# creating training dataset
classes = ["jan","srk"]

face_cas=cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

photo=[]
labels = []
for i in os.listdir("data"):
    for photos in os.listdir(os.path.join("data",i)):

        img = cv.imread(os.path.join("data",i,photos))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_rect = face_cas.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
        for x,y,w,h in face_rect:  #iterate through face detected in single img
            face_rol = gray[y:y+h , x:x+w]
            photo.append(face_rol)
            labels.append(classes.index(i))

print(photo)
print(labels)
print(len(photo) , len(labels))
photo= np.array(photo,dtype='object')
labels= np.array(labels)

# train recognizer and saving
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(photo,labels)
face_recognizer.save("face_recognizer_model.yml")
np.save("photo.npy",photo)
np.save("labels.npy",labels)



