from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  
from PyQt5.QtGui import *

try: 
	from .raw import *
	from .StyleSheet import *

except Exception: 
	from raw import *
	from StyleSheet import *

def shadow(radius:int):
	shadow  =  QGraphicsDropShadowEffect()
	shadow.setColor(Qt.black)
	shadow.setBlurRadius(radius)
	return shadow

def side_bar(master):
	_frame = QFrame(master)
	_frame.setGeometry(QRect(2, 1, 65, 1245))
	_frame.setStyleSheet(SIDEBAR)
	_frame.setGraphicsEffect(shadow(165))
	
	return _frame

def frame(master):
	_frame = QFrame(master)
	_frame.setGeometry(QRect(97, 0, 1451, 1521))
	_frame.mousePressEvent = lambda event : _frame.setFocus()
	_frame.setStyleSheet('''QFrame{ 
		border-radius: 15px
		}''')

	return _frame

def scroll_bar(master):

	_scroll_bar = QScrollArea(master)

	CHILD = QFrame()

	_scroll_bar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
	_scroll_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
	_scroll_bar.setWidgetResizable(True)

	_scroll_bar.setWidget(CHILD)
	
	return CHILD, _scroll_bar


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
	
	if val == 'ico': return icon
	else: return pixmap
