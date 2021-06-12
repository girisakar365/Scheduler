from FrontEnd.source import *

class MGSub(QDialog):

	def __init__(self):
		
		super().__init__()

		self.tool=Source(self)

		self.setWindowTitle('Manage Subject')
		self.resize(353,495)
		self.setMaximumSize(QSize(323,365))
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

		self.widget()

		self.setFocus()
		self.exec_()

	def widget(self):
		title=self.tool.label(self,'Optional Subjects','title')
		self.tool.geometry(title,8, 15, 220, 37)
		
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

		conform_btw = self.tool.button(self, style=self.tool.addStyle(20))
		self.tool.geometry(conform_btw,270, 320, 40, 40)
		conform_btw.setIcon( self.tool.image( PhotoLib.get(4) ) )
		self.tool.imageGeo(conform_btw,32)
		conform_btw.clicked.connect(self.close)

	def on_off(self,widget,line):
		if widget.isChecked():
			line.setEnabled(True)
			line.setFocus()

		else:
			line.clear()
			line.setEnabled(False)