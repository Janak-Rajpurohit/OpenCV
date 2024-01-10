import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# reads xml code (cascade file)
face_cas=cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

                                                            #increse neighbours reduce sensitivity
faces_rect = face_cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces found {len(faces_rect)}")

#iterate through face detected in single img
for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Detected",img)

cv.waitKey(0)