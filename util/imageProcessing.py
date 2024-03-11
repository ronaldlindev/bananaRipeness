
import tensorflow as tf
import numpy as np
import os
import time


def process(image): # turns image into a np array

    # image = tf.io.read_file(fileName)  # Read the image file
    # image = tf.image.decode_image(image, channels=3)  # Decode the image
    image = tf.convert_to_tensor(image)
    print(tf.shape(image))
    image = tf.image.resize(image, size = (200,100))  # Resize the image
    return image

