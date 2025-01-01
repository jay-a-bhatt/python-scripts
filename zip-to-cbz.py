"""
Script to make a .zip file into a .cbz file (essentially renaming)

Needs an 'input' folder in the same dir. as the script for input
Will output into a folder called 'output'
"""

import os

def rename_and_move_zip_to_cbz(input_directory, export_directory):
    if not os.path.exists(input_directory):
        print(f"Input directory {input_directory} does not exist.")
        return

    if not os.path.exists(export_directory):
        os.makedirs(export_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.zip'):
            new_filename = filename.replace('.zip', '.cbz')
            old_file = os.path.join(input_directory, filename)
            new_file = os.path.join(export_directory, new_filename)
            os.rename(old_file, new_file)
            print(f"Moved and renamed {filename} to {new_filename} in the export directory")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    input_directory = os.path.join(script_dir, "input")
    export_directory = os.path.join(script_dir, "export")
    
    rename_and_move_zip_to_cbz(input_directory, export_directory)

if __name__ == "__main__":
    main()
