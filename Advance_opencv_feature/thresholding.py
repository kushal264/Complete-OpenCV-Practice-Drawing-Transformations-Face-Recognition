import cv2 as cv
import numpy as np
img=cv.imread(r'c:\Users\LENOVO\Downloads\My Handsome Cat.jpeg')
gray=cv.cvtcolor(img,cv.COLOR_BGR2GRAY)

#simple threshold- threshold is used to binarise a img where we set a threshold value & above threshold to 255 pixel value it covert it to white(1)
# else less than threshold pixel value it becomes black, in simple thresh. we manually set threshold where 150 is threshold value and 255 is max pixel value
threshold, thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("simple threshold",thresh)
#in inverse black becomes 1 and zero becomes white
threshold, thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_inv)
cv.imshow("inverse threshold",thresh_inv)

#adaptive threshold
adaptive_thresh=cv.adaptivethreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,3)
cv.imshow("adaptive thresh",adaptive_thresh)
cv.waitKey(0)
cv.destroyAllWindows()