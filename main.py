from FaceDetector import FaceDetector
import utils

detector = FaceDetector("best.pt", "3.jpg")
detector.detect_faces()
utils.clear_dir("faces/")
detector.save_faces()
utils.show_image(detector.image_with_rectangles)
print("Number of detections:", detector.detections_count)