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
	_frame.setStyleSheet(Style('SIDEBAR'))
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
	'fancy_subtitle':['Segoe Print',12],
	'message':['Courier New',12],
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

def message(master, msg:str, type:str):
	_frame = QFrame(master)
	_frame.resize(350, 80)

	_frame.setGraphicsEffect(shadow(200))

	close = QPushButton(_frame)
	close.setIcon(image( PhotoLib.get(46) ))
	
	close.pressed.connect(
	lambda:close.setIconSize(QSize(12,12))
	)
	close.released.connect(
	lambda:close.setIconSize(QSize(13,13)))

	if type.upper() == 'W': 
		_frame.setStyleSheet(MSG_W)
		close.setStyleSheet(MSG_W_BTW)
	elif type.upper() == 'S': 
		_frame.setStyleSheet(MSG_S)
		close.setStyleSheet(MSG_S_BTW)
	
	close.setIconSize(QSize(16,16))
	close.move(320,4)
	close.clicked.connect(_frame.hide)

	lable = QLabel(msg, _frame)
	lable.setFont(font('message'))
	lable.move(8,20)
	lable.resize(300, 20 + len(msg))
	lable.setWordWrap(True)

	time = QTimer(_frame)
	time.timeout.connect(_frame.hide)
	time.start(10000)

	_frame.move(900,650)
	_frame.show()

	return _frame