import cv2
import os

img = cv2.imread('3.jpg')
imgWithRect = cv2.imread('3.jpg')
if os.path.isdir('faces') == 0: 
    os.mkdir('faces')
cascadePath = ".venv/lib64/python3.12/site-packages/cv2/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.1, 4)
for(x1, y1, x2, y2) in faces:
    cv2.rectangle(imgWithRect,(x1, y1), (x1+x2, y1+y2), (0, 0, 255), thickness=2)  
i = 0
for face in faces:
   i = i + 1
   save = img[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]
   cv2.imwrite('faces/%s.jpg' % i, save)
cv2.imshow('1',imgWithRect)
cv2.waitKey(0)    