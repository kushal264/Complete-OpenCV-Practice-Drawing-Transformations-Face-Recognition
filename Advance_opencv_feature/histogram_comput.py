import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread(r'C:\Users\LENOVO\Downloads\ironman.jpeg')
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank = np.zeros((img.shape[:2]), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, thickness=-1)
masking=cv.bitwise_and(grey,grey,mask=rectangle)
#histogram is used to represent the distributon of pixels intensity in a image
gray_hist=cv.calcHist([grey],[0],masking,[256],[0,256])
plt.figure()
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("no. of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.imshow('masked image', masking)

cv.waitKey(0)
cv.destroyAllWindows()