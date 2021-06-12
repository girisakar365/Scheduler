from source import *

class trframe: 

	def __init__(self,*arg,**kwarg):

		self.conform=arg[0]
		self.dele=arg[1]
		self.pdf=arg[2]
		self.search=arg[3]

		self.widict={key:value for key,value in kwarg.items()}

		self.tool = self.widict['tool']

		self.frame = self.widict['frame']

		self.search_bar=self.widict['search']

		self.msg=self.tool.msg(self.frame,'',0,0,82, 23)

		self.conform.clicked.connect(lambda:self._conform())
		self.search.clicked.connect(lambda:self._search())

	def id_gen(self):
		capitalChar = 'abcdefghijklmnopqrstuvwxyz'.upper()
		number = '0123456789'
		all = capitalChar+number
		return ''.join(sample(all,5))
	
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


	def _conform(self):
		if self.checkerror():
			entry=[i.text() for i in self.widict['entry']]
			itech=self.widict['combo'].currentText()

			data=[]
			c=0
			for i in entry:
				if c==2:
					tid=self.id_gen()
					data.append(tid)
				data.append(i)	
				c+=1
			data.append(itech)
			
			DB.insert(data)

			Table=self.widict['table']
			Table.setColumnCount(6)
			Table.setRowCount(len(DB.fetch()))

			col=['Frist Name','Surname','ID','Subject','Email','Classes']

			for i in range(6):
				item = QTableWidgetItem(col[i])
				Table.setHorizontalHeaderItem(i, item)
				item = Table.horizontalHeaderItem(i)

			rnum=0
			cnum=0
			Table.setColumnWidth(2,60)
			Table.setColumnWidth(4,180)
			for i in DB.fetch():
				for j in i:
					Table.setItem(rnum,cnum,QTableWidgetItem(j))
					cnum+=1
				rnum+=1
				cnum=0

			for i in self.widict['entry']:
				i.clear()

	def _search(self):
		Cache.insert(self.search_bar.text())
		self.search_bar.clear()
		c=self.tool.completer(self.search_bar,[next(iter(i)) for i in Cache.fetch()])
		c.popup().setStyleSheet('''selection-background-color:#474747;
		selection-color:#EFEFF0;''')