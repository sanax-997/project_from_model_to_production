from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.base import ContentFile
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import base64
import keras.models
import numpy as np
import os
from django.http import HttpResponse
import cv2


class Predict(APIView):

    def post(self, request, format=None):

        # Retrieve the Base64 encoded image data from the POST request
        encoded_image_data = request.POST.get('text')

        # Decode the Base64 encoded image data
        decoded_image = base64.b64decode(encoded_image_data)

        # generate a unique filename for the image
        filename = 'image.png'

        # Save the image file to disk
        with open(filename, 'wb') as f:
            f.write(decoded_image)

        # Convert the image to the specified format, which is needed for the ML model
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

        # Convert the image to the ML fileformat
        img = cv2.resize(img, (28, 28))

        # Convert the image to the ML fileformat
        img = cv2.resize(img, (224, 224))

        # Apply binary inversion to the image
        img = cv2.bitwise_not(img)

        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        # save preprocessed image
        cv2.imwrite("preprocessed_image.jpg", img)

        img = np.expand_dims(img, axis=0)

        # Delete the original file
        os.remove(filename)

        # Get the absolute path to the current directory
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Load the Keras machine learning model from file
        model_path = os.path.join(dir_path, 'product_classifier.h5')
        model = keras.models.load_model(model_path)

        # Preprocess the image for the mobilenetv2 model
        img = preprocess_input(img)

        # Use the model to make predictions on the input image
        predictions = model.predict(img)

        # Return the index of the most probable class
        predictions = np.argmax(predictions, axis=1)

        # Send the index as response to the client
        return HttpResponse(predictions)
