from source import *
from DataBase.lite_db import *

class MGSub(QDialog):

	def __init__(self):
		
		super().__init__()

		self.tool=Source(self)

		self.setWindowTitle('Manage Subject')
		self.resize(353,510)
		self.setMaximumSize(QSize(323,510))
		self.setStyleSheet('''QWidget{
		color:#ffffff;
		background-color:#292728;}''')

		self.maths_entry=self.tool.entry(self)
		self.maths_entry.setPlaceholderText("Sections")
		
		self.social_entry=self.tool.entry(self)
		self.social_entry.setPlaceholderText("Secitons")
		
		self.computer_entry=self.tool.entry(self)
		self.computer_entry.setPlaceholderText("Sections")
		
		self.bio_entry=self.tool.entry(self)
		self.bio_entry.setPlaceholderText("Secitons")		

		self.bstudies_entry=self.tool.entry(self)
		self.bstudies_entry.setPlaceholderText("Secitons")
		
		self.homgt_entry=self.tool.entry(self)
		self.homgt_entry.setPlaceholderText("Secitons")
		
		self.maths_cb=self.tool.checkbox(self,'Basic Mathematics:')
		
		self.social_cb=self.tool.checkbox(self,'Social S.T.D:')
		
		self.computer_cb=self.tool.checkbox(self,'Computer:')
		
		self.bio_cb=self.tool.checkbox(self,'Biology:')

		self.bstudies_cb=self.tool.checkbox(self,'B.Studies:')

		self.homgt_cb=self.tool.checkbox(self,'Hotel Management:')

		self.lab_cb=self.tool.checkbox(self,'State:')

		self.widget()

		self.setFocus()
		self.exec_()

	def widget(self):
		title=self.tool.label(self,'Subject Management','title')
		self.tool.geometry(title,8, 15, 260, 37)
		
		optsubi_title=self.tool.label(self,'Optional Subject I:','normal')
		self.tool.geometry(optsubi_title,10, 70, 150, 37)
		
		self.tool.geometry(self.maths_entry,148,110,50,20)
		self.tool.IntValidator(self.maths_entry)
		self.maths_entry.setEnabled(False)
		
		self.tool.geometry(self.social_entry,148,140,50,20)
		self.tool.IntValidator(self.social_entry)
		self.social_entry.setEnabled(False)

		optsubii_title=self.tool.label(self,'Optional Subject II:','normal')
		self.tool.geometry(optsubii_title,10, 180, 150, 37)

		lab_title=self.tool.label(self,'Lab Management:','normal')
		self.tool.geometry(lab_title,10, 340, 200, 37)

		break_title=self.tool.label(self,'Breaks','normal')
		self.tool.geometry(break_title,10, 410, 200, 37)

		self.tool.geometry(self.computer_entry,148,220,50,20)
		self.tool.IntValidator(self.computer_entry)
		self.computer_entry.setEnabled(False)

		self.tool.geometry(self.bio_entry,148,250,50,20)
		self.tool.IntValidator(self.bio_entry)
		self.bio_entry.setEnabled(False)

		self.tool.geometry(self.bstudies_entry,148,280,50,20)
		self.tool.IntValidator(self.bstudies_entry)
		self.bstudies_entry.setEnabled(False)

		self.tool.geometry(self.homgt_entry,148,310,50,20)
		self.tool.IntValidator(self.homgt_entry)
		self.homgt_entry.setEnabled(False)
		

		self.tool.geometry(self.maths_cb,10,110,125,20)
		self.maths_cb.stateChanged.connect(lambda:self.on_off(self.maths_cb,self.maths_entry))

		self.tool.geometry(self.social_cb,10,140,90,20)
		self.social_cb.stateChanged.connect(lambda:self.on_off(self.social_cb,self.social_entry))

		self.tool.geometry(self.computer_cb,10,220,100,20)
		self.computer_cb.stateChanged.connect(lambda:self.on_off(self.computer_cb,self.computer_entry))

		self.tool.geometry(self.bio_cb,10,250,100,20)
		self.bio_cb.stateChanged.connect(lambda:self.on_off(self.bio_cb,self.bio_entry))
		
		self.tool.geometry(self.bstudies_cb,10,280,100,20)
		self.bstudies_cb.stateChanged.connect(lambda:self.on_off(self.bstudies_cb,self.bstudies_entry))
		
		self.tool.geometry(self.homgt_cb,10,310,125,20)
		self.homgt_cb.stateChanged.connect(lambda:self.on_off(self.homgt_cb,self.homgt_entry))
		
		self.tool.geometry(self.lab_cb,10,380,95,20)
		lab_label=self.tool.label(self,'Include')
		font=QFont()
		font.setPointSize(9)
		lab_label.setFont(font)
		self.tool.geometry(lab_label,68,380,150,20)
		self.lab_cb.setChecked(True)
		self.lab_cb.stateChanged.connect(lambda:self.on_off(self.lab_cb,lab_label,'l'))

		same_rd=self.tool.radiobtw(self,'Same time')
		self.tool.geometry(same_rd,10, 450, 200, 17)
		same_rd.toggled.connect(lambda:Cache.update('break',0))

		split_rd=self.tool.radiobtw(self,'Split according to optional subject')
		split_rd.setChecked(True)
		split_rd.toggled.connect(lambda:Cache.update('break',1))
		self.tool.geometry(split_rd,10, 480, 230, 17)
		
		conform_btw = self.tool.button(self, style=self.tool.addStyle(20))
		self.tool.geometry(conform_btw,280, 468, 40, 40)
		conform_btw.setIcon( self.tool.image( PhotoLib.get(4) ) )
		self.tool.imageGeo(conform_btw,32)
		conform_btw.clicked.connect(self._conform)

	def on_off(self,widget,subwidget,state='e'):

		def entry():
			if widget.isChecked():
				subwidget.setEnabled(True)
				subwidget.setFocus()

			else:
				subwidget.clear()
				subwidget.setEnabled(False)

		def label():
			if widget.isChecked():
				subwidget.setText('Include')
				Cache.update('lab',1)
			else:
				subwidget.setText('Do not Include')
				Cache.update('lab',0)

		switch_dict={'e':entry,
		'l':label,
		}
		switch_dict[state]()

	def _conform(self):

		sub=['math','social','computer','bio','bstudies','homgt']

		count=0
		for i in [ i.text() for i in [self.maths_entry,self.social_entry,self.computer_entry,
		self.bio_entry,self.bstudies_entry,self.homgt_entry] ]:
			if i!='':
				Cache.update(sub[count],int(i))
			count+=1

		self.close()