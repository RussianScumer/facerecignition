import os
import cv2
def clear_dir(path = ""):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        os.unlink(file_path)

def create_path(path = ""):
    if os.path.isdir(path) == 0:
        os.mkdir(path)

def show_image(image):
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()