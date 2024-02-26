import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import random
from imageProcessing import process
import datetime
import json
import numpy as np
f = open(r"C:\Users\YouConfusedYet\Downloads\archive\banana-ripening-dataset.coco\Banco de dados de graus de maturacao de bananas.v2-data-set-maturacao2023-03-17.coco\labeled banana images\_annotations.coco.json")

data = json.load(f) ## has info liscences, categories, images, annotations

idToImage = {ele['id'] : ele['file_name'] for ele in data['images']}
idToLabel = {ele['id'] : ele['category_id'] for ele in data['annotations']}

numbers = list(range(1000))
random.shuffle(numbers)
conversion = {1 : 1, 2 : 1, 3 : 2, 4 : 2, 5 : 3 , 6 : 3, 7 : 4, 8: 4 }

validation_images = np.array([process(idToImage[ele]) for ele in numbers[900:999]])
validation_labels = np.array([conversion[idToLabel[ele]] for ele in numbers[900:999]])
test_images = np.array([process(idToImage[ele]) for ele in numbers[750:899]])
test_labels = np.array([conversion[idToLabel[ele]] for ele in numbers[750:899]])
train_images = np.array([process(idToImage[ele]) for ele in numbers[:749]])
train_labels = np.array([conversion[idToLabel[ele]] for ele in numbers[:749]])

model = models.Sequential()
model.add(layers.Rescaling(1./255, input_shape=(20, 10, 3)))
model.add(layers.Conv2D(16, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(2, activation='relu'))
model.add(layers.Dense(4))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
log_dir = "util/logs/fit/"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

history = model.fit(train_images, train_labels, epochs=20, 
                    validation_data=(test_images, test_labels),
                    callbacks=[tensorboard_callback], batch_size = 32)


test_loss, test_acc = model.evaluate(validation_images,  validation_labels, batch_size = 32, verbose=2)

model.save('models/model1')
print(f'validation loss: {test_loss}, validation accuracy: {test_acc}')
