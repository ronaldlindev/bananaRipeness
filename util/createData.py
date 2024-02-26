import csv
import json
from imageProcessing import process

import random
import numpy as np
import os

f = open(r"C:\Users\YouConfusedYet\Downloads\archive\banana-ripening-dataset.coco\Banco de dados de graus de maturacao de bananas.v2-data-set-maturacao2023-03-17.coco\labeled banana images\_annotations.coco.json")

data = json.load(f) ## has info liscences, categories, images, annotations

idToImage = {ele['id'] : ele['file_name'] for ele in data['images']}
idToLabel = {ele['id'] : ele['category_id'] for ele in data['annotations']}

print(data["annotations"][1])

s = set()
for ele in idToLabel:
    if idToLabel[ele] not in s:
        s.add(idToLabel[ele])

print(s)
