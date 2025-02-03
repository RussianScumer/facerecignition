import cv2
import os
from ultralytics import YOLO 
import numpy as np

model = YOLO("yolov11n-face.pt")
img = cv2.imread('3.jpg')
imgWithRect = cv2.imread('3.jpg')
if os.path.isdir('faces') == 0: 
    os.mkdir('faces')

i = 0
results = model(["3.jpg"])
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        print(x1, y1, x2, y2)
        cv2.rectangle(imgWithRect,(x1, y1), (x2, y2), (0, 0, 255), thickness=2) 
        save = img[y1:y2, x1:x2]
        i = i + 1
        cv2.imwrite('faces/%s.jpg' % i, save)
cv2.imshow('1', imgWithRect)
cv2.waitKey(0)
    