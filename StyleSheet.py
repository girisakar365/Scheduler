try: from .raw import Cache
except Exception: from raw import Cache

#COLOR:
entry_border = '#6A737D'
bg = ''
color = ''
sidebar_bg = ''
hlg = ''
login_bg = ''
blue_shade = ''

if Cache.fetch('switch','ui') == 0: #light
	bg = '#ffffff'
	color = '#1f2428'
	sidebar_bg = '#F6F8FA'
	hlg = '#ededed'
	login_bg = '#F6F8FA'
	blue_shade = '#00579A'

else: #dark
	bg = '#1f2428'
	color = '#ffffff'
	sidebar_bg = '#24292E'
	hlg = '#6A737D'
	login_bg = '#191D20'
	blue_shade = '#73AAFA'


_ = {
'WIDGET':{0:
'''QWidget{
		color:#1F2428;
		background-color:#ffffff;}''',
	1:
'''QWidget{
		color:#ffffff;
		background-color:#1F2428;}'''
},

'SIDEBAR':{0:
'''QFrame{
		background-color: #F6F8FA; 
		border-radius: 8px
		}''',
	1:
'''QFrame{
		background-color: #24292E; 
		border-radius: 15px
		}'''
},

'LABLE':{
	0:'QLabel{ color:#1F2428; }',
	
	1:'QLabel{ color:#ffffff; }'
},

'NBUTTON':{
	0:
'''QPushButton{
		border-radius:19px;
		}
		QPushButton:hover{
		background-color:#EDEDED;
		}''',
	1:
'''QPushButton{
		border-radius:19px;
		}
		QPushButton:hover{
		background-color:#6A737D;
		}'''
},

'SBUTTON':{
	0:
'''QPushButton{
		border-radius:19px;
		background-color:#F6F8FA
		}
		QPushButton:hover{
		background-color:#EDEDED;
		}''',
	1:
'''QPushButton{
		border-radius:19px;
		background-color:#24292E
		}
		QPushButton:hover{
		background-color:#6A737D;
		}'''
},

'LBUTTON':{
	0:
'''QPushButton{
		border-radius:19px;
		background-color:#F6F8FA;
		}
		QPushButton:hover{
		background-color:#EDEDED;
		}''',
	1:
'''QPushButton{
		border-radius:19px;
		background-color:#191D20;
		}
		QPushButton:hover{
		background-color:#6A737D;
		}'''

},

'LFRAME':{
	0:
'''
	background-color:#F6F8FA;
	border-radius:15px;
	''',
1:
'''
	background-color:#191D20;
	border-radius:15px;
	'''
},

'ENTRY':{ 
	0:
'''QLineEdit {
		    border: 1px solid;
		    border-radius: 5px;
			background-color:#F6F8FA;
		    border-color:#6A737D;
			selection-background-color:#00579A;
		    color:#1f2428;
		}		
		
	QLineEdit:hover{
		border-color:#1f2428;
		}''',
	
	1:
'''QLineEdit {
		    border: 1px solid;
		    border-radius: 5px;
			background-color:#24292E;
		    border-color:#6A737D;
			selection-background-color:#6A737D;
		    color:#ffffff;
		}
		
	QLineEdit:hover{
		border-color:#F6F8FA;
		}''',
	
},

'LENTRY':{
	0:
'''QLineEdit {
		border: 1px solid;
		border-radius: 5px;
		background-color:#F6F8FA;
		border-color:#EEEEEE;
		selection-background-color:#00579A;
		color:#1f2428;
		}
	QLineEdit:hover{
		border-color:#52bf90;
		}''',
	1:
'''QLineEdit {
		border: 1px solid;
		border-radius: 5px;
		background-color:#24292E;
		border-color:#080808;
		selection-background-color:#6A737D;
		color:white;
		}
	QLineEdit:hover{
		border-color:#73AAFA;
		}'''
},

'DIALOG':{
	0:
'''QDialog{
		color:#1F2428;
		background-color:#ffffff;}''',
	
	1:
'''QDialog{
		color:#ffffff;
		background-color:#1F2428;}'''
},

'RBUTTON':{
	0:
'font-size:12px; color: #1F2428;',

	1:
'font-size:12px; color: white;'
},

'COMBO':{
	0:
'''QComboBox {
		    border: 1px solid;
		    border-radius: 10px;
		    border-color:#6A737D;
		}
		
		QComboBox::drop-down {
		     subcontrol-origin: padding;
		     subcontrol-position: right;
		     width: 14px;
		}
		
		QComboBox:hover{
		border-color:#1F2428;
		color:#1F2428;
		}''',

	1: 
'''QComboBox {
		    border: 1px solid;
		    border-radius: 10px;
		    border-color:#6A737D;
		}
		
		QComboBox::drop-down {
		     subcontrol-origin: padding;
		     subcontrol-position: right;
		     width: 14px;
		}
		
		QComboBox:hover{
		border-color:#FFFFFF;
		color:#ffffff;
		}'''
},
'SPINBOX':{0:
'''
QSpinBox{
		border-radius:7px;
		border:1px solid;
		border-color:#6A737D;
		selection-background-color:#00579A;
		}
QSpinBox::up-button{
		color:#1F2428}
QSpinBox::down-button{
		color:#1F2428
		}
QSpinBox::hover
		{
		border-color:#1F2428;
		}''',

1:'''
QSpinBox{
		border-radius:7px;
		border:1px solid;
		border-color:#6A737D;
		selection-background-color:#6A737D;
		}
QSpinBox::up-button{
		color:#FFFFFF}
QSpinBox::down-button{
		color:#FFFFFF
		}
QSpinBox::hover
		{
		border-color:#ffffff;
		}'''},

'TIMEDIAL':{0:'''
QTimeEdit{
		border-radius:7px;
		border:1px solid;
		border-color:#6A737D;
		selection-background-color:#00579A;
		}
QTimeEdit::up-button{
		color:#1F2428}
QTimeEdit::down-button{
		color:#1F2428
		}
QTimeEdit::hover
		{
		border-color:#1F2428;
		}
''',

1: '''
QTimeEdit{
		border-radius:7px;
		border:1px solid;
		border-color:#6A737D;
		selection-background-color:#6A737D;
		}
QTimeEdit::up-button{
		color:#FFFFFF}
QTimeEdit::down-button{
		color:#FFFFFF
		}
QTimeEdit::hover
		{
		border-color:#ffffff;
		}
'''},
}

def Style(WIDGET):
	return _[WIDGET][Cache.fetch('switch','ui')]

MSG_W = 'QFrame{ background-color: #410910; color:#ffffff}'

MSG_S = 'QFrame{ background-color: #49ab81; color:#ffffff}'

MSG_S_BTW ='''QPushButton{
background-color:#49ab81;
border-radius: 2px;
}
QPushButton:hover{
background-color:#52bf90;
}'''

MSG_W_BTW ='''QPushButton{
background-color: #410910;
border-radius: 2px;
}
QPushButton:hover{
background-color:#a00000;
}'''

COMPLETER='''background-color:#292728;
		color:#ffffff;
		selection-background-color:#474747;
		selection-color:#EFEFF0;
		'''

TABLE='''QHeaderView::section{
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

SCROLL_BAR='''QScrollBar{
    background: #e1e1e1;
	width: 8px;
}
QScrollBar::handle:vertical {
    background: #999999;
	border-radius: 1px;
}
QScrollBar::handle:vertical:hover {
    background: #686868;
}
'''