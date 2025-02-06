import cv2
import os
from ultralytics import YOLO
import utils
import dlib

class FaceDetector:
    def __init__(self, model_path: str, image_path: str, output_dir: str = 'faces'):
        self.model = YOLO(model_path)
        self.image_path = image_path
        self.output_dir = output_dir
        self.image = cv2.imread(image_path)
        
        try:
            self.image_with_rectangles = self.image.copy()
        except NameError:
            print(NameError) 

        self.detections = []

        utils.clear_dir(self.output_dir)

    @property
    def detections_count(self) -> int:
        return len(self.detections)

    def detect_faces(self):
        results = self.model([self.image_path], conf = 0.3)
        self.detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                self.detections.append((x1, y1, x2, y2))
                cv2.rectangle(self.image_with_rectangles, (x1, y1), (x2, y2), (0, 0, 255), thickness=2)

    def save_faces(self):
        for i, (x1, y1, x2, y2) in enumerate(self.detections, start=1):
            face_image = self.image[y1:y2, x1:x2]
            cv2.imwrite(f'{self.output_dir}/{i}.jpg', face_image)
