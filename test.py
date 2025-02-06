import dlib
import cv2
import math 
import numpy as np

predictor =  dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face = cv2.imread('8.jpg')
height, width = face.shape[:2]
face_rect = dlib.rectangle(0, 0, width, height)
landmarks = predictor(face, face_rect)

left_eye_center = ((landmarks.part(36).x + landmarks.part(39).x) // 2, (landmarks.part(36).y + landmarks.part(39).y) // 2)
right_eye_center = ((landmarks.part(42).x + landmarks.part(45).x) // 2, (landmarks.part(42).y + landmarks.part(45).y) // 2)
cv2.circle(face, (left_eye_center[0], left_eye_center[1]), 2, (0, 255, 0), -1)  
cv2.circle(face, (right_eye_center[0], right_eye_center[1]), 2, (0, 255, 0), -1)  
dy = right_eye_center[1] - left_eye_center[1]
dx = right_eye_center[0] - left_eye_center[0]
angle = math.degrees(math.atan2(dy, dx)) 
center = (np.float32(left_eye_center[0]), np.float32(left_eye_center[1]))

h, w = face.shape[:2]
M = cv2.getRotationMatrix2D(center, angle, 1.0)
aligned_img = cv2.warpAffine(face, M, (w, h))
# Display the image with landmarks
cv2.imshow('Landmarks', aligned_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
