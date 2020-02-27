# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:51:14 2020

@author: DELL
"""
import multiprocessing
from multiprocessing import Process, Pool, Queue
import os

def func1(number,output):
  print('func1: starting')
  process_id = os.getpid()
  j = 0
  for i in range(100): 
      j+=3
      print('func1: running : {}'.format(process_id))
  print('func1: finished')
  output.put("Result of func1 : "+str(j))
  return True

def func2(number, output):
  print('func2: starting')
  process_id = os.getpid()
  j = 0
  for i in range(100): 
      j+=2
      print('func2: running : {}'.format(process_id))

  print('func2: finished')
  output.put("Result of func2 : "+str(j))
  return True

if __name__ == "__main__":
    output = Queue()
    p1 = Process(target=func1, args = (1,output))
    p2 = Process(target=func2, args = (2,output))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
#    print("Output :",output.get())
    while not output.empty():
        print(output.get())
    
    if output.empty():
        print("Queue is Empty")
#    p = Pool(multiprocessing.cpu_count())
#    data = p.map(func1, func2)
#    p.close()
#    print(data)
#def run_process():
#    p1 = Process(target=func1, args = (1,))
#    p2 = Process(target=func2, args = (2,))
#    a = p1.start()
#    b = p2.start()
#    print(a,b,p1,p2)
#    d1 = 'outside'
#    return d1

#print(run_process())
    
