import cv2
import os
import utils
import dlib

class FaceAligner:
    def __init__(self, model_path: str, faces_path: str = 'faces', output_dir: str = 'alignedfaces'):
        self.model_path = model_path
        self.faces_path = faces_path
        self.output_dir = output_dir
        self.faces = []
        self.predictor = dlib.shape_predictor(model_path)
        utils.create_path(self.output_dir)
        for filename in os.listdir(faces_path):
            self.faces.append(cv2.imread(os.path.join(faces_path, filename)))

    def face_align(self):
        for face in self.faces:
