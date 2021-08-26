try:
    from .Source import * 
    from .StyleSheet import LABLE, FRAME, SCROLL_BAR

except Exception:
    from Source import * 
    from StyleSheet import LABLE, FRAME, SCROLL_BAR


class Label:

    def __init__(self,*arg):
        
        self.WINDOW,self.SIDEBAR,self.TIME_TABLE,self.PROFESSOR,self.SUBJECT,self.RECORD,self.USER,self.SETTING,self.GUID = arg
        self.Widget={}

        self.record()
        self.professor()
        self.subject()
        self.time_table()
        self.user()
        self.setting()
        self.guid()

    def lable(self, master, x:int = 0 , y:int = 0, text='text', font_type='normal', style=LABLE):
        
        label=QLabel(text,master)
        label.setFont(font(font_type))
        label.setStyleSheet(style)
        label.setGeometry(QRect(x,y,0,0))
        label.adjustSize()
        
        return label

    def frame(self, master, w:int, h:int, style = FRAME):

        _frame = frame(master)
        _frame.setFixedSize(w,h) 
        _frame.setStyleSheet(style)
        _frame.setGraphicsEffect(shadow(65))

        return _frame

    def record(self):

        MASTER=self.RECORD

        title=self.lable(MASTER,10, 10, 'Records','title')

        empty=self.lable(MASTER, 401, 301, 'No Records Saved Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

    def professor(self):

        MASTER=self.PROFESSOR

        info_table=self.lable(MASTER,300,70,'Record of Professors','title')

        line(MASTER,270,0,'v')

        empty=self.lable(MASTER,501,301,'No Records Saved Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

        title=self.lable(MASTER,10, 10, 'Professor','title')

        form=self.lable(MASTER,10, 70, 'Entry Form','subtitle')
        
        name=self.lable(MASTER,10, 120, 'Name')
        
        email=self.lable(MASTER,10, 160, 'Email')
        
        subject=self.lable(MASTER,10, 200, 'Subject')
        
        classes=self.lable(MASTER,10, 240, 'Classes')

        line(MASTER,0,330,length=270)

        tool=self.lable(MASTER,10, 350, 'Tools','subtitle')

    def subject(self):

        MASTER=self.SUBJECT

        title=self.lable(MASTER,10, 3,'Subject','title')

        info=self.lable(MASTER,300,40,'Subject List','title')

        empty=self.lable(MASTER,501,301,'No Records Saved Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

        line(MASTER,270,0,'v')

        form=self.lable(MASTER,10, 70, 'Subject From','subtitle')
        
        sub_name=self.lable(MASTER,10, 120, 'Subject')
        
        faculty=self.lable(MASTER,10, 160, 'Faculty')
        
        class_=self.lable(MASTER,10, 200, 'Class')

        line(MASTER,0,280,length=270)

        tool=self.lable(MASTER,10, 310, 'Tools','subtitle')


    def time_table(self):

        MASTER=self.TIME_TABLE

        line(MASTER,270,0,'v')

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

        line(MASTER,0,320,length=270)

        period_info=self.lable(MASTER,10, 350, 'Period Form','subtitle')
        
        total_period=self.lable(MASTER,10, 390, 'Total Period')

        time=self.lable(MASTER,10, 430, 'Time')

        time_per_period=self.lable(MASTER,10, 470, 'Time Per Period')

        line(MASTER,0,550,length=270)

        option=self.lable(MASTER,10, 570, 'Tools','subtitle')

    def user(self):

        MASTER=self.USER
        font_=font('fancy_subtitle')
        font_.setBold(True)
        font_.setPointSize(30)

        title=self.lable(MASTER,10, 10, 'Welcome User')
        title.setStyleSheet('color:#7CCAFB')
        title.setFixedSize(300,50)
        title.setFont(font_)

        logo=self.lable(MASTER,50, 130,text='')
        logo.setPixmap( image(PhotoLib.get(28),'') )
        logo.setFixedSize(512,512)

        CHILD=self.frame(MASTER,480,480)
        CHILD.move(670,160)

        sub_title=self.lable(CHILD,170,50,'SIGN UP','fancy_title')
        sub_title.setStyleSheet('color:#7CCAFB')

        name=self.lable(CHILD,25, 140, 'User Name:','fancy_subtitle')
        name.setStyleSheet('color:#73AAFA')

        email=self.lable(CHILD,25, 200, 'Email:','fancy_subtitle')
        email.setStyleSheet('color:#79C0FB')

        password=self.lable(CHILD,25, 260, 'Password:','fancy_subtitle')
        password.setStyleSheet('color:#74ADFA')

        college=self.lable(CHILD,25, 320, 'College:','fancy_subtitle')
        college.setStyleSheet('color:#74ADFA')

    def setting(self):

        MASTER = self.SETTING

        title=self.lable(MASTER,10, 10, 'Settings','fancy_title')

        CHILD, SCROLLAREA = scroll_bar(MASTER)

        SCROLLAREA.move(260,65)
        SCROLLAREA.setFixedSize(1020, 668)
        bar = SCROLLAREA.verticalScrollBar()
        bar.setStyleSheet(SCROLL_BAR)

        layout = QVBoxLayout()
        layout.setSpacing(500)

        line(MASTER,0,65)

        line(MASTER,260,65,'v')

        general = self.lable(CHILD,400, 100, 'General','fancy_title')
        
        security = self.lable(CHILD,400, 100, 'Security','fancy_title')

        shortcut = self.lable(CHILD,400, 100, 'Manage Keyboard Shorcuts','fancy_title')
        
        manage_account = self.lable(CHILD, 10, 900, 'Manage Account','fancy_title')
        
        space = self.lable(CHILD, 10, 900, ' ','fancy_title')
        

        for i in general, security, shortcut, manage_account, space :
            layout.addWidget(i)

        CHILD.setLayout(layout)

        self.collect(frame = CHILD, scroll_bar = bar)

        # def manage_account():

        #     CHILD=self.frame(MASTER,955,620)
        #     CHILD.move(320,100)
        #     CHILD.hide()
            
        #     title_=self.lable(CHILD,20, 10, 'Manage Account','fancy_title')

        #     SUB_CHILD=frame(CHILD)
        #     SUB_CHILD.setFixedSize(805,820)
        #     SUB_CHILD.setStyleSheet('background-color: #ffffff')
        #     SUB_CHILD.move(100,60)
        #     SUB_CHILD.hide()


        #     self.collect(manage_account_frame=CHILD, manage_account_sub_frame=SUB_CHILD)

        # security()
        # shortcut()
        # manage_account()

    def guid(self):
        MASTER=self.GUID

        title=self.lable(MASTER,10, 10, 'Guid','title')

    def collect(self,**kwarg):

        for key,value in kwarg.items():
            self.Widget[key]=value