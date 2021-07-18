#COLOR: 
D_BACKGROUND='#1F2428'
D_LABLE='#FFFFFF'

LABLE="color= #ffffff"

MSG="color: #ffffff; background-color:#471117; border-radius: 10px;"

NORMAL_BUTTON='''QPushButton{
		border-radius:17px;
		}
		QPushButton:hover{
		background-color:#6A737D;
		}'''

COMBO_BOX='''QComboBox {
		    border: 1px solid;
		    border-radius: 10px;
		    border-color:black;
		    color:#ffffff;
		}
		
		QComboBox::drop-down {
		     subcontrol-origin: padding;
		     subcontrol-position: right;
		     width: 14px;
		}
		
		QComboBox:hover{
		border-color:#6A737D;
		color:#6A737D;
		}'''

ENTRY='''QLineEdit {
		    border: 1px solid;
		    border-radius: 9px;
		    border-color:white;
		    color:#ffffff;
		}
		
		QLineEdit:hover{
		    border-color:#004C98;
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

SPINBOX='''QSpinBox{
		border-radius:7px;
		border:1px solid;
		selection-background-color:#6A737D;
		}
		QSpinBox::up-button{
		color:#FFFFFF}
		QSpinBox::down-button{
		color:#FFFFFF
		}
		QSpinBox::hover
		{
		border-color:#6A737D;
		}'''