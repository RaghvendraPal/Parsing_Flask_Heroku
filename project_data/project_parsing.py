from __future__ import absolute_import
import pickle
import json
import pandas as pd
import numpy as np
import time
import sys
import textract as tx
import tensorflow_hub as hub
import tensorflow as tf
import re
from numba import jit, cuda

from .project_parsing_resume import project_parsing_data


project_max_len = 400
project_batch_size = 32
@jit
def decontracted(phrase):
    # specific
    phrase = re.sub(r"\u25cf", "", phrase)
    phrase = re.sub(r"\u00a0", "", phrase)
    phrase = re.sub(r"\xa0", "", phrase)
    # general \u200
    phrase = re.sub(r"\x0c", "", phrase)
    phrase = re.sub(r"\u200b", "", phrase)

    return phrase


def project_32_dim_matrix(padd_to_2d):
    test = []
    test.append(padd_to_2d)
    for seq in range(int(31)):
        new_seq = []
        for i in range(project_max_len):
          new_seq.append("__PAD__")
        test.append(new_seq)
    return test

def project_sentence_padd(text):
    j = 0
    length = project_max_len - len(text)
    if len(text) < project_max_len:
      while(j<length):
        text.append('__PAD__')
        j+=1
    else:
        text = text[:project_max_len]
    return text

def project_pre_processing(project_filepath):
    extension = project_filepath.split('.')
    if 'pdf' in extension or 'doc' in extension or 'docx' in extension:
        text = tx.process(project_filepath, method="pdftotext").decode('utf-8')
        text = text.split('\n')
        text = [decontracted(i) for i in text if decontracted(i) and i!= ' ']
        padd_to_2d_text = project_sentence_padd(text)
        padd_to_2d_text = project_32_dim_matrix(padd_to_2d_text)
        return padd_to_2d_text
    else:
        return 'file should be in .pdf or doc form'

def project_read_model():
    try:
        pickle_in = open(sys.path[0]+"/project_data/project_model/project_model.pickle","rb")
        project_model = pickle.load(pickle_in)
        pickle_in.close()
        return project_model
    except FileNotFoundError as e:
        print("File Not Found Error : "+str(e))
        return "File Not Found Error"

def project_model_prediction(project_filepath):
    # print("project file path",project_filepath)
    try:
        padd_to_2d_text = project_pre_processing(project_filepath)
    except Exception as e:
        return "Data Error : "+str(e)
    try:
        model = project_read_model()
        if model == "File Not Found Error":
            return "File Not Found Error"
        print(np.array(padd_to_2d_text).shape)
        prediction = model.predict(np.array(padd_to_2d_text))
        prediction = np.argmax(prediction, axis=-1)
        return project_parsing_data(prediction, padd_to_2d_text)
    except Exception as e:
        # print("Session Error" , e)
        return "Session Error : "+str(e)
