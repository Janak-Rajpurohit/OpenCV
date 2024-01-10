import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

# window , matrix on img and blur/modification is applied to center pixel of matrox

# averaging       #high kernal size more it gets blur
avg = cv.blur(img,(3,3))
cv.imshow('avg',avg)

# surrounding pix gets weight , avg of weight is given to cneter pix
# it is more natural than avg
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gauss',gauss)

# Median Blur   # median of surrounding pix
# more effective in reducing noise 
median = cv.medianBlur(img,3)
cv.imshow("Median",median)

# Bilateral Blur  # apply bluring retain edges in img
                            # kernal , surrounding colors , sigma space for influcence center pix from pix outside window 
bilat = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral Blur",bilat)

cv.waitKey(0)