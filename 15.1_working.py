import numpy as np 
import cv2 as cv

classes = ["jan","srk"]
face_cas=cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

# --- RUN only one time --- #
# loading train data
# labels = np.load("labels.npy",allow_pickle=True)
# photo = np.load("photo.npy")

# loading model
face_recognizer = cv.face.LBPHFaceRecognizer_create() 
face_recognizer.read("face_recognizer_model.yml")


# img = cv.imread("photos and videos/img2.jpg")
img = cv.imread("photos and videos/OIP.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Me",gray)

face_rect  = face_cas.detectMultiScale(gray, 1.1 , 4)

for x,y,w,h in face_rect:
    face_rol = gray[y:y+h , x:x+w]

    label, confidence = face_recognizer.predict(face_rol)
    print(f"Label - {classes[label]}\nConfidence - {confidence}")

    cv.putText(img,str(classes[label]),(40,40) , cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y) , (x+w,y+h),(0,255,0),thickness = 2)

# at last img is shown
cv.imshow("Detected Face",img)


cv.waitKey(0)
