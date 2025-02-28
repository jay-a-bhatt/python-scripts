import os
import shutil

def flatten_directory(input_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if root != input_dir: # Ensure we don't move files that are already in the input directory
                shutil.move(file_path, input_dir)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            # Remove the now empty directories
            if os.path.isdir(dir_path) and not os.listdir(dir_path):
                os.rmdir(dir_path)

if __name__ == "__main__":
    input_directory = "input/"
    flatten_directory(input_directory)
