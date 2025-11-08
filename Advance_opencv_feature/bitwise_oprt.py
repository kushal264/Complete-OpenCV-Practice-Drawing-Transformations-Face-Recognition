import numpy as np
import cv2 as cv

blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, thickness=-1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, thickness=-1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)
#bitwise and => gives intersecting region
#bitwise or => gives  non intersecting region and intersectiong region
#bitwise xor => gives  non intersecting region
bitwise_and = cv.bitwise_and( rectangle,circle)
bitwise_or = cv.bitwise_or(rectangle,circle)
bitwise_xor = cv.bitwise_xor( rectangle,circle)
bitwise_not = cv.bitwise_not(circle)

cv.imshow('bitwise_and', bitwise_and)
cv.imshow('bitwise_or', bitwise_or)
cv.imshow('bitwise_xor', bitwise_xor)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()
