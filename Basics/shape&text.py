import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype="uint8")

# Draw a filled circle in the center
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 150, (255, 150, 0), thickness=-1)

# Display the image with the circle
cv.imshow('blank', blank)
cv.waitKey(0)

# Draw a line on the same image
cv.line(blank, (0, 0), (0, 80), (0, 220, 0), thickness=-1)

# Show the image again with the line now added
cv.imshow('line', blank)
cv.waitKey(0)

cv.destroyAllWindows()
