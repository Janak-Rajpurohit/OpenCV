
# color space - RGB,BGR,GRAY,HSV - system representing the space of colors
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

# plt.imshow(img)      # Matplotlib assume it as RGB , so there is inversion of color
# plt.show()

# converting Gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# HSV 
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# lab 
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

# BGR to RGB 
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)   #inversion of color coz it assume it as BGR image

plt.imshow(rgb)
plt.show()

# we convert gray to bgr but can't gray to  hsv directly


cv.waitKey(0)