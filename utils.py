import os

def clear_dir(path = ""):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        os.unlink(file_path)