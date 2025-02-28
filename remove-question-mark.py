import os
import shutil

def remove_question_marks():
    input_dir = os.path.join(os.getcwd(), 'input')
    output_dir = os.path.join(os.getcwd(), 'output')

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            new_filename = filename.replace('?', '')
            old_filepath = os.path.join(root, filename)
            new_filepath = os.path.join(output_dir, new_filename)
            shutil.move(old_filepath, new_filepath)

if __name__ == "__main__":
    remove_question_marks()
