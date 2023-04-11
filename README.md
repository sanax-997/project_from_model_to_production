# Project: From Model To Production - Image classification for a refund department

## Overview
'Image classification for a refund department' is a web application consisting of a client and a server, which hosts a machine learning model for image classification. The software automatically classifies refund items into categories based on pictures of the items. The system consists overall of 3 working parts. The first component is the client, which is a Python script containing multiple classes, each responsible for a different action and a folder containing the refunded images. These images are then sent via HTTP requests in a string format. On the receiving end and as the second component we have a web application based on Django. The web application features an API endpoint for receiving the string data, a function to convert the data back to an image and a machine learning model for image classification. 

## Machine Learning model
The machine learning model must be downloaded sperately, since the filesize is too large for github.
Open the following link to download the model: https://drive.google.com/file/d/1dg5jWr1rDT4tSJDMEpY_qN2SPv_wFucV/view?usp=sharing
The donwloaded model must be copied back intot the folder structure.
1. Open the server directory
2. Open the classifier directory
2. Open the api directory
4. Paste the model inside the directory

## Installation
There are two seperate installation processes, one for the server and one for the client.

### Server
1. Download the application from Github and extract the contents
2. If you do not have `pipenv` already installed. Open a code command prompt or terminal in the extracted folder and install `pipenv` with the command `pip install pipenv`
3. Then execute the command `pipenv install`. This installs all the dependencies needed for the program
4. Execute the command `pipenv shell` to open a new virtual environment
5. Change the directory to `classifier` with the command `cd classifier`
6. Execute the command `py manage.py runserver` to launch the server

### Client
1. Download the application from Github and extract the contents
2. If you do not have `pipenv` already installed. Open a code command prompt or terminal in the extracted folder and install `pipenv` with the command `pip install pipenv`
3. Then execute the command `pipenv install`. This installs all the dependencies needed for the program
4. Execute the command `pipenv shell` to open a new virtual environment

## Usage
To use the application follow the steps:
1. Ensure that there are images in the "input" folder. The program should already contain files in the input folder. If the image files are not there or you already tested the application but want to test it again, the folder test_images contains 8 images, two for each category. Copy the contents to the "input" folder.
2. In the client application execute the command `py main.py`.

## Requirements
Python Version 3.9.0

## License
GPL-3.0 License
