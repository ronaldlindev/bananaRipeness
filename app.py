from flask import Flask, render_template, request, jsonify
import io, base64
import tensorflow as tf
import numpy as np
from tensorflow import keras
from util.imageProcessing import process 
import json 

MODEL_PATH = r'models/model1'

model = tf.keras.models.load_model(MODEL_PATH)

app = Flask(__name__)


@app.route('/', methods=['POST'])
def predict():
    base64_str = json.loads((request.get_data()))["imageData"]
    print("base64 loaded")
    image = base64.b64decode(base64_str[23:], validate=True)
    print("decoded")
    file = "my_image.jpg"
    with open(file, "wb") as f:
        f.write(image)
        print("file written")
        file = np.array([process(file)])
        print(file.shape)
        prediction = model.predict(file)
        print(prediction)
        prediction = np.argmax(prediction[0])
        response = jsonify({"class" : int(prediction)})
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response
         
   
  