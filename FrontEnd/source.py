from random import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  
from PyQt5.QtGui import * 
from db import *


class Source: 

	def __init__(self,root):

		self.root=root

		self.root.setObjectName("root")
		
		#SETUPVAR:
		QMetaObject.connectSlotsByName(self.root)

		#WINDOWTITLE:
		self.root.setWindowTitle('Sche-School')
		self.root.setStyleSheet('''QWidget{
		color:#ffffff;
		background-color:#292728;}''')

		self.styledict={
		'label':"color: #ffffff",

		'msg':"color: #ffffff; background-color:#471117; border-radius: 10px;",

		'btw':'''QPushButton{
		background-color: #004C98;
		border-radius:25px;
		}
		QPushButton:hover{
		background-color:#F7941D
		}''',

		'sub-btw':'''QPushButton{
		background-color: #292728;
		color:#ffffff\
		}
		QPushButton:hover{
		background-color:silver;
		}''',

		'combo':'''QComboBox {
		    border: 1px solid;
		    border-radius: 10px;
		    border-color:white;
		    color:#ffffff;
		}
		
		QComboBox:drop-down {
		     subcontrol-origin: padding;
		     subcontrol-position: right;
		     width: 14px;
		}
		
		QComboBox:Box Mode{
		    color:#ffffff
		}
		QComboBox:hover{
		    border-color:#004C98;
		color:#004C98;
		}''',

		'entry':'''QLineEdit {
		    border: 1px solid;
		    border-radius: 9px;
		    border-color:white;
		    color:#ffffff;
		}
		
		QLineEdit:hover{
		    border-color:#004C98;
		}''',

		'competer':'''background-color:#292728;
		color:#ffffff;
		selection-background-color:#474747;
		selection-color:#EFEFF0;
		''',

		'table':'''QHeaderView::section{
		    background-color: #292728;
		border-radius:25px;
		width:25;    
		color:silver;
		}
		
		QTableView::item{
		color:silver;
		selection-background-color:silver;
		selection-color:#292728;
		}
		
		QTableView::item:hover{
		background-color:silver;
		color:#292728;
		border-radius:14px;
		}
		
		QHeaderView::section:hover{
		background-color: silver;
		border-radius:11px;
		color:#292728;
		}'''
		}

	def addStyle(self,size:int):
		
		return self.styledict['sub-btw']+'QPushButton{border-radius:%dpx}'%size

	def completer(self,qline,clist:list):
		completer=QCompleter(clist)
		completer.popup().setStyleSheet(self.styledict['competer'])
		qline.setCompleter(completer)
		return completer

	def font(self,typ,*arg):
		font=QFont()

		if typ=='title':
			font.setFamily("Segoe UI Semibold")
			font.setPointSize(20)
			font.setBold(True)
			return font

		elif typ=='info':
			font.setFamily("Segoe UI bold")
			font.setPointSize(40)
			font.setBold(True)
			return font

		elif typ=='subtitle':
			font.setFamily("Segoe UI Light")
			font.setPointSize(16)
			return font

		elif typ=='normal':
			font.setFamily("Segoe UI Light")
			font.setPointSize(12)
			return font

		elif typ=='msg':
			font.setFamily("Segoe UI Light")
			font.setPointSize(10)
			return font

		elif typ=='entry':
			font=arg[0].font()
			font.setFamily("Segoe UI Light")
			font.setPointSize(12)
			arg[0].setFont(font)

	def msg(self,master,text,x,y,hight,width):
		label=self.label(master,text,'msg')
		self.geometry(label,x,y,hight,width)
		label.setStyleSheet(self.styledict['msg'])
		label.hide()
		return label

	def geometry(self,widget,x,y,hight,width):
		widget.setGeometry(QRect(x,y,hight,width))

	def label(self,master,text,fonttyp,*arg:str):
		label=QLabel(text,master)
		label.setFont(self.font(fonttyp))
		label.setStyleSheet(self.styledict['label'])
		return label

	def frame(self):
		_frame=QFrame(self.root)
		return _frame

	def line(self,master,typ='h'):
		_line = QFrame(master)
		#ORENTATION:
		if typ=='h':
			_line.setFrameShape(QFrame.HLine)
		else:
			_line.setFrameShape(QFrame.VLine)
		_line.setFrameShadow(QFrame.Sunken)

		return _line

	def entry(self,master):
		_entry=QLineEdit(master)
		_entry.setStyleSheet(self.styledict['entry'])
		_entry.setObjectName("entry")
		return _entry

	def IntValidator(self,entry,length:int=3):
		entry.setValidator(QIntValidator())
		entry.setMaxLength(length)

	def button(self,master,text='',style=None):

		if style!=None:
			pass
		else:
			style=self.styledict['btw']

		btw=QPushButton(text,master)
		btw.setFont(self.font('normal'))
		btw.setStyleSheet(style)
		btw.setCursor(QCursor(Qt.PointingHandCursor))
		return btw

	def animate_btw(self,widget,max_siz,min_siz=28):

		widget.pressed.connect(
			lambda:self.imageGeo(widget,min_siz)
			)
		widget.released.connect(
			lambda:self.imageGeo(widget,max_siz)
			)


	def combo(self,master,combolist:list=[]):
		_combo=QComboBox(master)
		_combo.setStyleSheet(self.styledict['combo'])
		_combo.setObjectName("_combo")

		for i in range(len(combolist)):
			_combo.addItem("")
			_combo.setItemText(i,combolist[i])

		return _combo

	def table(self,master):
		
		Table = QTableWidget(master)
		Table.setStyleSheet(self.styledict['table'])
		Table.setObjectName("table")

		return Table

	def checkbox(self,widget,text='Your text here'):
		 checkBox=QCheckBox(text,widget)
		 checkBox.setStyleSheet('font-size:12px;')
		 checkBox.setCursor(QCursor(Qt.PointingHandCursor))
		 return checkBox

	def image(self,img):
		pixmap=QPixmap()
		pixmap.loadFromData(img)

		icon=QIcon()
		icon.addPixmap(pixmap)
		return icon

	def imageGeo(self,widget,size:int):
		widget.setIconSize(QSize(size,size))