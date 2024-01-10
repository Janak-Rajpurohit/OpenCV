import cv2 as cv
import numpy as np

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

# Translation (shift img (up/dowwn/right/left) )
def translation(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1],img.shape[0])           #width , height
    return cv.warpAffine(img,transMat,dim)

# -x -> left translation
# -y -> up translation
# +x -> right translation
# -y -> down translation

translated = translation(img,-100,-100)   # shift 100 right 100 up
cv.imshow("Translated",translated)

# Rotation , rotating with an angle on any point 
def rotate(img,angle,rotPoint=None):           #by def none i.e.. center
    (height,width) = img.shape[:2]

    if rotPoint==None:
        rotPoint = (width//2,height//2)
                                                
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)      #rotation matrix with scale value 1.0
    dim = (width , height)

    return cv.warpAffine(img,rotMat,dim)

rotated = rotate(img,30)       # +30 anti clock wise
cv.imshow("Rotated",rotated)
# if you rotated img then it will rotate black bg also from first rotated img

# resizing
resized = cv.resize(img,(300,300),interpolation=cv.INTER_AREA)
cv.imshow("Resized Img",resized)

# fllipping         # 0 - flipping vertically , 1 horizontally , -1 Both
fliped = cv.flip(img,0)
cv.imshow("Flipped",fliped)

# cropping
crop = img[200:400 , 300:400]
cv.imshow("Cropped",crop)

cv.waitKey(0)

