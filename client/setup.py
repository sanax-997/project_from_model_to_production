# This module is to configure the input and output folders
import os


class Setup():
    # Choose directory for input files
    input_dir = os.path.join(os.getcwd(), 'input\\')
    # Choose directory for output files
    output_dir = os.path.join(os.getcwd(), 'output\\')

    # Store all filenames in a list
    files = os.listdir(input_dir)
    # Store all folder names in a list
    folders = []
    for entry in os.scandir(output_dir):
        if entry.is_dir():
            folders.append(entry.name)

    # Create a list to store the responses
    index_list = []

    def cleanup(folder_path):
        # iterate through all the subfolders of the folder
        for root, dirs, files in os.walk(folder_path):
            # iterate through all the files in each subfolder
            for file in files:
                # delete the file
                os.remove(os.path.join(root, file))
