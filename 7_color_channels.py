import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

blank = np.zeros(img.shape[:2],dtype='uint8')

#  spliting the color channel bgr
b,g,r = cv.split(img)

# cv.imshow('Green',g)
# cv.imshow('Blue',b)     # blue [part is white]
# cv.imshow('Red',r)

# print("Img",img.shape)
# print("g",g.shape)
# print("b",b.shape)
# print("r",r.shape)
# # gray scale img has shape of 1

# # merging three img to geet og one
# merged  = cv.merge([b,g,r])
# cv.imshow("Merged BGR",merged)

blue = cv.merge([b,blank,blank])
red = cv.merge([blank,blank,r])
green = cv.merge([blank,g,blank])

cv.imshow("Blue",blue)


cv.waitKey(0)