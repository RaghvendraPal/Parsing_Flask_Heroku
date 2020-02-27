# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:49:20 2020

@author: DELL
"""

# importing required modules 
#import PyPDF2 
#  
## creating a pdf file object 
#pdfFileObj = open('./upload/Raghvendra_Resume.pdf', 'rb') 
#  
## creating a pdf reader object 
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
#  
## printing number of pages in pdf file 
#print(pdfReader.numPages) 
#  
## creating a page object 
#pageObj = pdfReader.getPage(0) 
#  
## extracting text from page 
#print(pageObj.extractText()) 
#  
## closing the pdf file object 
#pdfFileObj.close() 
from docx import Document

document = Document('./upload/Aarti Demo resume.docx')
for para in document.paragraphs:
    print(para.text)