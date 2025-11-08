import os
import numpy as np
import cv2 as cv

# List of people (folder names in the training dataset directory)
people = ['chris hamssworth', 'damon salvotore', 'scarlet', 'steve rogers']
# Path to the dataset directory (each person's folder is inside this)
DIR = r'C:\Users\LENOVO\Desktop\face images'

# or p[]
# for i in os.listdir(r'c:\Users\LENOVO\Desktop\face images')
# p.append(i)


# Load the Haar Cascade XML for face detection
haar_cascade = cv.CascadeClassifier("frontalface_harcascade.xml")

# Lists to store features (face regions) and corresponding labels (numeric ID)
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            # Read the image
            img_array = cv.imread(img_path)
            if img_array is None:
                continue  # Skip if image not read correctly

            # Convert the image to grayscale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                # Extract the region of interest (ROI) which is the face
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

# Run the training data collection
create_train()

# Convert lists to numpy arrays for further processing
features = np.array(features, dtype='object')
labels = np.array(labels)

print(f'Length of features: {len(features)}')
print(f'Length of labels: {len(labels)}')
print("training done--")

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.save("face_trained.yml")
face_recognizer.train(features,labels)
np.save("features.npy",features)
np.save("labels.npy",labels)