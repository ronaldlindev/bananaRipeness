
import tensorflow as tf
import numpy as np
import os
import time


def process(fileName): # turns image into a np array
    startTime = time.time()

    image = tf.io.read_file(fileName)  # Read the image file
    image = tf.image.decode_image(image, channels=3)  # Decode the image
    image = tf.image.resize(image, size = (200,100))  # Resize the image
    print(image.shape)
    print(f'finished {fileName} in {time.time() - startTime}')
    return image

