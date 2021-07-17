from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  
from PyQt5.QtGui import * 
from raw import *

def side_bar(master):
	_frame=QFrame(master)
	_frame.setGeometry(QRect(0, 0, 65, 1245))
	_frame.setStyleSheet('''QFrame{
		background-color: #24292E;
		}''')
	
	return _frame

def frame(master):
	_frame=QFrame(master)
	_frame.setGeometry(QRect(67, 0, 1451, 1521))
	# _frame.setStyleSheet('background-color: #ffffff')
	
	return _frame

def font(typ):

	font=QFont()

	switch_dict={
	'title':['Segoe UI Semibold',20],
	'subtitle':['Segoe UI Light',16],
	'normal':['Segoe UI Light',12],
	'msg':['Segoe UI Light',10],
	'button':['Segoe UI Light',5],
	'huge':['Segoe UI Semibold',30]
			}

	font.setFamily(switch_dict[typ][0])
	font.setPointSize(switch_dict[typ][1])

	return font

def line(master,x,y,height,widht,typ='h'):
	_line = QFrame(master)
	#ORENTATION:
	if typ=='h':
		_line.setFrameShape(QFrame.HLine)

	elif typ=='v':
		_line.setFrameShape(QFrame.VLine)

	_line.setGeometry(QRect(x,y,height,widht))
		
	_line.setFrameShadow(QFrame.Sunken)

	return _line

def image(img):
	pixmap=QPixmap()
	pixmap.loadFromData(img)

	icon=QIcon()
	icon.addPixmap(pixmap)
	return icon
