import cv2 as cv
import numpy as np

# Load the image
img = cv.imread(r'c:\Users\LENOVO\Downloads\My Handsome Cat.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)

#color channels
b,g,r=cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
#cv.imshow('gray',gray)
#cv.imshow('hsv',hsv)
#cv.imshow('lab',lab)

blank=np.zeros(img.shape[:2],dtype="uint8")
blue=cv.merge([b,blank,blank])
cv.imshow('blue1',blue)
cv.waitKey(0)
cv.destroyAllWindows()


