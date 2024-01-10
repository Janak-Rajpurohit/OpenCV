# countours are border of object in img
import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# # reducing contour by bluring the edges
# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

canny = cv.Canny(img,125,125)
cv.imshow("Canny",canny)

                                                # mode - all contours
contours , hierarchies = cv.findContours(canny,cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE) 
# contours - python list of all contours in image
# hierarchies - hierarchical representation of contors EG..  circle inside square
# RETR_EXTERNAL all outside contours , RETR_INTERNAL all inside , RETR_TREE all hierarchcal contours
# CHAIN_APPROX_NONE - does'nt approx contours  EG for line it returns all points on that line
# CHAIN_APPROX_SIMPLE - compress line and give two end points of line
# another way of finfing contour

# # if pix <125 set it blank if pix>225 set it white   i.e.. binarizing image into white or black
# ret , thres = cv.threshold(gray,125,225, cv.THRESH_BINARY)
# cv.imshow("Threshold img",thres)
# contours , hierarchies = cv.findContours(thres,cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)

print(f"NO. of Contours {len(contours)}")    # SIMPLE - 181 contours # NONE - 181 , no points to compress   # after blur 65

# drawing contour on img
blank = np.zeros(img.shape,dtype='uint8')
                # on img , countour list , -1 -> all countours , color, thickness
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Countours Draw",blank)

# first canny method , thres has its  disadvantages


cv.waitKey(0)