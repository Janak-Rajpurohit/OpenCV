import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

# thresholding - binarizing image (black or white)
# if pix < threshold value set it to 0 (black)
# if pix > threshold value set it to 255 (white)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# SImple thresholding
                                #img, threshold val, value to set if pix is >, threshold type
threshold, thresh = cv.threshold(gray,120,255,cv.THRESH_BINARY)
cv.imshow("Thershold img",thresh)

# inverse the above thresh set value to 255 which are < 120
threshold, thresh_inv = cv.threshold(gray,120,255,cv.THRESH_BINARY_INV)
cv.imshow("Thershold Inverse img",thresh_inv)
# here we mannualy define threshols value 


# Adaptive Thresholding   - an  optimal threshold value is calc              
                                    #img , set 255 if > ,  kernal size 11 , C value =3 - subtracting from mean for finetuning
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive Thershold",adaptive_thresh)

# inverse
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,15,3)
cv.imshow("Adaptive Thershold",adaptive_thresh)



cv.waitKey(0)