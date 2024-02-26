import csv
import json
from imageProcessing import process

import random
import numpy as np
import os
os.chdir(r'C:\Users\YouConfusedYet\Desktop\bananaRipeness')
path = 'util/data/test/'
# train
images = []
labels = [] 
for fileName in os.listdir(path + r"unripe/"):
    images.append(process(path + r'unripe/' + fileName))
    labels.append(0)

for fileName in os.listdir(path + r"ripe/"):
    images.append(process(path + r'ripe/' + fileName))
    labels.append(1)

for fileName in os.listdir(path + r"overripe/"):
    images.append(process(path + r'overripe/' + fileName))
    labels.append(2)

for fileName in os.listdir(path + r"rotten/"):
    images.append(process(path + r'rotten/' + fileName))
    labels.append(3)
images = np.array(images)
labels = np.array(labels)
os.chdir(r'C:\Users\YouConfusedYet\Desktop\bananaRipeness\util\data')

np.save("test_images.npy", images)
np.save("test_labels.npy", labels)