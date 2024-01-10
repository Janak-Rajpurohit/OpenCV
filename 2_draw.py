import cv2 as cv
import numpy as np

#  blank image for drawing shapes on it , shape 500x500x3
blankImg = np.zeros((500,500,3),dtype='uint8')
cv.imshow("Blank",blankImg) 

# # paint img with certain color
# # blankImg[:]=0,0,255        # plaint img by red  RGB 0,0,255
# blankImg[200:300 , 300:400] = 0,255,0
# cv.imshow("Red",blankImg)

# # draw an rectangle 
#             # img , start , end , color , thickness of border (int) / to fill thickness=cv.FILLED or -1
# cv.rectangle(blankImg,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
# cv.imshow("Rectangle",blankImg)

# # draw a circle 
#                     # center, radius,color 
# cv.circle(blankImg,(100,150),40,(0,0,255),thickness=3)
# cv.imshow("Circle",blankImg)

# # draw line
# cv.line(blankImg,(0,0), (blankImg.shape[1]//2 , blankImg.shape[0]//2) , (255,255,255) ,thickness=3)
# cv.imshow("Line",blankImg)

# # write text on img
#             # img , text , position , font , color
# cv.putText(blankImg,"Hello its text",(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0))
# cv.imshow("TEXT",blankImg)

# img  = cv.imread("photos and videos/img2.jpg")
# cv.imshow("Me",img)

cv.waitKey(0)