import tensorflow as tf
import os
import pandas as pd
from matplotlib import pyplot as plt

# Load the model

model = tf.keras.models.load_model('/Users/srivanthdoddala/Downloads/my_model')

def preprocess_image(image):
    # Example preprocessing steps, adjust according to your model's requirements
    image = image.resize((224, 224))  # Resize image to the size your model expects
    image = np.array(image) / 255.0   # Normalize the image to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def predict(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    return predictions
