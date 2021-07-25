from Source import *
from StyleSheet import *
from raw import PhotoLib

class Connect:

    def __init__(self,*arg):
        self.Lable=arg[0]
        self.Button=arg[1]
        self.Box=arg[2]

        self.lable_widget=self.Lable.Widget
        self.button_widget=self.Button.Widget
        self.box_widget=self.Box.Widget

        self.lable=self.Lable.lable
        self.button=self.Button.button
        self.spinbox=self.Box.spinbox
        self.entry=self.Box.entry
        self.combo_box=self.Box.combo_box

        self.general()
        self.security()

    def frame_manager(self,Frame):
        Frames = {'general':self.lable_widget['general_frame'],
        'security':self.lable_widget['security_frame']}

        for i in Frames:
            if Frame is Frames[i] : Frames[i].show()

            else : Frames[i].hide()

    def general(self):
        MASTER=self.lable_widget['general_frame']

        general_btw=self.button_widget['general_btw']
        general_btw.clicked.connect(lambda:self.frame_manager(MASTER))
        
        style=NORMAL_BUTTON+'QPushButton{ border:3px solid white; }'
        light_mode_btw=self.button(MASTER,10,50,0,
        img=PhotoLib.get(38), style=NORMAL_BUTTON,size=256
        )
        light_mode_btw.setFixedSize(356,356)
        light_mode_btw.move(65,160)
        light_mode_btw.clicked.connect(lambda:[ 
            light_mode_btw.setStyleSheet(style),dark_mode_btw.setStyleSheet(NORMAL_BUTTON) ])


        dark_mode_btw=self.button(MASTER,10,50,0,
        img=PhotoLib.get(39), style=style
        ,size=256)
        dark_mode_btw.setFixedSize(356,356)
        dark_mode_btw.move(525,160)
        dark_mode_btw.clicked.connect(lambda:[ 
            dark_mode_btw.setStyleSheet(style),light_mode_btw.setStyleSheet(NORMAL_BUTTON) ])

    
    def security(self):
        MASTER=self.lable_widget['security_frame']

        E_WIDTH,E_HEIGHT=190,30

        AREA = 36

        security_btw=self.button_widget['security_btw']
        security_btw.clicked.connect(lambda:self.frame_manager(MASTER))


        def entry():

            STYLE=LOGIN_ENTRY# use this when sys locked +'QLineEdit{ border-color:#26d815; }'

            current_password=self.entry(MASTER,368, 230, E_WIDTH, E_HEIGHT, STYLE)
            current_password.setPlaceholderText('Current Password')
            current_password.setFont(font('entry'))

            new_password=self.entry(MASTER,368, 310, E_WIDTH, E_HEIGHT, STYLE)
            new_password.setPlaceholderText('New Password')
            new_password.setFont(font('entry'))


            re_enter_password=self.entry(MASTER,368, 390, E_WIDTH, E_HEIGHT, STYLE)
            re_enter_password.setPlaceholderText('Re-Enter New Password')
            re_enter_password.setFont(font('entry'))

        def combo():
            list_encry_mtdh=['Normal', 'Strong']
            encry_mtdh=self.combo_box(MASTER, 855, 320, 90, 25, list_encry_mtdh)
            
            list_ask_password=['At starting only', 'Major security area', 'Every step']
            ask_password=self.combo_box(MASTER, 805, 380, 120, 25, list_ask_password)


        def button():

            STYLE=NORMAL_BUTTON+'QPushButton{ background-color:#191D20;}'

            current_password=self.button(MASTER, 565, 231,AREA,PhotoLib.get(31),
            size=20,style=STYLE)
            self.Button.show_hide_password(current_password)

            new_password=self.button(MASTER, 565, 311,AREA,PhotoLib.get(31),
            size=20,style=STYLE)
            self.Button.show_hide_password(new_password)

            password_generator=self.button(MASTER, 605, 311,AREA,PhotoLib.get(33),
            size=20,style=STYLE)
            
            re_enter_password=self.button(MASTER, 565, 391,AREA,PhotoLib.get(31),
            size=20,style=STYLE)
            self.Button.show_hide_password(re_enter_password)

            conform=self.button(MASTER, 310, 485, 0, img=PhotoLib.get(41) ,font_type='fancy_subtitle',
            size=20, text=' conform', style=STYLE)
            conform.setFixedSize(160,43)
            conform.setGraphicsEffect(shadow(40))

        entry()
        button()
        combo()