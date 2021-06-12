from FrontEnd.source import * 
from Backend.Generator import Generator

class ttframe: 


	def __init__(self,*arg,**kwarg):

		self.optsub=arg[0]
		self.conform=arg[1]
		self.mail=arg[2]
		self.qr=arg[3]
		self.pdf=arg[4]

		self.widict={key:value for key,value in kwarg.items()}
		self.tool=self.widict['tool']
		self.frame=self.widict['frame']

		# errormsglabel
		self.msg=self.tool.msg(self.frame,'',0,0,82, 23)
		self.conform.clicked.connect(lambda:self._conform())

	def errorcheck(self):

		def msg(y):
			self.msg.setText('Input Missing!')
			self.msg.move(278,y)
			self.msg.show()
			timer=QTimer(self.msg)
			timer.timeout.connect(lambda:self.msg.hide())
			timer.start(5000)

		try:
			int(self.widict['entry'][0].text())
		except Exception:
			msg(430)
		else:
			try:
				int(self.widict['entry'][1].text()) 

			except Exception:
				msg(570)
			else:
				try:
					int(self.widict['entry'][2].text()) 

				except Exception:
					msg(640)
				else:
					self.msg.hide()
					return True


	def _conform(self):

		if self.errorcheck()==True:
			
			ed=[int(i.text()) for i in self.widict['entry']]
			cd=[i.currentText() for i in self.widict['combo']]

			title='Routine: Class-{c} {sb} ({sh})'.format(c=cd[0],sb=cd[1],sh=cd[2])
			self.widict['label'].setText(title)
			self.widict['label'].move(287,190)

			row=['Sun','Mon','Tues','Wed','Thur','Fri']
			col=[str(i+1) for i in range(ed[1])]
			
			Table=self.widict['table']

			Table.setColumnCount(len(col))
			Table.setRowCount((len(row)+1)*ed[0])

			for i in range(len(col)):
				item = QTableWidgetItem('P-'+col[i])
				Table.setHorizontalHeaderItem(i, item)
				item = Table.horizontalHeaderItem(i)
			
			count=0

			if cd[2]=='Day':
				shift='D'
			elif cd[2]=='Morning':
				shift='M'


			for i in range(ed[0]):
				item = QTableWidgetItem(shift+str(i+1))
				Table.setVerticalHeaderItem(7*i, item)
				item = Table.verticalHeaderItem(7*i)

				for i in row:
					count+=1
					item = QTableWidgetItem(i)
					Table.setVerticalHeaderItem(count, item)
					item = Table.verticalHeaderItem(count)
				count+=1

			for a in range(ed[0]*7):
				for b in range(ed[1]):
					 Table.setItem(a,b,QTableWidgetItem(''))

			num=0
			for i in range(ed[0]*6):
				num+=1
				i*=7
				for j in range(ed[1]):
					Table.setItem(i,j,QTableWidgetItem('_______{}_______'.format(shift+str(num))))
				
			

			gen=Generator(cd[1],cd[2],ed[0],(7,11),ed[1])
			for i in range(ed[0]):
				try:
					for j in range(2):
						shuffle(gen.sub_dict[gen.faculty])
						for sub in gen.sub_dict[gen.faculty]:
								a,b=gen.gen_class(gen.shift+str(i+1))
								Table.setItem(a,b,QTableWidgetItem(sub))
					
					if i<=7:
						sub='Computer'
					else:
						sub='Biology'
					for j in range(4):
						a,b=gen.gen_class(gen.shift+str(i+1))
						Table.setItem(a,b,QTableWidgetItem(sub))
				except Exception:
					continue