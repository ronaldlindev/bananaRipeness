from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
# from tensorflow import keras
# from util.imageProcessing import process 
import json 




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    print("cum")
    request
   
    return jsonify({"class" : 1})
    
         
   
  