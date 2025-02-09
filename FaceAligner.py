import cv2
import os
import utils
import dlib
import math
import numpy as np

class FaceAligner:
    def __init__(self, model_path: str = "shape_predictor_68_face_landmarks.dat", faces_path: str = 'faces', output_dir: str = 'alignedfaces'):
        self.model_path = model_path
        self.faces_path = faces_path
        self.output_dir = output_dir
        self.faces = []
        self.predictor = dlib.shape_predictor(model_path)
        self.aligned_faces = []
        utils.create_path(self.output_dir)
        for filename in os.listdir(faces_path):
            self.faces.append(cv2.imread(os.path.join(faces_path, filename)))

    def face_align(self):
        for face in self.faces:
            height, width = face.shape[:2]
            face_rect = dlib.rectangle(0, 0, width, height)
            landmarks = self.predictor(face, face_rect)
            left_eye_center = ((landmarks.part(36).x + landmarks.part(39).x) // 2, (landmarks.part(36).y + landmarks.part(39).y) // 2)
            right_eye_center = ((landmarks.part(42).x + landmarks.part(45).x) // 2, (landmarks.part(42).y + landmarks.part(45).y) // 2)
            dy = right_eye_center[1] - left_eye_center[1]
            dx = right_eye_center[0] - left_eye_center[0]
            angle = math.degrees(math.atan2(dy, dx)) 
            center = (np.float32(left_eye_center[0]), np.float32(left_eye_center[1]))
            h, w = face.shape[:2]
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            aligned_img = cv2.warpAffine(face, M, (w, h))
            self.aligned_faces.append(aligned_img)
    def save_aligned_faces(self):
        i = 0
        for face in self.aligned_faces:
            i = i + 1
            cv2.imwrite(f'{self.output_dir}/{i}.jpg', face)