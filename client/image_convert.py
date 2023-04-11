# This module is responsible for converting the images to a string
# The string then gets send to the DjangoRest server

# Import Libraries
import requests
import base64


class SendImages():

    def image_convert(files, input_dir):
        """
        This function converts the images in the "input" folder into a string
        """
        # Create an empty list to store converted files
        convert_files = []

        # Iterate through the files and store them as string
        for file in files:
            with open(input_dir + file, "rb") as image_file:
                convert_files.append(base64.b64encode(image_file.read()))

        return convert_files

    def send_string_to_api(convert_files):
        """
        This function takes the (image) strings from the list and sends them to the server
        """
        index_list = []
        for convert_file in convert_files:
            url = 'http://localhost:8000/api/'
            data = {'text': convert_file}
            response = requests.post(url, data=data)
            if response.status_code == 200:
                result = response.json()
                print(result)
                index_list.append(result)

        return index_list
