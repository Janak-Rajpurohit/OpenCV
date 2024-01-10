import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

# dimension of mask should be same as that of img
blank = np.zeros(img.shape[:2],dtype="uint8")

# mask shape circle
mask = cv.circle(blank,(img.shape[1]//2 - 50,img.shape[0]//2),200,255,-1)
cv.imshow("mask",mask)

masked_img = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked image",masked_img)

cv.waitKey(0)