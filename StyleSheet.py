#COLOR: 
D_BACKGROUND='#1f2428'
D_LABLE='#ffffff'

WIDGET='''QWidget{
		color:#ffffff;
		background-color:#1F2428;}'''

LABLE="color: #ffffff"

MSG="color: #ffffff; background-color:#471117; border-radius: 10px;"

NORMAL_BUTTON='''QPushButton{
		border-radius:19px;
		}
		QPushButton:hover{
		background-color:#6A737D;
		}'''

COMBO_BOX='''QComboBox {
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

ENTRY='''QLineEdit {
		    border: 1px solid;
		    border-radius: 10px;
		    border-color:#6A737D;
			selection-background-color:#6A737D;
		    color:#ffffff;
		}
		
		QLineEdit:hover{
		    border-color:#ffffff;
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

SPINBOX='''
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
		}'''

FRAME='''
background-color:#191D20;
border-radius:15px;
'''

LOGIN_ENTRY='''
QLineEdit {
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