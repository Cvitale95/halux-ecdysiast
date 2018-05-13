#CST205 Final Project
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,QPushButton, QHBoxLayout, QVBoxLayout, QTextBrowser
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
from urllib.request import Request, urlopen
import numpy as np
import cv2




class Encryption(QWidget):
	def __init__(self):
		super().__init__()
		
		#Set the Window
		self.setGeometry(100,100,300,300)
		self.setWindowTitle("CST 205 Final Project")
		
		#Line
		self.lineedit = QLineEdit("Enter your image's URL")
		self.lineedit.selectAll()
		
		#Button
		self.button = QPushButton("Download URL!",self) 
		self.label = QLabel('Its very case sensetive')
		self.button.clicked.connect(self.on_click)



		#Line the second
		self.lineedit2 = QLineEdit("Enter the name of your image")
		self.lineedit2.selectAll()

		
		#Button the Second
		self.button2 = QPushButton("Click to see your image") 
		self.label2 =QLabel("View Image in new window")
		self.button2.clicked.connect(self.on_click2)

		
		#Adding Widgets
		layout = QVBoxLayout()
		layout.addWidget(self.lineedit)
		layout.addWidget(self.button)
		layout.addWidget(self.label)
		layout.addWidget(self.lineedit2)
		layout.addWidget(self.button2)
		layout.addWidget(self.label2)
		
		
		#Adding Layout
		self.setLayout(layout)
		self.lineedit.setFocus()
		
	@pyqtSlot()
	#Button 1
	def on_click(self):
				    text = self.lineedit.text()
				    r = urlopen(text)
				    image_saved = open("Encrypt_Image.jpg","wb")
				    image_saved.write(r.read())
				    image_saved.close()
				    self.label.setText("Your image should be saved where you opened this application. It will be called Ecrypt_Image.")
                                                                                
		
	#Button 2
	def on_click2(self):
				textii = self.lineedit2.text()
				img_b = cv2.imread(textii)
				cv2.imshow("",img_b)
				
				





#Exit		
app = QApplication(sys.argv)
ex = Encryption()
ex.show()
sys.exit(app.exec_())
