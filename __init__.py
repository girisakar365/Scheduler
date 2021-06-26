'''
-*- coding: utf-8 -*-

__init__: FRONTEND COMPONENTS:

WARNING: Dependency files required to run this script must be avaliable.
'''

from source import *
from BackEnd.ttframe import ttframe
from BackEnd.trframe import trframe 
from subwin import MGSub

class FrontEnd(QMainWindow):

	def __init__(self,app):

		super().__init__()

		self.tool=Source(self)

		self.sidebar=self.side_bar()

		self.ttframe=self.tool.frame()
		self.tool.geometry(self.ttframe,230, -150, 0,0)

		self.trframe=self.tool.frame()
		self.tool.geometry(self.trframe,230, -150, 0, 0)

		self.hframe=self.tool.frame()
		self.tool.geometry(self.hframe,230, -150, 1451, 1521)
		self.widget()

		scr_rs = app.desktop().screenGeometry()
		width, height = scr_rs.width(), scr_rs.height()
		self.resize(width,height)

		self.show()

	def side_bar(self):

		sidebar=self.tool.frame()
		self.tool.geometry(sidebar,0, 0, 201, 1245)

		#BAR-StyleSheet
		sidebar.setStyleSheet('''QFrame{
		background-color: #004C98;
		}''')

		#BAR-Orientation:
		sidebar.setFrameShape(QFrame.StyledPanel)
		sidebar.setFrameShadow(QFrame.Raised)
		sidebar.setObjectName("bar")

		return sidebar

	def ttf(self):
		
		self.tool.geometry(self.ttframe,207, -150, 1451, 1521)

		#ORIENTATION
		self.ttframe.setFrameShape(QFrame.StyledPanel)
		self.ttframe.setFrameShadow(QFrame.Raised)
		self.ttframe.setObjectName("tt_frame")

		self.tool.geometry(self.trframe,230, -150, 0, 0)
		self.tool.geometry(self.hframe,230, -150, 0, 0)

	def hf(self):
		
		self.tool.geometry(self.hframe,230, -150, 1451, 1521)

		#ORIENTATION
		self.hframe.setFrameShape(QFrame.StyledPanel)
		self.hframe.setFrameShadow(QFrame.Raised)
		self.hframe.setObjectName("hframe")

		self.tool.geometry(self.trframe,230, -150, 0, 0)
		self.tool.geometry(self.ttframe,230, -150, 0, 0)

	def trf(self):

		self.tool.geometry(self.trframe,205, -10, 1451, 1521)

		self.trframe.setFrameShape(QFrame.StyledPanel)
		self.trframe.setFrameShadow(QFrame.Raised)
		self.trframe.setObjectName("tr_frame")

		self.tool.geometry(self.ttframe,230,-150,0,0)
		self.tool.geometry(self.hframe,230, -150, 0, 0)

	def widget(self):

		#LABELS:--------------------------------------------------
		menu_label = self.tool.label(self.sidebar,"Menu",'title')
		self.tool.geometry(menu_label,10, 20, 71, 37)

		home_label = self.tool.label(self.sidebar,"Home",'subtitle')
		self.tool.geometry(home_label,10, 90, 54, 30)

		home_line=self.tool.line(self.sidebar)
		self.tool.geometry(home_line,7,330,211,10)

		setting_label = self.tool.label(self.sidebar,"Setting",'subtitle')
		self.tool.geometry(setting_label,10, 350, 68, 30)

		setting_line=self.tool.line(self.sidebar)
		self.tool.geometry(setting_line,7,500,211,10)

		about_label = self.tool.label(self.sidebar,"About",'subtitle')
		self.tool.geometry(about_label,10, 520, 54, 30)

		#BUTTON:------------------------------------------------------------
		schrecord_btw = self.tool.button(self.sidebar,"Scheduled Records")
		self.tool.geometry(schrecord_btw,10, 160, 161, 51)
		schrecord_btw.clicked.connect(self.hf)

		timetable_btw = self.tool.button(self.sidebar,"Time Table")
		self.tool.geometry(timetable_btw,10, 220, 161, 51)
		timetable_btw.clicked.connect(self.ttf)

		professor_btw = self.tool.button(self.sidebar,"Professor")
		self.tool.geometry(professor_btw,20, 280, 161, 51)
		professor_btw.clicked.connect(self.trf)

		user_btw = self.tool.button(self.sidebar,"User")
		self.tool.geometry(user_btw,10, 390, 161, 51)

		display_btw = self.tool.button(self.sidebar,"Display")
		self.tool.geometry(display_btw,10, 450, 161, 51)

		guid_btw = self.tool.button(self.sidebar,"Guide")
		self.tool.geometry(guid_btw,10, 570, 161, 51)

		#HFRAME--------------------------------------------------------------	

		hf_info_line=self.tool.line(self.hframe,'v')
		self.tool.geometry(hf_info_line,580, 190, 3, 981)

		hf_timetable_label = self.tool.label(self.hframe,"Time tables",'title')
		self.tool.geometry(hf_timetable_label,110, 230, 151, 41)

		hf_teacheregistration_label = self.tool.label(self.hframe,"Teacher Records",'title')
		self.tool.geometry(hf_teacheregistration_label,710, 230, 201, 41)

		#TTFRAME---------------------------------------------------------------
		tt_timetable_label = self.tool.label(self.ttframe,"Time Table",'title')
		self.tool.geometry(tt_timetable_label,10, 160, 166, 28)

		tt_facultyinfo_label = self.tool.label(self.ttframe,"Faculty Information",'subtitle')
		self.tool.geometry(tt_facultyinfo_label,10, 240, 166, 28)		
		
		tt_facultyinfo_line=self.tool.line(self.ttframe)
		self.tool.geometry(tt_facultyinfo_line,0,512,277,3)
		
		tt_class_label = self.tool.label(self.ttframe,"Class:",'normal')
		self.tool.geometry(tt_class_label,40, 290, 37, 21)		

		tt_faculty_label = self.tool.label(self.ttframe,"Faculty:",'normal')
		self.tool.geometry(tt_faculty_label,40, 330, 50, 21)	

		tt_shift_label = self.tool.label(self.ttframe,"Shift:",'normal')
		self.tool.geometry(tt_shift_label,40, 380, 33, 21)		

		tt_totalsec_label = self.tool.label(self.ttframe,"Total Seciton:",'normal')
		self.tool.geometry(tt_totalsec_label,40, 430, 96, 21)		

		tt_mgsub_label = self.tool.label(self.ttframe,"Manage Subject:",'normal')
		self.tool.geometry(tt_mgsub_label,40, 470, 121, 21)		

		tt_periodinfo_label = self.tool.label(self.ttframe,"Period Information",'subtitle')
		self.tool.geometry(tt_periodinfo_label,10, 530, 168, 21)

		tt_totalperiod_label = self.tool.label(self.ttframe,"Total Period:",'normal')
		self.tool.geometry(tt_totalperiod_label,40, 570, 96, 21)

		tt_time_label = self.tool.label(self.ttframe,"Time:",'normal')
		self.tool.geometry(tt_time_label,40, 605, 36, 21)

		tt_timeperprd_label = self.tool.label(self.ttframe,"Time Per Period:",'normal')
		self.tool.geometry(tt_timeperprd_label,40, 640, 109, 21)

		tt_periodinfo_line=self.tool.line(self.ttframe)
		self.tool.geometry(tt_periodinfo_line,0,730,277,3)

		tt_option_label = self.tool.label(self.ttframe,"Options",'subtitle')
		self.tool.geometry(tt_option_label,10, 740, 70, 40)

		tt_routine_label = self.tool.label(self.ttframe,"Routine",'title')
		self.tool.geometry(tt_routine_label,650, 190, 596, 52)

		tt_hr_line=self.tool.line(self.ttframe,'v')
		self.tool.geometry(tt_hr_line,275, 5, 10, 890)

		#TT-ENTRY:------------------------------------------------------------------
		totalsection_completer=[str(i+1) for i in range(48)]
		totalprd_completer=[str(i+1) for i in range(4,8)]
		timeperprd_completer=['45','1','2']

		totalsection_entry=self.tool.entry(self.ttframe)
		self.tool.geometry(totalsection_entry,160, 430, 90, 21)
		self.tool.completer(totalsection_entry,totalsection_completer)
		self.tool.IntValidator(totalsection_entry)

		totalprd_entry=self.tool.entry(self.ttframe)
		self.tool.geometry(totalprd_entry,160, 570, 111, 21)
		self.tool.completer(totalprd_entry,totalprd_completer)
		self.tool.IntValidator(totalprd_entry,2)

		timeperprd_entry=self.tool.entry(self.ttframe)
		self.tool.geometry(timeperprd_entry,160, 640, 51, 21)
		self.tool.completer(timeperprd_entry,timeperprd_completer)
		self.tool.IntValidator(timeperprd_entry,2)

		#TT-Button------------------------------------------------------------------
		tt_mgsub_btw = self.tool.button(self.ttframe, style=self.tool.addStyle(15))
		self.tool.geometry(tt_mgsub_btw,170, 465, 30, 30)
		tt_mgsub_btw.setIcon( self.tool.image( PhotoLib.get(2) ) )
		self.tool.imageGeo(tt_mgsub_btw,24)
		tt_mgsub_btw.clicked.connect(self.subWindow)
		self.tool.animate_btw(tt_mgsub_btw,24,16)

		tt_conform_btw = self.tool.button(self.ttframe, style=self.tool.addStyle(20))
		self.tool.geometry(tt_conform_btw,230, 680, 40, 40)
		tt_conform_btw.setIcon( self.tool.image( PhotoLib.get(4) ) )
		self.tool.imageGeo(tt_conform_btw,32)
		self.tool.animate_btw(tt_conform_btw,32)		
		
		tt_mail_btw = self.tool.button(self.ttframe, style=self.tool.addStyle(20))
		self.tool.geometry(tt_mail_btw,20, 810, 40, 40)
		tt_mail_btw.setIcon( self.tool.image( PhotoLib.get(3) ) )
		self.tool.imageGeo(tt_mail_btw,32)
		self.tool.animate_btw(tt_mail_btw,32)

		tt_pdf_btw = self.tool.button(self.ttframe, style=self.tool.addStyle(20))
		self.tool.geometry(tt_pdf_btw,75, 810, 40, 40)
		tt_pdf_btw.setIcon( self.tool.image( PhotoLib.get(9) ) )
		self.tool.imageGeo(tt_pdf_btw,32)
		self.tool.animate_btw(tt_pdf_btw,32)

		#TT-COMBO:-------------------------------------------------------------------
		class_combo=['11','12']
		tt_class_combo=self.tool.combo(self.ttframe,class_combo)
		self.tool.geometry(tt_class_combo,160, 290, 91, 23)
		
		faculty_combo=['Science','Management','Law']
		tt_faculty_combo=self.tool.combo(self.ttframe,faculty_combo)
		self.tool.geometry(tt_faculty_combo,160, 330, 91, 23)
		
		shift_combo=['Morning','Day']
		tt_shift_combo=self.tool.combo(self.ttframe,shift_combo)
		self.tool.geometry(tt_shift_combo,160, 380, 91, 23)

		timecombo1=[str(i) for i in range(1,13)]
		tt_time_combo1=self.tool.combo(self.ttframe,timecombo1)
		self.tool.geometry(tt_time_combo1,160, 600, 51, 23)

		timecombo2=['AM','PM']
		tt_time_combo2=self.tool.combo(self.ttframe,timecombo2)
		self.tool.geometry(tt_time_combo2,220, 600, 51, 23)		

		tppcombo=['Min','Hr']
		tt_time_combo2=self.tool.combo(self.ttframe,tppcombo)
		self.tool.geometry(tt_time_combo2,220, 640, 51, 23)		

		#TT-Table---------------------------------------------------------------		
		tt_table=self.tool.table(self.ttframe)
		self.tool.geometry(tt_table,287, 240, 853, 640)	

		#BACKEND-TT:
		BE_TT=ttframe(
		tt_mgsub_btw,tt_conform_btw,tt_mail_btw,tt_pdf_btw,#BUTTONS#
		entry=(totalsection_entry,totalprd_entry,timeperprd_entry),
		combo=(tt_class_combo,tt_faculty_combo,tt_shift_combo,tt_time_combo1,tt_time_combo2),
		table=tt_table,
		label=tt_routine_label,
		tool=self.tool,frame=self.ttframe
			)

		#TRFRAME------------------------------------------------------------------------
		tr_professor_label = self.tool.label(self.trframe,"Professor",'title')
		self.tool.geometry(tr_professor_label,10, 20, 287, 37)

		tr_form_label = self.tool.label(self.trframe,"Registration Form",'subtitle')
		self.tool.geometry(tr_form_label,10, 80, 160, 35)

		tr_fname_label = self.tool.label(self.trframe,"Frist Name:",'normal')
		self.tool.geometry(tr_fname_label,30, 130, 74, 21)

		tr_sname_label = self.tool.label(self.trframe,"Surname Name:",'normal')
		self.tool.geometry(tr_sname_label,30, 170, 106, 21)

		tr_subject_label = self.tool.label(self.trframe,"Subject:",'normal')
		self.tool.geometry(tr_subject_label,30, 210, 90, 21)

		tr_email_label = self.tool.label(self.trframe,"Email:",'normal')
		self.tool.geometry(tr_email_label,30, 250, 45, 21)

		tr_classes_label = self.tool.label(self.trframe,"Classes:",'normal')
		self.tool.geometry(tr_classes_label,30, 295, 90, 21)

		tr_div_label = self.tool.label(self.trframe,"Course Divider",'subtitle')
		self.tool.geometry(tr_div_label,10, 410, 150, 25)

		tr_option_label = self.tool.label(self.trframe,"Options",'subtitle')
		self.tool.geometry(tr_option_label,10, 660, 96, 25)

		tr_tableinfo_label = self.tool.label(self.trframe,"Professor Record",'subtitle')
		self.tool.geometry(tr_tableinfo_label,350,40,270,32)

		tr_totalsec_label=self.tool.label(self.trframe,"Total Section:",'normal')
		self.tool.geometry(tr_totalsec_label,10, 455, 90, 22)

		tr_class_label=self.tool.label(self.trframe,"Class:",'normal')
		self.tool.geometry(tr_class_label,10, 490, 90, 22)

		tr_faculty_label=self.tool.label(self.trframe,"Faculty",'normal')
		self.tool.geometry(tr_faculty_label,10, 530, 90, 22)

		tr_shift_label=self.tool.label(self.trframe,"Shift",'normal')
		self.tool.geometry(tr_shift_label,10, 570, 90, 22)

		# TR-ENTRY----------------------------------------------------------------
		tr_fname_entry=self.tool.entry(self.trframe)
		self.tool.geometry(tr_fname_entry,145, 130, 90, 21)
		tr_fname_entry.setPlaceholderText('First Name')
		
		tr_sname_entry=self.tool.entry(self.trframe)
		self.tool.geometry(tr_sname_entry,145, 170, 90, 22)
		tr_sname_entry.setPlaceholderText('Surname Name')
		
		tr_subject_entry=self.tool.entry(self.trframe)
		self.tool.geometry(tr_subject_entry,145, 210, 130, 21)
		tr_subject_entry.setPlaceholderText('Subject')
		sub_list=['Physics', 'Chemistry','Maths','English','Nepali','Computer',
		'Account','Economics','Constitutional Law','Jurispredunce','Procedrual Law',
		'Social']
		self.tool.completer(tr_subject_entry,sub_list)
		tr_email_entry=self.tool.entry(self.trframe)
		self.tool.geometry(tr_email_entry,145, 250, 130, 22)
		tr_email_entry.setPlaceholderText('example@gmail.com')

		tr_tsec_entry=self.tool.entry(self.trframe)
		self.tool.geometry(tr_tsec_entry,145, 455, 90, 22)
		tr_tsec_entry.setPlaceholderText('Total Section')
		self.tool.IntValidator(tr_tsec_entry)

		tr_search_entry=self.tool.entry(self.trframe)
		tr_search_entry.setStyleSheet('''
		    background-color: #FFFFFF;
		    border-radius: 5px;
		    border-color:#FFFFFF;
		    color:#292728;''')
		shadow = QGraphicsDropShadowEffect()
		shadow.setColor(Qt.black)
		shadow.setBlurRadius(1)
		tr_search_entry.setGraphicsEffect(shadow)
		self.tool.geometry(tr_search_entry,350, 90, 670, 35)
		self.tool.font('entry',tr_search_entry)
		c=self.tool.completer(tr_search_entry,[next(iter(i)) for i in Cache.fetch()])
		c.popup().setStyleSheet('''selection-background-color:#474747;
		selection-color:#EFEFF0;''')
		tr_search_entry.setPlaceholderText('Search (by name, subject, email, class)')

		tr_fromsec_line=self.tool.line(self.trframe)
		self.tool.geometry(tr_fromsec_line,0,400,291,10)

		tr_secdiv_line=self.tool.line(self.trframe)
		self.tool.geometry(tr_secdiv_line,0,650,291,10)
		
		tr_hr_line=self.tool.line(self.trframe,'v')
		self.tool.geometry(tr_hr_line,285, 5, 10, 890)

		#TR-COMBO------------------------------------------------------------
		iteach_combo=['11','12','both']
		tr_iteach_combo=self.tool.combo(self.trframe,iteach_combo)
		self.tool.geometry(tr_iteach_combo,145, 295, 90, 21)

		class_combotr=['11','12']
		tr_class_combo=self.tool.combo(self.trframe,class_combotr)
		self.tool.geometry(tr_class_combo,145, 490, 91, 23)
		
		faculty_combotr=['Science','Management','Law']
		tr_faculty_combo=self.tool.combo(self.trframe,faculty_combotr)
		self.tool.geometry(tr_faculty_combo,145, 530, 91, 23)
		
		shift_combotr=['Morning','Day']
		tr_shift_combo=self.tool.combo(self.trframe,shift_combotr)
		self.tool.geometry(tr_shift_combo,145, 570, 91, 23)

		#TR-Button-------------------------------------------------------------
		tr_conform_btw = self.tool.button(self.trframe, style=self.tool.addStyle(20))
		self.tool.geometry(tr_conform_btw,230, 350, 40, 40)
		tr_conform_btw.setIcon( self.tool.image( PhotoLib.get(4) ) )
		self.tool.imageGeo(tr_conform_btw,32)
		self.tool.animate_btw(tr_conform_btw,32)
		
		tr_dtable_btw = self.tool.button(self.trframe, style=self.tool.addStyle(20))
		self.tool.geometry(tr_dtable_btw,10, 700, 40, 40)
		tr_dtable_btw.setIcon( self.tool.image( PhotoLib.get(1) ) )
		self.tool.imageGeo(tr_dtable_btw,32)
		self.tool.animate_btw(tr_dtable_btw,32)	
		
		tr_pdf_btw = self.tool.button(self.trframe, style=self.tool.addStyle(20))
		self.tool.geometry(tr_pdf_btw,60, 700, 40, 40)
		tr_pdf_btw.setIcon( self.tool.image( PhotoLib.get(9) ) )
		self.tool.imageGeo(tr_pdf_btw,32)
		self.tool.animate_btw(tr_pdf_btw,32)

		tr_search_btw=self.tool.button(self.trframe)
		tr_search_btw.setStyleSheet('''QPushButton{
		border-radius:12px;
		background-color: white;
		color:#292728;
		}''')
		self.tool.geometry(tr_search_btw,982, 90, 38, 35)
		tr_search_btw.setIcon( self.tool.image( PhotoLib.get(6) ) )
		self.tool.imageGeo(tr_search_btw,24)
		self.tool.animate_btw(tr_search_btw,24,21)

		tr_add_btw = self.tool.button(self.trframe, style=self.tool.addStyle(20))
		self.tool.geometry(tr_add_btw,230, 610, 40, 40)
		tr_add_btw.setIcon( self.tool.image( PhotoLib.get(10) ) )
		self.tool.imageGeo(tr_add_btw,32)
		self.tool.animate_btw(tr_add_btw,32)

		#TR-Table---------------------------------------------------------------
		tr_table=self.tool.table(self.trframe)
		self.tool.geometry(tr_table,350, 140, 670, 601)

		#BACKEND-TT:
		BE_TR=trframe(
		tr_conform_btw,tr_dtable_btw,tr_pdf_btw,tr_search_btw,#BUTTONS#
		entry=(tr_fname_entry,tr_sname_entry,tr_subject_entry,tr_email_entry),
		combo=tr_iteach_combo,
		table=tr_table,
		tool=self.tool,frame=self.trframe,
		search=tr_search_entry
			)

	def subWindow(self):
		win=MGSub()

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	root=FrontEnd(app)#provided app for scree_geo
	sys.exit(app.exec_())