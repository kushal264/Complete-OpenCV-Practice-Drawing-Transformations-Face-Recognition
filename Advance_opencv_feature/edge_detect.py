import cv2 as cv
import numpy as np

# Load the image
img = cv.imread(r'c:\Users\LENOVO\Downloads\My Handsome Cat.jpeg')
if img is None:
    raise FileNotFoundError("Image not found. Check the path again.")

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Laplacian edge detection
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Apply Sobel edge detection (X and Y directions)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

# Convert Sobel results to uint8 before combining
abs_sobelx = np.uint8(np.absolute(sobelx))
abs_sobely = np.uint8(np.absolute(sobely))
sobel_combine = cv.bitwise_or(abs_sobelx, abs_sobely)
cv.imshow('Sobel Combined', sobel_combine)

# Apply Canny edge detection
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()
