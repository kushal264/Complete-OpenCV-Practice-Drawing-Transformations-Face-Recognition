import numpy as np
import cv2 as cv
img=cv.imread(r'C:\Users\LENOVO\Downloads\ironman.jpeg')
blank = np.zeros((img.shape[:2]), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, thickness=-1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, thickness=-1)

weired_shape = cv.bitwise_and(rectangle, circle)

# Apply the mask to the image
masked = cv.bitwise_and(img, img, mask=weired_shape)
# masking is used to extract (or highlight) only a specific part of the image, masking img should be of same size as img
cv.imshow('weired shape', weired_shape)
cv.imshow('masked image', masked)

cv.waitKey(0)
cv.destroyAllWindows()