
import numpy as np
import cv2 as cv

# Load the image
img = cv.imread(r'c:\Users\LENOVO\Downloads\IPl 2023 Orange purple Cap.jpeg')

#averaging: 3,3 window ka group m  pixel ki value average hogi uska baki neighbour pixels where 3*3 is kernal o that window

average=cv.blur(img,(3,3))
cv.imshow('average',average)

#same bs isma hr pixel ko weight diya jata h or us weight ka base p us window ko blur krta h

blur=cv.GaussianBlur(img,(3,3),0)
cv.imshow('blur',blur)

#  here giving 3 will means 3,3 kernal and blur based on median of all neighbour pixels of that window, better to remove noisr data

median=cv.medianBlur(img,3)
cv.imshow('median',median)

#bilateral:(more effectyive as it does not remove edges)10:diameter of window,35 is sigma color more value more smooth less give sharper
# 25:A larger sigmaSpace means that pixels farther apart can still influence each other if their colors are similar.
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)
cv.destroyAllWindows()
