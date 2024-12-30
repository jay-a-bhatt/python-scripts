import os

def rename_and_move_zip_to_cbz(input_directory, export_directory):
    # Ensure the input directory exists
    if not os.path.exists(input_directory):
        print(f"Input directory {input_directory} does not exist.")
        return

    # Ensure the export directory exists or create it if it doesn't
    if not os.path.exists(export_directory):
        os.makedirs(export_directory)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a .zip file
        if filename.endswith('.zip'):
            # Create the new filename by replacing .zip with .cbz
            new_filename = filename.replace('.zip', '.cbz')
            # Build the full file paths
            old_file = os.path.join(input_directory, filename)
            new_file = os.path.join(export_directory, new_filename)
            # Move and rename the file to the export directory
            os.rename(old_file, new_file)
            print(f"Moved and renamed {filename} to {new_filename} in the export directory")

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Detect the operating system
    input_directory = os.path.join(script_dir, "input")  # Use script directory with subdirectory "input"
    export_directory = os.path.join(script_dir, "export")  # Use script directory with subdirectory "export"
    
    # Call the function to rename and move files to the export directory
    rename_and_move_zip_to_cbz(input_directory, export_directory)

if __name__ == "__main__":
    main()
