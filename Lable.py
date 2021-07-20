from Source import * 
from StyleSheet import LABLE, LOGIN_FRAME

class Label:

    def __init__(self,*arg):
        
        self.WINDOW, self.SIDEBAR, self.TIME_TABLE, self.PROFESSOR, self.SUBJECT, self.RECORD, self.USER, self.SETTING, self.GUID = arg
        
        self.record()
        self.professor()
        self.subject()
        self.time_table()
        self.user()
        self.setting()
        self.guid()

    def lable(self,master,X,Y,text,font_type='normal',style=LABLE):
        
        label=QLabel(text,master)
        label.setFont(font(font_type))
        label.setStyleSheet(style)
        label.setGeometry(QRect(X,Y,0,0))
        label.adjustSize()
        
        return label

    def frame(self,master):
        login_frame=frame(master)
        login_frame.setFixedSize(480,480)
        login_frame.move(670,160) 
        login_frame.setStyleSheet(LOGIN_FRAME)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(Qt.black)
        shadow.setBlurRadius(110)
        login_frame.setGraphicsEffect(shadow)

        return login_frame

    def record(self):
        MASTER=self.RECORD

        title=self.lable(MASTER,10, 10, 'Records','title')

        empty=self.lable(MASTER,401,301,'No Records Saved Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

    def professor(self):
        MASTER=self.PROFESSOR

        info_table=self.lable(MASTER,300,70,'Record of Professors','title')

        line(MASTER,270,0,10,1000,'v')

        empty=self.lable(MASTER,501,301,'No Records Saved Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

        title=self.lable(MASTER,10, 10, 'Professor','title')

        form=self.lable(MASTER,10, 70, 'Entry Form','subtitle')
        
        name=self.lable(MASTER,10, 120, 'Name')
        
        email=self.lable(MASTER,10, 160, 'Email')
        
        subject=self.lable(MASTER,10, 200, 'Subject')
        
        classes=self.lable(MASTER,10, 240, 'Classes')

        line(MASTER,0,330,270,5)

        tool=self.lable(MASTER,10, 350, 'Tools','subtitle')

    def subject(self):
        MASTER=self.SUBJECT

        title=self.lable(MASTER,10, 3,'Subject','title')

        info=self.lable(MASTER,300,40,'Subject List','title')

        empty=self.lable(MASTER,501,301,'No Records Saved Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

        line(MASTER,270,0,10,1000,'v')

        form=self.lable(MASTER,10, 70, 'Subject From','subtitle')
        
        sub_name=self.lable(MASTER,10, 120, 'Subject')
        
        faculty=self.lable(MASTER,10, 160, 'Faculty')
        
        class_=self.lable(MASTER,10, 200, 'Class')

        line(MASTER,0,280,270,5)

        tool=self.lable(MASTER,10, 310, 'Tools','subtitle')


    def time_table(self):
        MASTER=self.TIME_TABLE

        line(MASTER,270,0,10,1000,'v')

        title=self.lable(MASTER,10, 10, 'Time Table','title')

        routine=self.lable(MASTER,300,70,'Routine','title')

        empty=self.lable(MASTER,501,301, 'No Routine Generated Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

        faculty_info=self.lable(MASTER,10, 70, 'Faculty Form','subtitle')
        
        _class=self.lable(MASTER,10, 120, 'Class')

        faculty=self.lable(MASTER,10, 160, 'Faculty')

        shift=self.lable(MASTER,10, 200, 'Shift')

        total_section=self.lable(MASTER,10, 240, 'Total Section')

        manage_subject=self.lable(MASTER,10, 280, 'Manage Subject')

        line(MASTER,0,320,270,5)

        period_info=self.lable(MASTER,10, 350, 'Period Form','subtitle')
        
        total_period=self.lable(MASTER,10, 390, 'Total Period')

        time=self.lable(MASTER,10, 430, 'Time')

        time_per_period=self.lable(MASTER,10, 470, 'Time Per Period')

        line(MASTER,0,550,270,5)

        option=self.lable(MASTER,10, 570, 'Tools','subtitle')

    def user(self):
        MASTER=self.USER
        font_=font('login_subtitle')
        font_.setBold(True)
        font_.setPointSize(30)

        title=self.lable(MASTER,10, 10, 'Welcome User')
        title.setStyleSheet('color:#7CCAFB')
        title.setFixedSize(300,50)
        title.setFont(font_)

        dummy_logo=self.lable(MASTER,50, 130,text='')
        dummy_logo.setPixmap( image(PhotoLib.get(28),'') )
        dummy_logo.setFixedSize(512,512)
       
        login_frame=self.frame(MASTER)

        login_title=self.lable(login_frame,170,50,'SIGN UP')
        login_title.setStyleSheet('color:#7CCAFB')
        login_title.setFont(font('login_title'))
        login_title.setFixedSize(200,30)

        name=self.lable(login_frame,25, 140, 'User Name:','subtitle')
        name.setStyleSheet('color:#73AAFA')
        name.setFont(font('login_subtitle'))
        name.setFixedWidth(200)

        email=self.lable(login_frame,25, 200, 'Email:','subtitle')
        email.setStyleSheet('color:#79C0FB')
        email.setFont(font('login_subtitle'))
        email.setFixedWidth(200)

        password=self.lable(login_frame,25, 260, 'Password:','subtitle')
        password.setStyleSheet('color:#74ADFA')
        password.setFont(font('login_subtitle'))
        password.setFixedWidth(200)

        college=self.lable(login_frame,25, 320, 'College:','subtitle')
        college.setStyleSheet('color:#74ADFA')
        college.setFont(font('login_subtitle'))
        college.setFixedWidth(200)

    def setting(self):
        MASTER=self.SETTING

        title=self.lable(MASTER,10, 10, 'Settings','title')

    def guid(self):
        MASTER=self.GUID

        title=self.lable(MASTER,10, 10, 'Guid','title')