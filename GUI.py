# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 03:42:06 2021

@author: yongjin
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QDial
from PyQt5.QtWidgets import QGroupBox,QCheckBox, QHBoxLayout, QSpacerItem,QSizePolicy, QLCDNumber


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        
        groupBox1 = QGroupBox("Config")
        vbox1 = QVBoxLayout(groupBox1) #subject to groupbox
        readFile = QPushButton("Read File", groupBox1)
        
        vbox1.addWidget(readFile, 1)
        decodeFile = QPushButton("Decode", groupBox1)
        decodeFile.clicked.connect(self.clicked_slot)
        vbox1.addWidget(decodeFile, 1)
        chBox = QCheckBox("Advanced", groupBox1)
        vbox1.addWidget(chBox, 1)
        # spacerItem = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # vbox1.addItem(spacerItem)
        
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        vbox.addWidget(groupBox1)
        
        top_btn=QPushButton('Top')
        top_btn.clicked.connect(self.change_txt)
        vbox.addWidget(top_btn)
        
        lcd = QLCDNumber(self)
        dial = QDial(self)
        
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        # connect lcd and dial
        dial.valueChanged.connect(lcd.display)
        
        
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)
        
        
        topLayout = QFormLayout()
        
        self.editline=QLineEdit()
        topLayout.addRow("Some Text:", self.editline)
        
        vbox.addLayout(topLayout)
        
        self.textedit=QTextEdit()
        vbox.addWidget(self.textedit)
        
        readFile.clicked.connect(self.test)
        # Qlabel
        self.testlabel=QLabel('<h1>Hello World!</h1>')
        vbox.addWidget(self.testlabel)

        
        self.setLayout(vbox)
        
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 500)
        #self.move(60, 60)
        self.show()
        
    # Function for push buttons        
    def resizeBig(self):
        self.resize(400, 500)
    def resizeSmall(self):
        self.resize(200, 300)
    def test(self):
        print("TEST") # print this text in the console
        self.editline.clear()
        #self.textedit.setPlainText('Test')
        #self.testlabel.text
    def clicked_slot(self):
        # get text from editline
        string = self.editline.text()
        ## change program title
        self.setWindowTitle(string)
        # and Delete the input text
        self.editline.clear()
    def change_txt(self):
        string = self.editline.text()
        self.testlabel.setText('<h1>{0}</h1>'.format(string))
  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



# Help: https://wikidocs.net/21945
    

# layout2 = QGridLayout()
# layout2.addWidget(QPushButton('Top'))
# layout2.addWidget(QPushButton('Middle'))
# layout2.addWidget(QPushButton('Bottom'),1,1)
# layout2.addWidget(QLabel('<h1>Hello World!</h1>'))


# topLayout = QFormLayout()
# topLayout.addRow("Some Text:", QLineEdit())

