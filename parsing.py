# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:51:14 2020

@author: DELL
"""
from __future__ import absolute_import
import multiprocessing
from numba import jit, cuda
from multiprocessing import Process, Pool, Queue
import os
# from optparse import OptionParser
import json
from ner_data.ner_parsing import ner_model_prediction
# from data import data_dict
from project_data.project_parsing import project_model_prediction
from update_dict_result import update_dict

@jit
def ner_parsing_func(file_path, output):
    ner_parsing_data = ner_model_prediction(file_path)
    output.put(ner_parsing_data)
    # output.put({'a':1})
    return True

def project_parsing_func(file_path, output):
    project_parsing_data = project_model_prediction(file_path)
    output.put(project_parsing_data)
    # output.put({'b':2})
    return True

def main(file_path):
    # parser = OptionParser()
    # parser.add_option("-p", "--path", dest="file_path", help="Path to Image.")
    # (options, args) = parser.parse_args()
    # options.file_path
    output = Queue()
    p1 = Process(target=ner_parsing_func, args = (file_path,output))
    p2 = Process(target=project_parsing_func, args = (file_path,output))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
#    print("Output :",output.get())
    ner_data = output.get()
    project_data = output.get()
    # print(ner_data)
    # print(project_data)
    # print(type(project_data), type(ner_data))
    # try:
    data_dict = {**ner_data, **project_data}
    data_dict = update_dict(data_dict)
        # print(json.dumps(data_dict))
    # except Exception as e:
    #     print("Eception : ", e)
    return data_dict
# if __name__ == "__main__":
#     main()
# def func1(number,output):
#   print('func1: starting')
#   process_id = os.getpid()
#   j = 0
#   for i in range(100):
#       j+=3
#       print('func1: running : {}'.format(process_id))
#   print('func1: finished')
#   output.put("Result of func1 : "+str(j))
#  return True
#
# def func2(number, output):
#   print('func2: starting')
#   process_id = os.getpid()
#   j = 0
#   for i in range(100):
#       j+=2
#       print('func2: running : {}'.format(process_id))
#
#   print('func2: finished')
#   output.put("Result of func2 : "+str(j))
#  return True
#
# if __name__ == "__main__":
#     output = Queue()
#     p1 = Process(target=func1, args = (1,output))
#     p2 = Process(target=func2, args = (2,output))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
# #    print("Output :",output.get())
#     while not output.empty():
#         print(output.get())
#
#     if output.empty():
#         print("Queue is Empty")
# #    p = Pool(multiprocessing.cpu_count())
# #    data = p.map(func1, func2)
# #    p.close()
# #    print(data)
# #def run_process():
# #    p1 = Process(target=func1, args = (1,))
# #    p2 = Process(target=func2, args = (2,))
# #    a = p1.start()
# #    b = p2.start()
# #    print(a,b,p1,p2)
# #    d1 = 'outside'
# #    return d1
#
# #print(run_process())
