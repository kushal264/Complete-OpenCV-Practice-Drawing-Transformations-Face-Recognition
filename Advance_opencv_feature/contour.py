import cv2 as cv
import numpy as np

# Load the image
img = cv.imread(r'c:\Users\LENOVO\Downloads\My Handsome Cat.jpeg')

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Canny edge detection
canny = cv.Canny(gray, 125, 175)

# Find contours
contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Apply thresholding
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# Optional: display the results
cv.imshow('Canny', canny)
cv.imshow('Threshold', thresh)
cv.waitKey(0)
cv.destroyAllWindows()
