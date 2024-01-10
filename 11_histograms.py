import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("photos and videos/img2.jpg")
cv.imshow("Me",img)

# # computing histograms
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# # grayscale hiatogram #list og imgs , list of channels ,mask(you can give mask) ,list of bins,range of possible pix value
# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

# plt.figure()
# plt.title("Grayscale histogram")
# plt.xlabel("Bins")
# plt.ylabel("No of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])

# plt.show()


# COLOR HISTOGRAM
colors = ('b','g','r')
plt.figure()
plt.title("Grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
for i,col in enumerate(colors):
    # grayscale hiatogram #list og imgs , list of channels ,mask(you can give mask) ,list of bins,range of possible pix value
    color_hist = cv.calcHist([img],[i],None,[256],[0,256])    
    plt.plot(color_hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)