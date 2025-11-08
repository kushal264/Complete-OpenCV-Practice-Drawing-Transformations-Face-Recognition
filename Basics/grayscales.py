import cv2 as cv
img=cv.imread(r'C:\Users\LENOVO\Downloads\201430.jpg')
resize=cv.resize(img,(700,500),interpolation=cv.INTER_AREA)
gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(resize,(7,7),cv.BORDER_DEFAULT)
colorsss = cv.cvtColor(resize,cv.COLOR_BGR2RGB)
crop=resize[50:200,200:400]
cv.imshow('crop',crop)
cv.imshow('rgb',colorsss)
cv.imshow('blur',blur)
cv.imshow('gray',gray)
cv.waitKey(0)
cv.destroyAllWindows()
