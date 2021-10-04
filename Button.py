try:
    from .Source import *
    from .Photo_Lib import * 

except Exception:
    from Source import * 
    from Photo_Lib import *
    
class Button:
    def __init__(self,*arg):

        self.Widget = {}
        
        self.AREA = 36
        
        if len(arg) > 1:
            (self.WINDOW,
            self.SIDEBAR,
            self.TIME_TABLE,
            self.PROFESSOR,
            self.SUBJECT,
            self.RECORD,
            self.USER,
            self.SETTING,
            self.GUID,
             self.SETTING_CHILD,
             self.BAR
             )  =  arg
            self.side_bar()

        else:
            CHILD =  arg

    def button(self,master,x,y,area,img = None,style = None,size = 32,
    font_type = 'normal',text = ''):

        button = QPushButton(text,master)
        
        try:
            button.setIcon(img)
            button.setIconSize(QSize(size,size))
            button.pressed.connect(
                lambda:button.setIconSize(QSize(size-3,size-3))
                )
            button.released.connect(
                lambda:button.setIconSize(QSize(size,size))
                )

        except Exception:pass

        button.enterEvent  = lambda event : button.setFixedSize(area+4,area+2)
        button.leaveEvent  = lambda event : button.setFixedSize(area,area)

        button.setFont(font(font_type))
        button.setStyleSheet(style)
        button.setCursor(QCursor(Qt.PointingHandCursor))
        button.setGeometry(QRect(x,y,area,area))

        return button

    def radio_button(self,master,text,x,y):
        radio = QRadioButton(text,master)
        radio.setStyleSheet('font-size:12px; color: white;')
        radio.setCursor(QCursor(Qt.PointingHandCursor))
        radio.adjustSize()
        radio.move(x,y)

        return radio

    def check_button(self,master,text,x,y):
        check = QCheckBox(text,master)
        check.setStyleSheet('font-size:12px; color: white;')
        check.setCursor(QCursor(Qt.PointingHandCursor))
        check.move(x,y)
        check.adjustSize()
        
        return check

    def control_bar(self, value:int): self.BAR.setValue( value )

    def show_hide_password(self,button):
        button.pressed.connect(
            lambda:[button.setIcon(EYE_OPENED),button.setIconSize(QSize(18,18))]
            )
        button.released.connect(
            lambda:[button.setIcon( EYE_CLOSED ),button.setIconSize(QSize(20,20))]
            )
    
    def frame_manager(self,Frame):

        Frames  =  {'record':self.RECORD,
        'professor':self.PROFESSOR,
        'subject':self.SUBJECT,
        'time_table':self.TIME_TABLE,
        'user':self.USER,
        'settings':self.SETTING,
        'guid':self.GUID,
        }
        for i in Frames:
            if Frame is Frames[i] : Frames[i].show()

            else : Frames[i].hide()

    def side_bar(self):

        SIDEBAR_BUTTON = NORMAL_BUTTON + 'QPushButton{background-color: #24292E;}'

        record = self.button(self.SIDEBAR,14, 30, self.AREA, RECORD,
        size = 24,style = SIDEBAR_BUTTON
        )
        record.setToolTip('Record')
        self.record(record)

        professor = self.button(self.SIDEBAR,14, 90, self.AREA, PROFESSOR,
        size = 24,style = SIDEBAR_BUTTON
        )
        professor.setToolTip('Professor')
        self.professor(professor)

        subject = self.button(self.SIDEBAR,14, 150, self.AREA, SUBJECT,
        size = 24,style = SIDEBAR_BUTTON
        )
        subject.setToolTip('Subjects')
        self.subject(subject)
        
        time_table = self.button(self.SIDEBAR,14, 210, self.AREA, TIME_TABLE,
        size = 24,style = SIDEBAR_BUTTON
        )
        time_table.setToolTip('Time Table')
        self.time_table(time_table)

        user = self.button(self.SIDEBAR,14, 585, self.AREA, USER_L, # changable
        size = 28,style = SIDEBAR_BUTTON
        )
        user.setToolTip('User')
        self.user(user)
        
        setting = self.button(self.SIDEBAR,14, 645, self.AREA, GEAR_L, # changable
        size = 28,style = SIDEBAR_BUTTON
        )
        setting.setToolTip('Setting')
        self.setting(setting)

        guid = self.button(self.SIDEBAR,14, 695, self.AREA, WHAT_L, # changable
        size = 28,style = SIDEBAR_BUTTON
        )
        guid.setToolTip('Guid')
        self.guid(guid)

    def record(self,master):
        MASTER = self.RECORD
        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def professor(self,master):

        MASTER = self.PROFESSOR

        insert = self.button(MASTER,220,275,self.AREA, NEXT_L, # changable
        size = 28,style = NORMAL_BUTTON)

        pdf = self.button(MASTER,10, 388,self.AREA, PDF,
        size = 28,style = NORMAL_BUTTON)

        excle = self.button(MASTER, 60, 388,self.AREA, XLSX,
        size = 28,style = NORMAL_BUTTON)

        master.clicked.connect(lambda:self.frame_manager(MASTER))
    
    def subject(self,master):

        MASTER = self.SUBJECT

        insert = self.button(MASTER,220,255,self.AREA, NEXT_L, # changable
        size = 28,style = NORMAL_BUTTON)

        slot = self.button(MASTER, 80, 159, self.AREA, PEN_L,
        size = 20, style = NORMAL_BUTTON)

        self.collect(slot = slot)

        pdf = self.button(MASTER, 10, 355,self.AREA, PDF,
        size = 28,style = NORMAL_BUTTON)
        
        excle = self.button(MASTER, 60, 355,self.AREA, XLSX,
        size = 28,style = NORMAL_BUTTON)

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def time_table(self,master):
        MASTER = self.TIME_TABLE
        manage_subject = self.button(MASTER,150, 275,self.AREA, PEN_L,# changable
        size = 23,style = NORMAL_BUTTON)
        
        self.collect(manage = manage_subject)

        conform = self.button(MASTER,220, 510,self.AREA+2, GENERATE_L, # changable
        size = 28,style = NORMAL_BUTTON)
        
        save = self.button(MASTER,10, 610,self.AREA, MARK_L, # changable
        size = 20,style = NORMAL_BUTTON)

        email = self.button(MASTER,60, 610,self.AREA, MAIL,
        size = 28,style = NORMAL_BUTTON)

        pdf = self.button(MASTER, 110, 610,self.AREA, PDF,
        size = 28,style = NORMAL_BUTTON)
        
        excle = self.button(MASTER, 160, 610,self.AREA, XLSX,
        size = 28,style = NORMAL_BUTTON)

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def user(self,master):

        MASTER = self.USER
        sign_up = self.button(MASTER, 1088, 581,self.AREA+5, LOGIN,
        size = 32,style = NORMAL_BUTTON+'''QPushButton{ border-radius: 20px;
        background-color:#191D20;}''')

        current_user = self.button(MASTER, 1200, 10,self.AREA+12, ACCOUNT, 
        size = 46,style = NORMAL_BUTTON+'''QPushButton{ border-radius: 23px; 
        background-color:#191D20;}''')

        show_hide_pass  =  self.button(MASTER, 1014, 421,self.AREA, EYE_CLOSED,
        size  =  20,style  =  NORMAL_BUTTON+'''QPushButton{ background-color:#191D20;}''')
        self.show_hide_password(show_hide_pass)

        self.collect(up = show_hide_pass)

        master.clicked.connect(lambda: self.frame_manager(MASTER))

    def setting(self,master):

        MASTER = self.SETTING
        CHILD = self.SETTING_CHILD

        master.clicked.connect(lambda:self.frame_manager(MASTER))

        MASTER.show()

        MENU_BAR_BUTTON = NORMAL_BUTTON+'QPushButton{border-radius:20px;}'

        def button_animation(button,w:int,h:int):
            button.enterEvent = lambda event : button.setFixedSize(w+4,h+2)
            button.leaveEvent = lambda event : button.setFixedSize(w,h)

        search = self.button(MASTER, 1090, 18, self.AREA, SCOPE_L, # changable
        size = 20, style = NORMAL_BUTTON)

        general = self.button(MASTER,35, 130, 0, GEAR_L, # changable
        size = 18,style = MENU_BAR_BUTTON,text = '  General')
        general.setFixedSize(150,43)

        security = self.button(MASTER, 35, 200, 0, SECURE_L, # changable
        size = 20,style = MENU_BAR_BUTTON,text = '  Security')
        security.setFixedSize(150,43)

        shortcut = self.button(MASTER, 35, 270, 0, KEYBOARD_L, # changable
        size = 20,style = MENU_BAR_BUTTON,text = '  Shortcuts')
        shortcut.setFixedSize(150,43)

        manage_account = self.button(MASTER, 38, 340, 0, USER_L, # changable
        size = 20, style = MENU_BAR_BUTTON, text = '  Manage Account')
        manage_account.setFixedSize(158,43)

        for i in [general,security,shortcut,manage_account]:
            width  =  150
            height  =  43
            if i is manage_account:
                width  =  158
            button_animation(i,width,height)#only for elongated menu buttons

        def general_():

            style = NORMAL_BUTTON + 'QPushButton{ border:3px solid white; }'

            light_mode_btw = self.button(CHILD,10,50,0,
            img = UI_L, style = NORMAL_BUTTON,size = 256
            )
            light_mode_btw.setFixedSize(356,356)
            light_mode_btw.move(65,90)
            light_mode_btw.clicked.connect(lambda:[ 
                light_mode_btw.setStyleSheet(style),dark_mode_btw.setStyleSheet(NORMAL_BUTTON) ])
            
            light_mode_btw.enterEvent = lambda event: light_mode_btw.setFixedSize(360,360)
            light_mode_btw.leaveEvent = lambda event: light_mode_btw.setFixedSize(356,356)

            dark_mode_btw = self.button(CHILD,10,50,0,img = UI_D, style = style, size = 256)
            dark_mode_btw.setFixedSize(356,356)
            dark_mode_btw.move(525,90)
            dark_mode_btw.clicked.connect(lambda:[ 
                dark_mode_btw.setStyleSheet(style),light_mode_btw.setStyleSheet(NORMAL_BUTTON) ])
            
            dark_mode_btw.enterEvent = lambda event: dark_mode_btw.setFixedSize(354,354)
            dark_mode_btw.leaveEvent = lambda event: dark_mode_btw.setFixedSize(356,356)

        def security_():
            current_password = self.button(CHILD, 285, 675, self.AREA, EYE_CLOSED,
            size = 20,style = NORMAL_BUTTON)
            self.show_hide_password(current_password)

            new_password = self.button(CHILD, 285, 760, self.AREA, EYE_CLOSED,
            size = 20,style = NORMAL_BUTTON)
            self.show_hide_password(new_password)

            password_generator = self.button(CHILD, 325, 760, self.AREA, KEY,
            size = 20,style = NORMAL_BUTTON)
            
            re_enter_password = self.button(CHILD, 285, 840, self.AREA, EYE_CLOSED,
            size = 20,style = NORMAL_BUTTON)
            self.show_hide_password(re_enter_password)

            conform = self.button(CHILD,  80, 920, 0, img = TICK_L ,font_type = 'fancy_subtitle',
            size = 20, text = ' conform', style = NORMAL_BUTTON)
            conform.setFixedSize(160,43)
            
            conform.enterEvent = lambda event: conform.setFixedSize(164,45)
            conform.leaveEvent = lambda event: conform.setFixedSize(160,43)

            conform.setGraphicsEffect(shadow(40))

            self.collect(
                cp = current_password, np = new_password, rep = re_enter_password
            )

        def shortcut_():
            conform = self.button(CHILD,  690, 1440, 0, img = TICK_L ,font_type = 'fancy_subtitle',
            size = 20, text = ' Save Changes', style = NORMAL_BUTTON)
            conform.setFixedSize(160,43)
            
            conform.enterEvent = lambda event: conform.setFixedSize(164,45)
            conform.leaveEvent = lambda event: conform.setFixedSize(160,43)

            conform.setGraphicsEffect(shadow(40))

        general_()
        security_()
        shortcut_()

        general.clicked.connect( lambda: self.control_bar(0) )
        security.clicked.connect(lambda: self.control_bar(550) )
        shortcut.clicked.connect(lambda: self.control_bar( 1100 ))
        manage_account.clicked.connect(lambda: self.control_bar( self.BAR.maximum()))


    def guid(self,master):
        
        MASTER = self.GUID

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def collect(self, *arg, **kwarg):

        for key,value in kwarg.items():
            self.Widget[key] = value