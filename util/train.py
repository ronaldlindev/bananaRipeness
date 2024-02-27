import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import random
from imageProcessing import process
import datetime
import json
import numpy as np
import os
os.chdir(r'C:\Users\YouConfusedYet\Desktop\bananaRipeness\util\data')
train_images = np.load('train_images.npy')
train_labels = np.load('train_labels.npy')

test_images = np.load('test_images.npy')
test_labels = np.load('test_labels.npy')

validation_images = np.load('validation_images.npy')
validation_labels = np.load('validation_labels.npy')


model = models.Sequential()
model.add(layers.Rescaling(1./255, input_shape=(200, 100, 3)))
model.add(layers.Conv2D(16, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((4, 4)))
model.add(layers.Flatten())
model.add(layers.Dense(30, activation='relu'))
model.add(layers.Dense(4))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
log_dir = "util/logs/fit/"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels),
                    callbacks=[tensorboard_callback], batch_size = 32, shuffle = True)


test_loss, test_acc = model.evaluate(validation_images,  validation_labels, batch_size = 32, verbose=2)

os.chdir(r'C:\Users\YouConfusedYet\Desktop\bananaRipeness')

model.save('models/model1')
print(f'validation loss: {test_loss}, validation accuracy: {test_acc}')
