from source import *

class trframe: 

	def __init__(self,*arg,**kwarg):

		self.conform=arg[0]
		self.delete=arg[1]
		self.pdf=arg[2]
		self.search=arg[3]

		self.widict={key:value for key,value in kwarg.items()}

		self.tool = self.widict['tool']

		self.frame = self.widict['frame']

		self.search_bar=self.widict['search']

		self.msg=self.tool.msg(self.frame,'',0,0,82, 23)

		self.Table=self.widict['table']

		self.conform.clicked.connect(lambda:self._conform())
		self.delete.clicked.connect(lambda:self._delete())
		self.search.clicked.connect(lambda:self._search())
	
	def checkerror(self):
		y=[130,170,210,250]
		num=0
		for i in [i.text() for i in self.widict['entry']]:
			if i=='':
				self.msg.setText('Input Missing!')
				self.msg.move(238,y[num])
				self.msg.show()
				timer=QTimer(self.msg)
				timer.start(5000)
				timer.timeout.connect(lambda:self.msg.hide())
				return False
			num+=1

		return True

			
	def _genTable(self,row:int):
		self.Table.setColumnWidth(2,60)
		self.Table.setColumnWidth(4,210)
		self.Table.setColumnWidth(5,60)
		self.Table.setColumnCount(6)
		self.Table.setRowCount(row)

		col=['Frist Name','Surname','ID','Subject','Email','Classes']

		for i in range(6):
			item = QTableWidgetItem(col[i])
			self.Table.setHorizontalHeaderItem(i, item)
			item = self.Table.horizontalHeaderItem(i)

		for i in  range(row):
			for j in range(6):
				self.Table.setItem(i,j,QTableWidgetItem(''))

	def _conform(self):
		for i in self.widict['entry']:
			i.clear()

	def _delete(self):
		self._genTable(0)

	def _search(self):

		def data_caching():
			#caching data 
			Cache.insert(self.search_bar.text())
			c=self.tool.completer(self.search_bar,[next(iter(i)) for i in Cache.fetch()])
			c.popup().setStyleSheet('''selection-background-color:#474747;
			selection-color:#EFEFF0;''')
		
		data_caching()
		self.search_bar.clear()