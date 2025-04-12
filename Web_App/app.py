from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import logging

app = Flask(__name__)

# Load the No_Feature.h5 model
model = tf.keras.models.load_model('No_Feature.h5', compile=False)

# Define a function to preprocess the input image
def preprocess_image(image):
    # Resize the image to the expected input size of the model
    image = tf.image.resize(image, (256, 256))
    # Convert the image to a NumPy array and normalize its pixel values
    image = np.array(image) / 255.0
    # Add an extra dimension to the array to match the model's input shape
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def home():
    return render_template('TTS.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image file from the form data
    image_file = request.files['image']
    # Read the image file into a TensorFlow tensor
    image = tf.image.decode_image(image_file.read(), channels=3)
    # Preprocess the input image
    preprocessed_image = preprocess_image(image)
    # Use the model to make predictions
    predictions = model.predict(preprocessed_image)
    # TODO: Process the predictions and prepare the data to be passed to the HTML file
    # Render the HTML file with the predicted results
    return render_template('results.html', predictions=predictions)


if __name__ == '__main__':
    app.run()
