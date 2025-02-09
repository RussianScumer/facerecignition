from FaceDetector import FaceDetector
import utils
from FaceAligner import FaceAligner

detector = FaceDetector("best.pt", "3.jpg")
detector.detect_faces()
utils.clear_dir("faces/")
utils.clear_dir("alignedfaces/")
detector.save_faces()
print("Number of detections:", detector.detections_count)
aligner = FaceAligner()
aligner.face_align()
aligner.save_aligned_faces()
