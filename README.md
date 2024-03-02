# Banana Ripeness Classification 

This project demonstrates a fruit ripeness classification system, specifically focusing on bananas. It utilizes:

TensorFlow: A machine learning library for creating the classification model.
Flask: A lightweight web framework for building the REST API.
HTML & CSS: For developing the user interface to interact with the API.

## Project Overview

This project aims to classify the ripeness of a banana based on an image. The user interacts through a web interface, uploads an image of a banana, and receives the predicted ripeness category (e.g., unripe, ripe, overripe, and rotten).

## Installation 

Clone the repository
``` 
git clone https://github.com/RonaldLinDev/bananaRipeness
```
Install dependencies 
```
pip install -r requirements.txt
```
Run the Server Locally
```
flask run
```

## Usage 

The web application will ask for access to the user's webcam. Centering an image of a banana on the webcam and clicking 'Capture' will cause the model to output its perdicted ripeness classification.


(Hosted server for the web service has been discontinued due to server costs)
Previously hosted here: https://bananaripeness.onrender.com 

