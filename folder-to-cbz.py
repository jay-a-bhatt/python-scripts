import os
import zipfile

def compress_images_to_cbz(input_directory, export_directory):
    # Ensure the input directory exists
    if not os.path.exists(input_directory):
        print(f"Input directory {input_directory} does not exist.")
        return

    # Ensure the export directory exists or create it if it doesn't
    if not os.path.exists(export_directory):
        os.makedirs(export_directory)

    # Iterate through all folders in the input directory
    for foldername in os.listdir(input_directory):
        folder_path = os.path.join(input_directory, foldername)
        
        if os.path.isdir(folder_path):
            # Check if the folder contains only image files
            valid_extensions = ['.jpg', '.jpeg', '.png']
            for filename in os.listdir(folder_path):
                if not any(filename.lower().endswith(ext) for ext in valid_extensions):
                    print(f"Error: {foldername} contains non-image files.")
                    return
            
            # Compress the images into a zip file with no compression
            cbz_filename = os.path.join(export_directory, f"{foldername}.cbz")
            with zipfile.ZipFile(cbz_filename, 'w', zipfile.ZIP_STORED) as zipf:
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)
                    zipf.write(file_path, arcname=filename)
            
            print(f"Compressed and renamed folder {foldername} to {foldername}.cbz in the export directory")

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    input_directory = os.path.join(script_dir, "input")  # Use script directory with subdirectory "input"
    export_directory = os.path.join(script_dir, "export")  # Use script directory with subdirectory "export"
    
    # Call the function to compress images and rename files
    compress_images_to_cbz(input_directory, export_directory)

if __name__ == "__main__":
    main()
