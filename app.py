import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os
from parsing import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if 'filename' in request.files:
        file = request.files['filename']
        if file.filename != '':
            file_path = os.path.join('upload', file.filename)
            file.save(file_path)
    # file_name = request.files
    # file_name = file_name.file
    # return request.files['filename'].filename
    # print(file_name)
    data = main(file_path)
    # print(data)
    if 'Exception' in data:
        return render_template('error_show.html', error=data)
    else:
        return render_template('resume.html', data_dict=data)
    # return render_template('resume.html')


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = 8080)

# if __name__ == "__main__":
#     app.run(debug=True)
