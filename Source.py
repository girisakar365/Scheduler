from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  
from PyQt5.QtGui import *
from raw import *

def side_bar(master):
	_frame = QFrame(master)
	_frame.setGeometry(QRect(0, 0, 65, 1245))
	_frame.setStyleSheet('''QFrame{
		background-color: #24292E;
		}''')
	
	return _frame

def frame(master):
	_frame = QFrame(master)
	_frame.setGeometry(QRect(67, 0, 1451, 1521))
	_frame.mousePressEvent = lambda event : _frame.setFocus()
	
	return _frame

def scroll_bar(master,x,y,width,height):

	from StyleSheet import SCROLL_BAR

	_scroll_bar = QScrollBar(master)
	_scroll_bar.setGeometry(x,y,width,height)

	_scroll_bar.setStyleSheet(SCROLL_BAR)

	return _scroll_bar

def shadow(radius:int):
	shadow  =  QGraphicsDropShadowEffect()
	shadow.setColor(Qt.black)
	shadow.setBlurRadius(radius)
	return shadow

def font(typ):

	font = QFont()

	switch_dict = {
	'title':['Segoe UI Semibold',23],
	'subtitle':['Segoe UI Light',16],
	'normal':['Segoe UI Light',12],
	'msg':['Segoe UI Light',10],
	'button':['Segoe UI Light',5],
	'huge':['Segoe UI Semibold',30],
	'entry':['Segoe UI Light',12],
	'fancy_title':['Segoe Print',20],
	'fancy_huge':['Segoe Print',30],
	'fancy_subtitle':['Segoe Print',12]

			}

	font.setFamily(switch_dict[typ][0])
	font.setPointSize(switch_dict[typ][1])

	return font

def line(master,x,y,typ = 'h',length = 1300):
	_line  =  QFrame(master)
	#ORENTATION:
	if typ == 'h':
		_line.setFrameShape(QFrame.HLine)
		_line.setFixedSize(length,1)

	elif typ == 'v':
		_line.setFrameShape(QFrame.VLine)
		_line.setFixedSize(1,length)

	_line.move(x,y)
	_line.setStyleSheet('border: 1px solid #6A737D;')
		
	_line.setFrameShadow(QFrame.Sunken)

	return _line

def image(img,val = 'ico'):
	pixmap = QPixmap()
	pixmap.loadFromData(img)

	icon = QIcon()
	icon.addPixmap(pixmap)
	
	if val == 'ico':return icon
	else:return pixmap
