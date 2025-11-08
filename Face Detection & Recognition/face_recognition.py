import numpy as np
import os
import cv2 as cv
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

people = ['chris hamssworth', 'damon salvotore', 'scarlet', 'steve rogers']
#feature=np.load('features.npy')
#labels=np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')  # should now work properly


img=cv.imread(r'c:\Users\LENOVO\Desktop\face images\damon salvotore\@iansomerhalder on ig_.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


 # Detect faces in the image
faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for (x, y, w, h) in faces_rect:
    # Extract the region of interest (ROI) which is the face
    faces_roi = gray[y:y+h, x:x+h]
    label,confidence=face_recognizer.predict(faces_roi)
    print(f"label={people[label]} with a confidence of={confidence}")
    cv.putText(img,str(people[label]),(20,20),cv.FRONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("person",gray)
cv.imshow('detected face',img)
cv.waitKey(0)
cv.destroyAllWindows()