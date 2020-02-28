from __future__ import absolute_import
import pickle
import json
import pandas as pd
import numpy as np
from optparse import OptionParser
import time
import textract as tx
import tensorflow_hub as hub
import tensorflow as tf
import sys
from numba import jit, cuda


from .ner_parsing_resume import ner_parsing_data

ner_max_len = 20
ner_split = 20
ner_batch_size = 32
@jit
def ner_32_dim_matrix(padd_to_2d):

    for i in range(int(32 - int(len(padd_to_2d)%32))):
        padd_to_2d.append(["__PAD__" for i in range(ner_max_len)])

    return padd_to_2d

def ner_padding_padd(padd_to_2d):
    new_X = []
    for seq in padd_to_2d:
      new_seq = []
      for i in range(ner_max_len):
          try:
              new_seq.append(seq[i])
          except:
              new_seq.append("__PAD__")
      new_X.append(new_seq)
    return new_X

def ner_to_matrix(padd):
    return [padd[i:i+ner_split] for i in range(0, len(padd), ner_split)]

def ner_pre_processing(ner_filepath):
    extension = ner_filepath.split('.')
    if 'pdf' in extension or 'doc' in extension or 'docx' in extension:
        text = tx.process(ner_filepath, method="pdftotext").decode('utf-8')
        text = text.replace('\n',' ').replace('\r',' ').replace('\t',' ')
        text = text.replace('  ',' ')
        padd_to_2d_text = list(ner_to_matrix(text.split()))
        padd_to_2d_text = ner_padding_padd(padd_to_2d_text)
        padd_to_2d_text = ner_32_dim_matrix(padd_to_2d_text)
        return padd_to_2d_text
    else:
        return 'file should be in .pdf or doc form'

def ner_read_model():
    try:
        # print(absolute_import, sys.path[0]+"\\ner_data\\ner_model\\ner_model.pickle")
        pickle_in = open(sys.path[0]+"/ner_data/ner_model/ner_model.pickle","rb")
        ner_model = pickle.load(pickle_in)
        pickle_in.close()
        return ner_model
    except FileNotFoundError as e:
        print("File Not Found Error : "+str(e))
        return "File Not Found Error"

def ner_model_prediction(ner_filepath):
    # print("ner file path",ner_filepath)
    try:
        padd_to_2d_text = ner_pre_processing(ner_filepath)
    except Exception as e:
        return "Data Error : "+str(e)
    try:
        model = ner_read_model()
        if model == "File Not Found Error":
            return "File Not Found Error"
        print(np.array(padd_to_2d_text).shape)
        prediction = model.predict(np.array(padd_to_2d_text))
        prediction = np.argmax(prediction, axis=-1)

        return ner_parsing_data(prediction, padd_to_2d_text)
    except Exception as e:
        # print("Session Error" , e)
        return "Session Error : "+str(e)
