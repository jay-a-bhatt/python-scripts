"""
Script to turn a folder of images (.jpg, .jpeg, .png) into a .cbz file

Needs an 'input' folder in the same dir. as the script for input
Will output into a folder called 'output'
"""

import os
import zipfile

def compress_images_to_cbz(input_directory, export_directory):
    if not os.path.exists(input_directory):
        print(f"Input directory {input_directory} does not exist.")
        return

    if not os.path.exists(export_directory):
        os.makedirs(export_directory)

    for foldername in os.listdir(input_directory):
        folder_path = os.path.join(input_directory, foldername)
        
        if os.path.isdir(folder_path):
            valid_extensions = ['.jpg', '.jpeg', '.png']
            for filename in os.listdir(folder_path):
                if not any(filename.lower().endswith(ext) for ext in valid_extensions):
                    print(f"Error: {foldername} contains non-image files.")
                    return
            
            cbz_filename = os.path.join(export_directory, f"{foldername}.cbz")
            with zipfile.ZipFile(cbz_filename, 'w', zipfile.ZIP_STORED) as zipf:
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)
                    zipf.write(file_path, arcname=filename)
            
            print(f"Compressed and renamed folder {foldername} to {foldername}.cbz in the export directory")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    input_directory = os.path.join(script_dir, "input")
    export_directory = os.path.join(script_dir, "export")
    
    compress_images_to_cbz(input_directory, export_directory)

if __name__ == "__main__":
    main()
