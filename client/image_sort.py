import os
import shutil
import datetime


class SortImages():

    def sort(files, input_dir, output_dir, index_list, folders):
        counter = 0
        for index in index_list:
            for folder in folders:
                if str(index) == folder[0]:

                    # List all the files in the destination folder
                    dest_path = os.path.join(output_dir, folder)
                    dest_files = os.listdir(dest_path)

                    # count number of files in folder
                    num_files = len(dest_files)
                    # increment number by 1
                    num_files += 1

                    # get current date
                    today = datetime.datetime.now().date()

                    # get category name from folder path
                    category_name = folder.split("_")[1]

                    # Create the paths from the source folder to the destination folder
                    src_file = os.path.join(input_dir, files[counter])
                    dest_file = os.path.join(dest_path, files[counter])

                    # move the file to the destination directory
                    shutil.move(src_file, dest_file)

                    # create new file name with number and date
                    new_file_name = f"{num_files}_{category_name}_{today.strftime('%Y_%m_%d')}.png"

                    # rename file
                    os.rename(dest_file,
                              os.path.join(dest_path, new_file_name))

                    counter = counter + 1
