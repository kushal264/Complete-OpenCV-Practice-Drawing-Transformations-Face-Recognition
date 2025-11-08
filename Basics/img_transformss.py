import cv2 as cv
import numpy as np
img = cv.imread(r'c:\Users\LENOVO\Downloads\My Handsome Cat.jpeg')
def translation(img,x,y):
    transmat=np.float32([[1,0,-x],[0,1,-y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)
translated=translation(img,100,100)

#rotation
def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
    rotmat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotmat,dimensions)
cv.imshow('translated',translated)
rotation=rotate(img,45)
cv.imshow('rotate',rotation)
cv.waitKey(0)
cv.destroyAllWindows()