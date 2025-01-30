import cv2
import os
import numpy as np
import math

if os.path.isdir('alignedfaces') == 0:  
    os.mkdir('alignedfaces')
i = 0
faces = []
for filename in os.listdir('faces'):
    faces.append(cv2.imread(os.path.join('faces', filename)))
    print(filename)  
eye_detector = cv2.CascadeClassifier('.venv/lib/python3.12/site-packages/cv2/data/haarcascade_eye.xml')
eyes = eye_detector.detectMultiScale(faces[11], 1.1, 4)
sorted_eyes = sorted(eyes, key=lambda e: e[0])[:2]
left_eye, right_eye = sorted_eyes[0], sorted_eyes[1]

left_eye_center = (left_eye[0] + left_eye[2] // 2, left_eye[1] + left_eye[3] // 2)
right_eye_center = (right_eye[0] + right_eye[2] // 2, right_eye[1] + right_eye[3] // 2)

dy = right_eye_center[1] - left_eye_center[1]
dx = right_eye_center[0] - left_eye_center[0]
angle = math.degrees(math.atan2(dy, dx))
center = (np.float32(left_eye_center[0]), np.float32(left_eye_center[1]))

h, w = faces[11].shape[:2]
M = cv2.getRotationMatrix2D(center, angle, 1.0)
aligned_img = cv2.warpAffine(faces[11], M, (w, h))

print(eyes)
cv2.imshow('1', faces[11])
cv2.imshow('2', aligned_img)
cv2.waitKey(0)
'''for face in faces:
    i = i + 1
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    landmarks = predictor(gray)

        # Извлечем ключевые точки
    points = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(68)])

        # Определим точки для выравнивания
    left_eye = points[36:42].mean(axis=0)
    right_eye = points[42:48].mean(axis=0)

    dy = right_eye[1] - left_eye[1]
    dx = right_eye[0] - left_eye[0]
    angle = np.arctan2(dy, dx) * 180.0 / np.pi

    # Выравнивание
    h, w = face.shape[:2]
    center = (w // 2, h // 2)
        
    M = cv2.getRotationMatrix2D(center, angle, scale=1.0)
    aligned = cv2.warpAffine(face, M, (w, h))
    cv2.imwrite('faces/%s.jpg' % i, aligned)'''

