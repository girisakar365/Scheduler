'''
NOTE Extraction of "FRAMES" is done from Lable.py so all the LABLE WIDGET HANDLED BY MASTERS in Lable.py must not be
included here.
'''
from Source import *
from StyleSheet import *
from raw import PhotoLib

class Connect:

    def __init__(self,*arg):
        self.Lable, self.Button, self.Box = arg

        self.lable_widget = self.Lable.Widget
        self.button_widget = self.Button.Widget
        self.box_widget = self.Box.Widget

        self.lable = self.Lable.lable
        self.button = self.Button.button
        self.spinbox = self.Box.spinbox
        self.entry = self.Box.entry
        self.combo_box = self.Box.combo_box

        self.MASTER = self.lable_widget['frame']
        self.bar = self.lable_widget['scroll_bar']

        self.general()
        self.security()
        self.shortcut()
        # self.manage_account()

    def control_bar(self, value:int): self.bar.setValue( value )   

    def echo(self,button,entry):
        button.pressed.connect(
            lambda:[entry.setEchoMode(QLineEdit.Normal)]
            )
        button.released.connect(
            lambda:[entry.setEchoMode(QLineEdit.Password)]
            )

    def general(self):

        general_btw = self.button_widget['general_btw']
        
        style = NORMAL_BUTTON + 'QPushButton{ border:3px solid white; }'

        light_mode_btw = self.button(self.MASTER,10,50,0,
        img = PhotoLib.get(38), style = NORMAL_BUTTON,size = 256
        )
        light_mode_btw.setFixedSize(356,356)
        light_mode_btw.move(65,90)
        light_mode_btw.clicked.connect(lambda:[ 
            light_mode_btw.setStyleSheet(style),dark_mode_btw.setStyleSheet(NORMAL_BUTTON) ])
        
        light_mode_btw.enterEvent = lambda event: light_mode_btw.setFixedSize(360,360)
        light_mode_btw.leaveEvent = lambda event: light_mode_btw.setFixedSize(356,356)

        light_mode_lable = self.lable(self.MASTER, 200, 460, 'Light Mode','fancy_subtitle')


        dark_mode_btw = self.button(self.MASTER,10,50,0,img = PhotoLib.get(39), style = style, size = 256)
        dark_mode_btw.setFixedSize(356,356)
        dark_mode_btw.move(525,90)
        dark_mode_btw.clicked.connect(lambda:[ 
            dark_mode_btw.setStyleSheet(style),light_mode_btw.setStyleSheet(NORMAL_BUTTON) ])
        
        dark_mode_btw.enterEvent = lambda event: dark_mode_btw.setFixedSize(354,354)
        dark_mode_btw.leaveEvent = lambda event: dark_mode_btw.setFixedSize(356,356)

        dark_mode_lable = self.lable(self.MASTER, 660, 460, 'Dark Mode','fancy_subtitle')

        general_btw.clicked.connect( lambda: self.control_bar(0) ) 

    
    def security(self):

        E_WIDTH,E_HEIGHT = 190,30

        AREA = 36

        security_btw = self.button_widget['security_btw']

        line(self.MASTER, 480, 620, 'v', 350)

        def lable():
            system_status=self.lable(self.MASTER, 605, 680, 'System Status:', 'fancy_subtitle')
            
            encry_mthd=self.lable(self.MASTER, 605, 760, 'Encryption Method:', 'fancy_subtitle')
            
            ask_password=self.lable(self.MASTER, 605, 840, 'Ask Password:', 'fancy_subtitle')

            answer_ss = self.lable(self.MASTER, 785, 685, 'Unlocked', 'fancy_subtitle',
            'color:#d13429')

        def entry():

            STYLE = LOGIN_ENTRY# use this when sys locked  + 'QLineEdit{ border-color:#26d815; }'

            current_password = self.entry(self.MASTER, 80, 680, E_WIDTH, E_HEIGHT, STYLE)
            current_password.setPlaceholderText('Current Password')
            current_password.setFont(font('entry'))
            current_password.setEchoMode(QLineEdit.Password)

            new_password = self.entry(self.MASTER, 80, 760, E_WIDTH, E_HEIGHT, STYLE)
            new_password.setPlaceholderText('New Password')
            new_password.setFont(font('entry'))
            new_password.setEchoMode(QLineEdit.Password)

            re_enter_password = self.entry(self.MASTER, 80, 840, E_WIDTH, E_HEIGHT, STYLE)
            re_enter_password.setPlaceholderText('Re-Enter New Password')
            re_enter_password.setFont(font('entry'))
            re_enter_password.setEchoMode(QLineEdit.Password)

            return current_password, new_password, re_enter_password, self.box_widget['user_password_entry']

        def combo():
            list_encry_mtdh = ['Normal', 'Strong']
            encry_mtdh = self.combo_box(self.MASTER, 785, 765, 90, 25, list_encry_mtdh)
            
            list_ask_password = ['At starting only', 'Major security area', 'Every step']
            ask_password = self.combo_box(self.MASTER, 785, 840, 120, 25, list_ask_password)


        def button():

            current_password = self.button(self.MASTER, 285, 675, AREA, PhotoLib.get(31),
            size = 20,style = NORMAL_BUTTON)
            self.Button.show_hide_password(current_password)

            new_password = self.button(self.MASTER, 285, 760, AREA, PhotoLib.get(31),
            size = 20,style = NORMAL_BUTTON)
            self.Button.show_hide_password(new_password)

            password_generator = self.button(self.MASTER, 325, 760, AREA, PhotoLib.get(33),
            size = 20,style = NORMAL_BUTTON)
            
            re_enter_password = self.button(self.MASTER, 285, 840, AREA, PhotoLib.get(31),
            size = 20,style = NORMAL_BUTTON)
            self.Button.show_hide_password(re_enter_password)

            conform = self.button(self.MASTER,  80, 920, 0, img = PhotoLib.get(41) ,font_type = 'fancy_subtitle',
            size = 20, text = ' conform', style = NORMAL_BUTTON)
            conform.setFixedSize(160,43)
            
            conform.enterEvent = lambda event: conform.setFixedSize(164,45)
            conform.leaveEvent = lambda event: conform.setFixedSize(160,43)

            conform.setGraphicsEffect(shadow(40))

            return current_password, new_password, re_enter_password, self.button_widget['user_password_btw']

        lable()
        for button_,entry_ in zip(button(),entry()):
            self.echo(button_,entry_)
        combo()

        security_btw.clicked.connect(lambda: self.control_bar(532) )

    def shortcut(self):

        def lable():

            record = self.lable(self.MASTER, 0, 0, 'Record','fancy_subtitle')
            professor = self.lable(self.MASTER, 0, 0, 'Professor','fancy_subtitle')
            subject = self.lable(self.MASTER, 0, 0, 'Subject','fancy_subtitle')
            time_table = self.lable(self.MASTER, 0, 0, 'Time Table','fancy_subtitle')
            user = self.lable(self.MASTER, 0, 0, 'User','fancy_subtitle')
            guid = self.lable(self.MASTER, 0, 0, 'Guid','fancy_subtitle')
            manage_subject = self.lable(self.MASTER, 0, 0, 'Manage Subject','fancy_subtitle')
            email = self.lable(self.MASTER, 0, 0, 'Emailing','fancy_subtitle')

            return record, professor, subject, time_table, user, guid, manage_subject, email

        def entry():
            
            WIDTH,HEIGHT = 50,80

            record = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)
            professor = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)
            subject = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)
            time_table = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)
            user = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)
            guid = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)
            manage_subject = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)
            email = self.entry(self.MASTER, 0, 0, WIDTH, HEIGHT)

            for i in record, professor, subject, time_table, user, guid, manage_subject, email:
                i.setFixedSize(220,26)
                i.setFont(font('entry'))

            return record, professor, subject, time_table, user, guid, manage_subject, email

        lable()
 

        shortcut_btw = self.button_widget['shortcut_btw']
    
    def manage_account(self):
        
        MASTER = self.lable_widget['manage_account_frame']

        self.Master = self.lable_widget['manage_account_sub_frame']

        manage_account_btw = self.button_widget['manage_account_btw']
