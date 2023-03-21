from flask import Flask, jsonify, request,json
from flask_cors import CORS

import cv2 as cv

from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
import io
from keras.models import load_model  
  

app = Flask(__name__)
CORS(app)
  
@app.route('/temp', methods = ['GET'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})
  
  

@app.route('/algo', methods = ['POST'])
def disp():
    
    
    # this for postman
    # filestr = request.files['myFile'].read() 
    # print(filestr)
    # file_bytes = np.fromstring(filestr, np.uint8)

    # img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    # print(img.shape)
    
    
    #This is for browserbase64
    
    recievedImage =  request.form.get('myFile')
    
    # base64_decoded = base64.b64decode(recievedImage)
    # print(base64_decoded)
    # print(file_bytes.shape)
    # img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    # print(img)
    # file_bytes = np.fromstring(recievedImage, np.uint8)
    # # print(type(recievedImage))
    # image = Image.open(io.BytesIO(file_bytes))
    # image_np = np.array(image)
    # print(image_np)
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(recievedImage, "utf-8"))))
    img.save('my-image.png')
    img = cv.imread("my-image.png")
   
    print(img.shape)
    
    
    
    
    # #interesting Part
    
    modelTest = load_model("angryHappySadModel.h5")
    resize = tf.image.resize(img,(256,256))
    yhat = modelTest.predict(np.expand_dims(resize/255,0))
    print(yhat)
    #0 for angry 1 for happy and 2 for sad (index)
    print(yhat.argmax())
    emotion=""
    if yhat.argmax() == 0:
        emotion = "angry"
    elif yhat.argmax() == 1:
        emotion = "happy"
    else:
        emotion = "sad"    
        
    
    return jsonify({'data': emotion})



  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)