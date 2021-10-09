# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:20:56 2021

@author: Yongjin

Reference: https://besixdouze.net/40

"""

## Installation needed
## pip install python-docx



from docx import Document

document = Document()
document.save("test.docx")

# document.add_heading('이 문서의 타이틀! lvl = 0', level = 0)
# document.add_heading('이 문서의 타이틀! lvl = 1', level = 1)
# document.add_heading('이 문서의 타이틀! lvl = 2', level = 2)
# document.add_heading('이 문서의 타이틀! lvl = 3', level = 3)
# document.add_heading('이 문서의 타이틀! lvl = 4', level = 4)
# document.add_heading('이 문서의 타이틀! lvl = 5', level = 5)


document.save("test.docx")