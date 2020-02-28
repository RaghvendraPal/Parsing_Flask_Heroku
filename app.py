import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os
# from parsing import main

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if 'filename' in request.files:
        photo = request.files['filename']
        if photo.filename != '':
            photo.save(os.path.join('upload', photo.filename))
    # file_name = request.files
    # file_name = file_name.file
    return request.files['filename'].filename
    # print(file_name)
    # data_dict = main(file_name)
    # print(data_dict)
    # return render_template('resume.html', prediction_text=file_name)


if __name__ == "__main__":
    app.run(debug=True)
