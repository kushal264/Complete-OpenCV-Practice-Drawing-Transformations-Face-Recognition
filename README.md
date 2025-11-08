# Complete-OpenCV-Practice-Drawing-Transformations-Face-Recognition
This repository contains my practice and implementation of various OpenCV image-processing techniques, starting from basic operations to a fully working face detection and face recognition system.
# 📸 Face Detection & Recognition using OpenCV (Python)

The project is organized into structured folders so anyone can clearly understand the flow:  
✅ Image Processing Basics  
✅ Transformations  
✅ Face Detection  
✅ Face Recognition (Training + Prediction)

---

## ✅ Features

### 🔹 **1. Basic Image Operations**
- Create blank images
- Draw circles, lines, rectangles
- Add text to images
- Display images using `cv.imshow()`

### 🔹 **2. Image Transformations**
- Translation (shift in x and y directions)
- Rotation around any point
- Implemented using `cv.warpAffine()`

### 🔹 **3. Face Detection**
- Use `haarcascade_frontalface_default.xml`
- Convert images to grayscale
- Detect faces using `detectMultiScale()`
- Draw bounding boxes around detected faces

### 🔹 **4. Face Recognition (LBPH)**
- Train custom dataset using LBPH Face Recognizer
- Extract face features (Region of Interest)
- Save training data:
  - `face_trained.yml`
  - `features.npy`
  - `labels.npy`
- Predict person name from new images
- Display prediction with confidence score

---

## 🗂 Folder Structure


