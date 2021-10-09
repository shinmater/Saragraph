# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:56:45 2021

@author: Yongjin
"""

# extracting_text.py
 
from PyPDF2 import PdfFileReader
 
 
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
 
        # get the first page
        page = pdf.getPage(0)
      #  print(page)
       #     print('Page type: {}'.format(str(type(page))))
 
        text = page.extractText()
        print(text)
 
 
# if __name__ == '__main__':
#     path = 'A4_CV_Shin_KIAS.pdf'
#     text_extractor(path)
    

path = 'Interest Income Statement.pdf'
f = open(path, 'rb')
pdf = PdfFileReader(f)

page = pdf.getPage(0)

text = page.extractText()
print(text)

