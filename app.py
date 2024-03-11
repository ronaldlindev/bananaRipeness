from flask import Flask, render_template, request, jsonify
import io, base64
import tensorflow as tf
import numpy as np
from tensorflow import keras
from util.imageProcessing import process 
from flask_cors import CORS, cross_origin
import json 

MODEL_PATH = r'models/model1'

model = tf.keras.models.load_model(MODEL_PATH)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/home')
def render_home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    base64_str = json.loads((request.get_data()))["imageData"]
    image = base64.b64decode(base64_str[23:], validate=True)
    file = np.array([process(image)])
    prediction = model.predict(file)
    prediction = np.argmax(prediction[0])
    response = jsonify({"class" : int(prediction)})
    return response
         
   
  