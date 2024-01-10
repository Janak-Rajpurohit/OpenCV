import cv2 as cv

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("RGB",img)

gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)  # converting RGB 2 GRAY
cv.imshow("Gray",gray)

# Blur img
                            #odd number kernal size , to increase blur increse kernal size
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur",blur)

# Edge cascade
# to reduce edge ,  give blur img 
canny = cv.Canny(img,90,90)       #thresholf value level of edging on img
cv.imshow("Canny",canny)

# Dilating the img using structuring element (canny)
dilated =  cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dialted",dilated)

#  eroding is opposite of dilating
# we get back the same canny from dilated img
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)

# Resize
resized = cv.resize(img,(500,500),interpolation =cv.INTER_CUBIC)   # by default INTER_AREA for reducing img into smaller img
                                                                   # INTER_CUBIC for enlarging img (Slowest but hight quality)
cv.imshow("Resixed",resized)

# Cropping
cropped = img[50:100 , 200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
