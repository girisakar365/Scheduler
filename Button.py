try:
    from .Source import * 
    from .StyleSheet import NORMAL_BUTTON

except Exception:
    from Source import * 
    from StyleSheet import NORMAL_BUTTON
class Button:
    def __init__(self,*arg):
        self.WINDOW,self.SIDEBAR,self.TIME_TABLE,self.PROFESSOR,self.SUBJECT,self.RECORD,self.USER,self.SETTING,self.GUID  =  arg

        self.Widget = {}
        
        self.AREA = 36

        self.side_bar()

    def button(self,master,x,y,area,img = None,style = None,size = 32,
    font_type = 'normal',text = ''):

        button = QPushButton(text,master)
        
        try:
            button.setIcon(image( img ))
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

    def show_hide_password(self,button):
        button.pressed.connect(
            lambda:[button.setIcon(image( PhotoLib.get(32) )),button.setIconSize(QSize(18,18))]
            )
        button.released.connect(
            lambda:[button.setIcon(image( PhotoLib.get(31) )),button.setIconSize(QSize(20,20))]
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

        record = self.button(self.SIDEBAR,14, 30, self.AREA,PhotoLib.get(10),
        size = 24,style = SIDEBAR_BUTTON
        )
        record.setToolTip('Record')
        self.record(record)

        professor = self.button(self.SIDEBAR,14, 90, self.AREA,PhotoLib.get(8),
        size = 24,style = SIDEBAR_BUTTON
        )
        professor.setToolTip('Professor')
        self.professor(professor)

        subject = self.button(self.SIDEBAR,14, 150, self.AREA,PhotoLib.get(9),
        size = 24,style = SIDEBAR_BUTTON
        )
        subject.setToolTip('Subjects')
        self.subject(subject)
        
        time_table = self.button(self.SIDEBAR,14, 210, self.AREA,PhotoLib.get(7),
        size = 24,style = SIDEBAR_BUTTON
        )
        time_table.setToolTip('Time Table')
        self.time_table(time_table)

        user = self.button(self.SIDEBAR,14, 585, self.AREA,PhotoLib.get(12),
        size = 28,style = SIDEBAR_BUTTON
        )
        user.setToolTip('User')
        self.user(user)
        
        setting = self.button(self.SIDEBAR,14, 645, self.AREA,PhotoLib.get(13),
        size = 28,style = SIDEBAR_BUTTON
        )
        setting.setToolTip('Setting')
        self.setting(setting)

        guid = self.button(self.SIDEBAR,14, 695, self.AREA,PhotoLib.get(15),
        size = 28,style = SIDEBAR_BUTTON
        )
        guid.setToolTip('Guid')
        self.guid(guid)

    def record(self,master):
        MASTER = self.RECORD
        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def professor(self,master):

        MASTER = self.PROFESSOR

        insert = self.button(MASTER,220,275,self.AREA,PhotoLib.get(25),
        size = 28,style = NORMAL_BUTTON)

        pdf = self.button(MASTER,10, 388,self.AREA,PhotoLib.get(4),
        size = 28,style = NORMAL_BUTTON)

        excle = self.button(MASTER, 60, 388,self.AREA,PhotoLib.get(27),
        size = 28,style = NORMAL_BUTTON)

        master.clicked.connect(lambda:self.frame_manager(MASTER))
    
    def subject(self,master):

        MASTER = self.SUBJECT

        insert = self.button(MASTER,220,235,self.AREA,PhotoLib.get(25),
        size = 28,style = NORMAL_BUTTON)

        pdf = self.button(MASTER, 10, 355,self.AREA,PhotoLib.get(4),
        size = 28,style = NORMAL_BUTTON)
        
        excle = self.button(MASTER, 60, 355,self.AREA,PhotoLib.get(27),
        size = 28,style = NORMAL_BUTTON)

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def time_table(self,master):
        MASTER = self.TIME_TABLE
        manage_subject = self.button(MASTER,150, 275,self.AREA,PhotoLib.get(2),
        size = 23,style = NORMAL_BUTTON)

        conform = self.button(MASTER,220, 510,self.AREA+2,PhotoLib.get(6),
        size = 28,style = NORMAL_BUTTON)
        
        save = self.button(MASTER,10, 610,self.AREA,PhotoLib.get(18),
        size = 20,style = NORMAL_BUTTON)

        email = self.button(MASTER,60, 610,self.AREA,PhotoLib.get(3),
        size = 28,style = NORMAL_BUTTON)

        pdf = self.button(MASTER, 110, 610,self.AREA,PhotoLib.get(4),
        size = 28,style = NORMAL_BUTTON)
        
        excle = self.button(MASTER, 160, 610,self.AREA,PhotoLib.get(27),
        size = 28,style = NORMAL_BUTTON)

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def user(self,master):

        MASTER = self.USER
        sign_up = self.button(MASTER, 1088, 581,self.AREA+5,PhotoLib.get(29),
        size = 32,style = NORMAL_BUTTON+'''QPushButton{ border-radius: 20px;
        background-color:#191D20;}''')

        current_user = self.button(MASTER, 1230, 10,self.AREA+12,PhotoLib.get(30),
        size = 46,style = NORMAL_BUTTON+'''QPushButton{ border-radius: 23px; 
        background-color:#191D20;}''')

        show_hide_pass  =  self.button(MASTER, 1014, 421,self.AREA,PhotoLib.get(31),
        size  =  20,style  =  NORMAL_BUTTON+'''QPushButton{ background-color:#191D20;}''')
        self.show_hide_password(show_hide_pass)

        self.collect(user_password_btw = show_hide_pass)

        master.clicked.connect(lambda: self.frame_manager(MASTER))

    def setting(self,master):

        MASTER = self.SETTING

        master.clicked.connect(lambda:self.frame_manager(MASTER))

        MASTER.show()

        MENU_BAR_BUTTON = NORMAL_BUTTON+'QPushButton{border-radius:20px;}'

        def button_animation(button,w:int,h:int):
            button.enterEvent = lambda event : button.setFixedSize(w+4,h+2)
            button.leaveEvent = lambda event : button.setFixedSize(w,h)

        search = self.button(MASTER, 1090, 18, self.AREA, PhotoLib.get(44),
        size = 20, style = NORMAL_BUTTON)

        general = self.button(MASTER,35, 130, 0, PhotoLib.get(13),
        size = 18,style = MENU_BAR_BUTTON,text = '  General')
        general.setFixedSize(150,43)

        security = self.button(MASTER, 35, 200, 0, PhotoLib.get(35),
        size = 20,style = MENU_BAR_BUTTON,text = '  Security')
        security.setFixedSize(150,43)

        shorcut = self.button(MASTER, 35, 270, 0, PhotoLib.get(37),
        size = 20,style = MENU_BAR_BUTTON,text = '  Shortcuts')
        shorcut.setFixedSize(150,43)

        manage_account = self.button(MASTER, 38, 340, 0, PhotoLib.get(12),
        size = 20, style = MENU_BAR_BUTTON, text = '  Manage Account')
        manage_account.setFixedSize(158,43)

        for i in [general,security,shorcut,manage_account]:
            width  =  150
            height  =  43
            if i is manage_account:
                width  =  158
            button_animation(i,width,height)#only for elongated menu buttons

        self.collect(general_btw = general, security_btw = security, shortcut_btw = shorcut,
        manage_account_btw = manage_account)

    def guid(self,master):
        
        MASTER = self.GUID

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def collect(self,**kwarg):

        for key,value in kwarg.items():
            self.Widget[key] = value