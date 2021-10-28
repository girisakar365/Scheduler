try:
    from .src import *
    from .Photo_Lib import * 

except Exception:
    from src import * 
    from Photo_Lib import *


class Button:
    def __init__(self,*arg):

        self.Widget = {}
        self.Ui = {"button":[],
        'l-button':[],
        'gear':[],
        'scope':[],
        'what':[],
        'user':[],
        'pen':[],
        'secure':[],
        'keyboard':[],
        'tick':[],
        'back':[],
        'mark':[],
        'generator':[],
        'next':[]
        }
        
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
            self.BAR,
            self.LOCK
             )  =  arg
            self.side_bar()
            self.lock()

        else:
            CHILD =  arg

        self.Widget['ui-theme'] = self.ui_theme

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
        radio.setStyleSheet(Style("RBUTTON"))
        radio.setCursor(QCursor(Qt.PointingHandCursor))
        radio.adjustSize()
        radio.move(x,y)

        return radio

    def check_button(self,master,text,x,y):
        check = QCheckBox(text,master)
        check.setStyleSheet(Style('RBUTTON'))
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
    
    def ui_theme(self):
        
        self.WINDOW.setStyleSheet(Style('WIDGET'))
        self.SIDEBAR.setStyleSheet(Style('SIDEBAR'))

        for side_bar_btw in self.Ui['side_bar']:
            side_bar_btw.setStyleSheet(Style('SBUTTON'))

        for normal_btw in self.Ui['button']:
            normal_btw.setStyleSheet(Style('NBUTTON'))

        for l_btw in self.Ui['l-button']:
            l_btw.setStyleSheet(Style('LBUTTON'))

        #ico-changes:
        for i in ['scope', 'user', 'gear', 'what', 'pen', 'mark', 'generator', 'next',
         'secure', 'keyboard', 'tick', 'back']:
            for j in self.Ui[i]:
                j.setIcon(ico(i.upper()))

    def side_bar(self):

        record = self.button(self.SIDEBAR,14, 30, self.AREA, RECORD,
        size = 24,style = Style('SBUTTON')
        )
        record.setToolTip('Record')
        self.record(record)

        professor = self.button(self.SIDEBAR,14, 90, self.AREA, PROFESSOR,
        size = 24,style = Style('SBUTTON')
        )
        professor.setToolTip('Professor')
        self.professor(professor)

        subject = self.button(self.SIDEBAR,14, 150, self.AREA, SUBJECT,
        size = 24,style = Style('SBUTTON')
        )
        subject.setToolTip('Subjects')
        self.subject(subject)
        
        time_table = self.button(self.SIDEBAR,14, 210, self.AREA, TIME_TABLE,
        size = 24,style = Style('SBUTTON')
        )
        time_table.setToolTip('Time Table')
        self.time_table(time_table)

        user = self.button(self.SIDEBAR,14, 585, self.AREA, ico('USER'),
        size = 28,style = Style('SBUTTON')
        )
        self.Ui['user'].append(user)
        user.setToolTip('User')
        self.user(user)
        
        setting = self.button(self.SIDEBAR,14, 645, self.AREA, ico('GEAR'),
        size = 28,style = Style('SBUTTON')
        )
        self.Ui['gear'].append(setting)
        setting.setToolTip('Setting')
        self.setting(setting)

        guid = self.button(self.SIDEBAR,14, 695, self.AREA, ico('WHAT'),
        size = 28,style = Style('SBUTTON')
        )
        self.Ui['what'].append(guid)
        guid.setToolTip('Guid')
        self.guid(guid)

        self.collect('ui',
        side_bar = [record,time_table,professor,subject,user,setting,guid]
        )

    def record(self,master):
        MASTER = self.RECORD
        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def professor(self,master):

        MASTER = self.PROFESSOR

        insert = self.button(MASTER,220,275,self.AREA, ico('NEXT'),
        size = 28,style =Style('NBUTTON') )
        self.Ui['next'].append(insert)

        pdf = self.button(MASTER,10, 388,self.AREA, PDF,
        size = 28,style =Style('NBUTTON') )

        excle = self.button(MASTER, 60, 388,self.AREA, XLSX,
        size = 28,style =Style('NBUTTON') )

        for i in [insert,pdf,excle]:
            self.Ui['button'].append(i)

        master.clicked.connect(lambda:self.frame_manager(MASTER))
    
    def subject(self,master):

        MASTER = self.SUBJECT

        insert = self.button(MASTER,220,255,self.AREA, ico('NEXT'),
        size = 28,style =Style('NBUTTON') )
        self.Ui['next'].append(insert)

        slot = self.button(MASTER, 80, 159, self.AREA, ico('PEN'),
        size = 20, style =Style('NBUTTON') )
        self.Ui['pen'].append(slot)

        self.collect(slot = slot)

        pdf = self.button(MASTER, 10, 355,self.AREA, PDF,
        size = 28,style =Style('NBUTTON') )
        
        excle = self.button(MASTER, 60, 355,self.AREA, XLSX,
        size = 28,style =Style('NBUTTON') )

        for i in [insert,pdf,excle,slot]:
            self.Ui['button'].append(i)

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def time_table(self,master):
        MASTER = self.TIME_TABLE
        manage_subject = self.button(MASTER,150, 275,self.AREA, ico('PEN'),
        size = 23,style =Style('NBUTTON') )
        self.Ui['pen'].append(manage_subject)
        
        self.collect(manage = manage_subject)

        conform = self.button(MASTER,220, 510,self.AREA+2, ico('GENERATOR'),
        size = 28,style =Style('NBUTTON') )
        self.Ui['generator'].append(conform)        
        
        save = self.button(MASTER,10, 610,self.AREA, ico('MARK'),
        size = 20,style =Style('NBUTTON') )
        self.Ui['mark'].append(save)

        email = self.button(MASTER,60, 610,self.AREA, MAIL,
        size = 28,style =Style('NBUTTON') )

        pdf = self.button(MASTER, 110, 610,self.AREA, PDF,
        size = 28,style =Style('NBUTTON') )
        
        excle = self.button(MASTER, 160, 610,self.AREA, XLSX,
        size = 28,style =Style('NBUTTON') )

        for i in [conform,save,email,pdf,excle,manage_subject,save]:
            self.Ui['button'].append(i)

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def user(self,master):

        MASTER = self.USER
        sign_up = self.button(MASTER, 1088, 581,self.AREA+5, LOGIN,
        size = 32,style =Style('LBUTTON') +'''QPushButton{ border-radius: 20px; }''')

        current_user = self.button(MASTER, 1200, 10,self.AREA+12, ACCOUNT, 
        size = 46,style = Style('LBUTTON')+'''QPushButton{ border-radius: 23px; }''')

        show_hide_pass  =  self.button(MASTER, 1014, 421,self.AREA, EYE_CLOSED,
        size  =  20,style = Style('LBUTTON'))
        self.show_hide_password(show_hide_pass)

        self.collect(up = show_hide_pass)
        
        for i in [sign_up,current_user,show_hide_pass]:
            self.Ui['l-button'].append(i)

        master.clicked.connect(lambda: self.frame_manager(MASTER))

    def setting(self,master):

        MASTER = self.SETTING
        CHILD = self.SETTING_CHILD

        master.clicked.connect(lambda:self.frame_manager(MASTER))

        MASTER.show()

        MENU_BAR_BUTTON =Style('NBUTTON') +'QPushButton{border-radius:20px;}'

        def button_animation(button,w:int,h:int):
            button.enterEvent = lambda event : button.setFixedSize(w+4,h+2)
            button.leaveEvent = lambda event : button.setFixedSize(w,h)

        search = self.button(MASTER, 1090, 18, self.AREA, ico('SCOPE'),
        size = 20, style =Style('NBUTTON') )
        self.Ui['scope'].append(search)

        general = self.button(MASTER,35, 130, 0, ico('GEAR'),
        size = 18,style = MENU_BAR_BUTTON,text = '  General')
        general.setFixedSize(150,43)
        self.Ui['gear'].append(general)

        security = self.button(MASTER, 35, 200, 0, ico('SECURE'), # changable
        size = 20,style = MENU_BAR_BUTTON,text = '  Security')
        security.setFixedSize(150,43)
        self.Ui['secure'].append(security)

        shortcut = self.button(MASTER, 35, 270, 0, ico('KEYBOARD'), # changable
        size = 20,style = MENU_BAR_BUTTON,text = '  Shortcuts')
        shortcut.setFixedSize(150,43)
        self.Ui['keyboard'].append(shortcut)

        manage_account = self.button(MASTER, 38, 340, 0, ico('USER'), # changable
        size = 20, style = MENU_BAR_BUTTON, text = '  Manage Account')
        manage_account.setFixedSize(158,43)
        self.Ui['user'].append(manage_account)

        for i in [general,security,shortcut,manage_account]:
            width  =  150
            height  =  43
            if i is manage_account:
                width  =  158
            button_animation(i,width,height)#only for elongated menu buttons

        def general_():

            light_mode_btw = self.button(CHILD,10,50,0,style=Style('NBUTTON'),
            img = UI_L,size = 256
            )
            light_mode_btw.setFixedSize(356,356)
            light_mode_btw.move(65,90)
            
            light_mode_btw.enterEvent = lambda event: light_mode_btw.setFixedSize(360,360)
            light_mode_btw.leaveEvent = lambda event: light_mode_btw.setFixedSize(356,356)

            dark_mode_btw = self.button(CHILD,10,50,0,img = UI_D, size = 256,style=Style('NBUTTON'))
            dark_mode_btw.setFixedSize(356,356)
            dark_mode_btw.move(525,90)

            self.Widget['dark-mode-btw'] = dark_mode_btw
            self.Widget['light-mode-btw'] = light_mode_btw
            
            dark_mode_btw.enterEvent = lambda event: dark_mode_btw.setFixedSize(354,354)
            dark_mode_btw.leaveEvent = lambda event: dark_mode_btw.setFixedSize(356,356)

        def security_():
            current_password = self.button(CHILD, 285, 675, self.AREA, EYE_CLOSED,
            size = 20,style =Style('NBUTTON') )
            self.show_hide_password(current_password)

            new_password = self.button(CHILD, 285, 760, self.AREA, EYE_CLOSED,
            size = 20,style =Style('NBUTTON') )
            self.show_hide_password(new_password)

            password_generator = self.button(CHILD, 325, 760, self.AREA, KEY,
            size = 20,style =Style('NBUTTON') )
            self.Widget['password-generator'] = password_generator
            
            re_enter_password = self.button(CHILD, 285, 840, self.AREA, EYE_CLOSED,
            size = 20,style =Style('NBUTTON') )
            self.show_hide_password(re_enter_password)

            conform = self.button(CHILD,  80, 920, 0, img = ico('TICK') ,font_type = 'fancy_subtitle',
            size = 20, text = ' conform', style =Style('NBUTTON') )
            conform.setFixedSize(160,43)
            self.Ui['tick'].append(conform)
            self.Widget['save-password'] = conform
            
            conform.enterEvent = lambda event: conform.setFixedSize(164,45)
            conform.leaveEvent = lambda event: conform.setFixedSize(160,43)

            conform.setGraphicsEffect(shadow(40))

            reset_password = self.button(CHILD, 785, 840, self.AREA, RESET, # changable
            size = 28,style = Style('NBUTTON'))
            self.Widget['reset-password'] = reset_password

            self.collect(
                cp = current_password, np = new_password, rep = re_enter_password
            )
            for i in [current_password,new_password,password_generator,re_enter_password
            ,conform, reset_password]:
                self.Ui['button'].append(i)

        def shortcut_():
            conform = self.button(CHILD,  690, 1440, 0, img = ico('TICK') ,font_type = 'fancy_subtitle',
            size = 20, text = ' Save Changes', style =Style('NBUTTON') )
            conform.setFixedSize(160,43)
            self.Ui['tick'].append(conform)
            
            conform.enterEvent = lambda event: conform.setFixedSize(164,45)
            conform.leaveEvent = lambda event: conform.setFixedSize(160,43)

            conform.setGraphicsEffect(shadow(40))

            self.Ui['button'].append(conform)

        general_()
        security_()
        shortcut_()

        for i in [search,general,security,shortcut,manage_account]:
            self.Ui['button'].append(i)

        general.clicked.connect( lambda: self.control_bar(0) )
        security.clicked.connect(lambda: self.control_bar(550) )
        shortcut.clicked.connect(lambda: self.control_bar( 1100 ))
        manage_account.clicked.connect(lambda: self.control_bar( self.BAR.maximum()))


    def guid(self,master):
        
        MASTER = self.GUID

        master.clicked.connect(lambda:self.frame_manager(MASTER))

    def lock(self):
        MASTER = self.LOCK
      
        log_in = self.button(MASTER, 543, 470, 0, ENTER,
        size = 20, style = Style('LBUTTON'), text = ' Log in')
        log_in.setFixedSize(250, 40)

        log_in.enterEvent = lambda event: log_in.setFixedSize(247,39)
        log_in.leaveEvent = lambda event: log_in.setFixedSize(250,40)

        log_in.setGraphicsEffect(shadow(40))

        eye  =  self.button(MASTER, 794, 419, self.AREA, EYE_CLOSED,
        size  =  20,style = Style('LBUTTON'))
        self.show_hide_password(eye)
        
        self.Widget['lb'] = eye

        self.Ui['l-button'].extend([log_in, eye])

        self.Widget['log-in'] = log_in

    def collect(self,key = '', **kwarg):
        
        if key == '':
            for key,value in kwarg.items():
                self.Widget[key] = value

        if key == 'ui':
            for key,value in kwarg.items():                        
                self.Ui[key] = value
