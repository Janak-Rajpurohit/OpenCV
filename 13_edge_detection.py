import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

gray  = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Lap",lap)

# Sobel combines gradient from x and y 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0) 
sobely = cv.Sobel(gray,cv.CV_64F,0,1) 
combine_sobel = cv.bitwise_or(sobelx , sobely)

cv.imshow("sobel X",sobelx)
cv.imshow("sobel Y",sobely)
cv.imshow("commbined sobel ",combine_sobel)

# canny is high stage process which make use of Sobel
canny = cv.Canny(gray,150,175)
cv.imshow("Canny",canny)

cv.waitKey(0)