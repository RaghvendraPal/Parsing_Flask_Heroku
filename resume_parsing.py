# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:32:52 2020

@author: RAGHVENDRA PAL
"""



# import sys
import pickle
import json
import pandas as pd
import numpy as np
from optparse import OptionParser
import time
# try:
import textract as tx
import tensorflow_hub as hub
# import tensorflow-gpu as tf
import tensorflow as tf
# except Exception as e:
#     print(e)
  # !pip install textract
  # import textract as tx
#!pip install --upgrade pip setuptools wheel
#!pip install -I tensorflow
#!pip install -I keras
# import keras
# from keras.preprocessing.sequence import pad_sequences
# from keras.utils import to_categorical
#pip3 install --upgrade --force-reinstall tensorflow-gpu
#!pip install tensorflow
#!pip install keras
# # try:
#     from keras.models import Model, Input
#     from keras.layers import LSTM, Embedding, Dense
#     from keras.layers.merge import add
#     from keras.layers import TimeDistributed, Dropout, Bidirectional, Lambda
#     import tensorflow as tf
#     import tensorflow_hub as hub
#     from keras import backend as K
# # except:
    # !pip install tensorflow
    # !pip install tensorflow_hub
    # !pip install keras
    # from keras.models import Model, Input
    # from keras.layers import LSTM, Embedding, Dense
    # from keras.layers.merge import add
    # from keras.layers import TimeDistributed, Dropout, Bidirectional, Lambda
    # import tensorflow as tf
    # import tensorflow_hub as hub
    # from keras import backend as K

#!pip install textract


class resume_parsing:
    def __init__(self, filepath):
        self.filepath = filepath
        self.max_len = 400
        pickle_in = open("./idx2tag.pickle","rb")
        self.idx2tag = pickle.load(pickle_in)
        self.batch_size = 32
        self.n_tags = len(self.idx2tag.keys())
        # print(self.n_tags)
        print(self.idx2tag)
        # print(type(self.idx2tag))

    def pre_processing(self):
        # file path should have .pdf, .docx or .doc extension
        extension = self.filepath.split('.')
        # print(extension)
        if 'pdf' in extension or 'doc' in extension or 'docx' in extension:
            # text = tx.process(self.filepath, method="pdftotext").decode('utf-8').replace('  ','')
            text = tx.process(self.filepath, method="pdftotext").decode('utf-8')
            # print(text)
            text = text.split('\n')
            print(text)
            padd_to_2d_test = [i for i in text if i and i!=' ' ]
            # text = text.replace('\n',' ').replace('\t',' ').replace('\r',' ').replace('(',' ( ').replace(')',' ) ').replace('}',' } ')
            # text = text.replace(',',' , ').replace('{',' { ').replace('  ',' ').replace(':',' ')
            # padd_to_2d_test = []
            # text = text.split('\n')
            j = 0
            length = 400 - len(padd_to_2d_test)
            if len(padd_to_2d_test) < 400:
              while(j<length):
                padd_to_2d_test.append('__PAD__')
                j+=1
            test = []
            test.append(padd_to_2d_test)
            for seq in range(int(31)):
                new_seq = []
                for i in range(self.max_len):
                  new_seq.append("__PAD__")
                test.append(new_seq)
        #    print("Shape of data : ", np.array(test).shape)

            return test
        else:
            return 'file should be in .pdf or doc form'


    def check_dict_key(self, dict_data, key):
        if key not in dict_data.keys():
            dict_data[key] = []

    def read_model(self):
        try:
            pickle_in = open("./model.pickle","rb")
            return pickle.load(pickle_in)
        except FileNotFoundError as e:
            print("File Not Found Error : "+str(e))
            return "File Not Found Error"

    def model_prediction(self):
        try:
            padd_to_2d_test = self.pre_processing()
        except Exception as e:
            return "Data Error : "+str(e)
        try:
            model = self.read_model()
            if model == "File Not Found Error":
                return "File Not Found Error"
            print(np.array(padd_to_2d_test).shape)
            p = model.predict(np.array(padd_to_2d_test))
            p = np.argmax(p, axis=-1)
            word_tag = ""
            dict_data = {}
            for i in range(p.shape[0]):
              for w, pred in zip(padd_to_2d_test[i], p[i]):
                if w != "__PAD__" and self.idx2tag[pred] != 'OTH':
                    print("{:15}: ({})".format(w, self.idx2tag[pred]))
                    word = w
                    self.check_dict_key(dict_data, self.idx2tag[pred])
                    if self.idx2tag[pred] == 'B-PERSON':
                        word_tag = 'B-PERSON'
                        dict_data['B-PERSON'].append(word)
                    elif self.idx2tag[pred] == 'I-PERSON':
                        if word_tag == 'B-PERSON':
                            dict_data['B-PERSON'][-1] = dict_data['B-PERSON'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-PERSON')
                            dict_data['B-PERSON'].append(word)
                    if self.idx2tag[pred] == 'B-SKILLS':
                        word_tag = 'B-SKILLS'
                        dict_data['B-SKILLS'].append(word)
                    elif self.idx2tag[pred] == 'I-SKILLS':
                        if word_tag == 'B-SKILLS':
                            dict_data['B-SKILLS'][-1] = dict_data['B-SKILLS'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-SKILLS')
                            dict_data['B-SKILLS'].append(word)
                    if w.lower()!='email':
                        if self.idx2tag[pred] == 'B-EMAIL':
                            word_tag = 'B-EMAIL'
                            dict_data['B-EMAIL'].append(word)
                        elif self.idx2tag[pred] == 'I-EMAIL':
                            if word_tag == 'B-EMAIL':
                                dict_data['B-EMAIL'][-1] = dict_data['B-EMAIL'][-1]+' '+word
                            else:
                                self.check_dict_key(dict_data, 'B-EMAIL')
                                dict_data['B-EMAIL'].append(word)

                    if self.idx2tag[pred] == 'B-COMPANY':
                        word_tag = 'B-COMPANY'
                        dict_data['B-COMPANY'].append(word)
                    elif self.idx2tag[pred] == 'I-COMPANY':
                        if word_tag == 'B-COMPANY':
                            dict_data['B-COMPANY'][-1] = dict_data['B-COMPANY'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-COMPANY')
                            dict_data['B-COMPANY'].append(word)

                    if self.idx2tag[pred] == 'B-LOCATION':
                        word_tag = 'B-LOCATION'
                        dict_data['B-LOCATION'].append(word)
                    elif self.idx2tag[pred] == 'I-LOCATION':
                        if word_tag == 'B-LOCATION':
                            dict_data['B-LOCATION'][-1] = dict_data['B-LOCATION'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-LOCATION')
                            dict_data['B-LOCATION'].append(word)

                    if self.idx2tag[pred] == 'B-DEGREE':
                        word_tag = 'B-DEGREE'
                        dict_data['B-DEGREE'].append(word)
                    elif self.idx2tag[pred] == 'I-DEGREE':
                        if word_tag == 'B-DEGREE':
                            dict_data['B-DEGREE'][-1] = dict_data['B-DEGREE'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-DEGREE')
                            dict_data['B-DEGREE'].append(word)

                    if self.idx2tag[pred] == 'B-COLLEGE':
                        word_tag = 'B-COLLEGE'
                        dict_data['B-COLLEGE'].append(word)
                    elif self.idx2tag[pred] == 'I-COLLEGE':
                        if word_tag == 'B-COLLEGE':
                            dict_data['B-COLLEGE'][-1] = dict_data['B-COLLEGE'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-COLLEGE')
                            dict_data['B-COLLEGE'].append(word)

                    if self.idx2tag[pred] == 'B-EXP':
                        word_tag = 'B-EXP'
                        dict_data['B-EXP'].append(word)
                    elif self.idx2tag[pred] == 'I-EXP':
                        if word_tag == 'B-EXP':
                            dict_data['B-EXP'][-1] = dict_data['B-EXP'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-EXP')
                            dict_data['B-EXP'].append(word)
                    if self.idx2tag[pred] == 'B-PROJECT-EXP':
                        word_tag = 'B-PROJECT-EXP'
                        dict_data['B-PROJECT-EXP'].append(word)
                    elif self.idx2tag[pred] == 'I-PROJECT-EXP':
                        if word_tag == 'B-PROJECT-EXP':
                            dict_data['B-PROJECT-EXP'][-1] = dict_data['B-PROJECT-EXP'][-1]+' '+word
                        else:
                            self.check_dict_key(dict_data, 'B-PROJECT-EXP')
                            dict_data['B-PROJECT-EXP'].append(word)
            return dict_data
        except Exception as e:
            # print("Session Error" , e)
            return "Session Error : "+str(e)


# resume = resume_parsing('Raghvendra Resume.pdf')
#resume = resume_parsing('/content/drive/My Drive/Resume/Raghvendra Resume.pdf')
# model.summary()
#
#model_prediction('Raghvendra Resume.pdf')
# data_dict = resume.model_prediction()
# print(sys.argv)
parser = OptionParser()

parser.add_option("-p", "--path", dest="file_path", help="Path to Image.")
(options, args) = parser.parse_args()

time1 = time.time()
resume = resume_parsing(options.file_path)
# text = resume.pre_processing()
# print(text)
# print("Shape", text.shape)
data_dict = resume.model_prediction()
# print(data_dict)
# print(json.dumps(data_dict))
print("time taken : ", time.time() - time1)
# print("Data Printed")
# sys.exit(0)
