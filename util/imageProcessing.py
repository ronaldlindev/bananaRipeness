
import tensorflow as tf
import numpy as np
import os
import time
pathToImage = r'C:\Users\YouConfusedYet\Downloads\archive\banana-ripening-dataset.coco\Banco de dados de graus de maturacao de bananas.v2-data-set-maturacao2023-03-17.coco\labeled banana images\\'


def process(fileName): # turns image into a np array
    startTime = time.time()

    image = tf.io.read_file(pathToImage + fileName)  # Read the image file
    image = tf.image.decode_image(image, channels=3)  # Decode the image
    image = tf.image.resize(image, size = (20,10))  # Resize the image
    print(f'finished {fileName} at {time.time() - startTime}')
    return image

