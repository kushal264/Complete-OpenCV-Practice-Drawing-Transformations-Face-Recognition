import numpy as np
import cv2 as cv
img=cv.imread(r"c:\Users\LENOVO\Downloads\_3.jpeg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray ",gray)
haar_cascade=cv.CascadeClassifier("frontalface_harcascade.xml")
# 1 type ka classifier jo img ka face ka features ko smjh ka unhe classify krta h or iska liya ham scartch sa likha feature of face extract
#krna ka liya frontal_casscade nam ki xml file ka code sa karenga

face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2)
# yaha p face_rect return karega list of all the faces jinko detect kiya  h img m
print(f"number of faces: {len(face_rect)}")

for(x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    # ya loop hr 1 list k face p rectangle draw karega jiska pixel value x  y h

cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()