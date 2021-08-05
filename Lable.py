from Source import * 
from StyleSheet import LABLE, FRAME

class Label:

    def __init__(self,*arg):
        
        self.WINDOW,self.SIDEBAR,self.TIME_TABLE,self.PROFESSOR,self.SUBJECT,self.RECORD,self.USER,self.SETTING,self.GUID,self.MENU_BAR = arg
        self.Widget={}

        self.record()
        self.professor()
        self.subject()
        self.time_table()
        self.user()
        self.setting()
        self.guid()

    def lable(self,master,x,y,text,font_type='normal',style=LABLE):
        
        label=QLabel(text,master)
        label.setFont(font(font_type))
        label.setStyleSheet(style)
        label.setGeometry(QRect(x,y,0,0))
        label.adjustSize()
        
        return label

    def frame(self,master,w:int,h:int):
        _frame=frame(master)
        _frame.setFixedSize(w,h) 
        _frame.setStyleSheet(FRAME)
        _frame.setGraphicsEffect(shadow(65))

        return _frame

    def record(self):
        MASTER=self.RECORD

        title=self.lable(MASTER,10, 10, 'Records','title')

        empty=self.lable(MASTER,401,301,'No Records Saved Yet!','huge')
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
        MASTER=self.SETTING

        CHILD=self.MENU_BAR

        title=self.lable(MASTER,10, 10, 'Settings','fancy_title')

        menu_bar_title=self.lable(CHILD,90, 10, 'Menu','fancy_title')

        self.lable(MASTER,620,360,'Choose An Option','fancy_huge','color:#6A737D')

        def general():
            CHILD=self.frame(MASTER,945,620)
            CHILD.move(330,100)
            CHILD.hide()

            title_=self.lable(CHILD,20, 10, 'General','fancy_title')

            ui_theme=self.lable(CHILD,400, 100, 'Ui Theme','fancy_title')

            light_mode=self.lable(CHILD,196, 540, 'Light Mode','subtitle')
            
            dark_mode=self.lable(CHILD,676, 540, 'Dark Mode','subtitle')

            self.collect(general_frame=CHILD)
        
        def security():
            CHILD=self.frame(MASTER,955,620)
            CHILD.move(320,100)
            CHILD.hide()

            title_=self.lable(CHILD,20, 10, 'Security','fancy_title')

            lock_system=self.lable(CHILD,270, 100, 'Lock System','fancy_title')

            current_password=self.lable(CHILD,155, 230, 'Current Password:','fancy_subtitle')

            new_password=self.lable(CHILD,155, 310, 'New Password:','fancy_subtitle')

            re_enter_password=self.lable(CHILD,155, 390, 'Re-Enter New Password:','fancy_subtitle')

            line(CHILD,656,-10,'v')
            
            status=self.lable(CHILD,755, 170, 'Status','fancy_title')

            system_status=self.lable(CHILD,675, 260, 'System Status:','fancy_subtitle')
            
            encry_mthd=self.lable(CHILD,675, 320, 'Encryption Method:','fancy_subtitle')

            ask_password=self.lable(CHILD,675, 380, 'Ask Password:','fancy_subtitle')
            
            answer_ss = self.lable(CHILD,855, 260, 'Unlocked','fancy_subtitle',
            'color:#d13429')

            self.collect(security_frame=CHILD)

        def shortcut():
            CHILD=self.frame(MASTER,955,620)
            CHILD.move(320,100)
            CHILD.hide()

            SUB_CHILD=frame(CHILD)
            SUB_CHILD.setFixedSize(805,820)
            SUB_CHILD.move(120,160)

            title_=self.lable(CHILD,20, 10, 'Manage Keyboard Shortcuts','fancy_title')

            self.collect(shortcut_frame=CHILD, shortcut_sub_frame=SUB_CHILD)

        def manage_account():
            CHILD=self.frame(MASTER,955,620)
            CHILD.move(320,100)
            CHILD.hide()
            
            title_=self.lable(CHILD,20, 10, 'Manage Account','fancy_title')

            SUB_CHILD=frame(CHILD)
            SUB_CHILD.setFixedSize(805,820)
            SUB_CHILD.setStyleSheet('background-color: #ffffff')
            SUB_CHILD.move(100,60)
            SUB_CHILD.hide()

            self.lable(CHILD,260,250,'No account signed in.','fancy_huge','color:#6A737D')


            self.collect(manage_account_frame=CHILD, manage_account_sub_frame=SUB_CHILD)

        general()
        security()
        shortcut()
        manage_account()

    def guid(self):
        MASTER=self.GUID

        title=self.lable(MASTER,10, 10, 'Guid','title')

    def collect(self,**kwarg):

        for key,value in kwarg.items():
            self.Widget[key]=value