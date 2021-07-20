from Source import * 
from StyleSheet import NORMAL_BUTTON


class Button:
    def __init__(self,*arg):
        self.WINDOW, self.SIDEBAR, self.TIME_TABLE, self.PROFESSOR, self.SUBJECT, self.RECORD, self.USER, self.SETTING, self.GUID = arg

        self.AREA=36

        self.GRID_LAYOUT=QVBoxLayout()

        self.side_bar()

    def button(self,master,x,y,area,img,style=None,size=32,
    font_type='normal',text=''):

        button=QPushButton(text,master)
        button.setIcon(image( img ))
        button.setIconSize(QSize(size,size))
        button.pressed.connect(
            lambda:button.setIconSize(QSize(size-3,size-3))
            )
        button.released.connect(
            lambda:button.setIconSize(QSize(size,size))
            )
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

    def side_bar(self):

        SIDEBAR_BUTTON=NORMAL_BUTTON+'QPushButton{background-color: #24292E;}'

        record=self.button(self.SIDEBAR,14, 30, self.AREA,PhotoLib.get(10),
        size=24,style=SIDEBAR_BUTTON
        )
        record.setToolTip('Record')
        self.record(record)

        professor=self.button(self.SIDEBAR,14, 90, self.AREA,PhotoLib.get(8),
        size=24,style=SIDEBAR_BUTTON
        )
        professor.setToolTip('Professor')
        self.professor(professor)

        subject=self.button(self.SIDEBAR,14, 150, self.AREA,PhotoLib.get(9),
        size=24,style=SIDEBAR_BUTTON
        )
        subject.setToolTip('Subjects')
        self.subject(subject)
        
        time_table=self.button(self.SIDEBAR,14, 210, self.AREA,PhotoLib.get(7),
        size=24,style=SIDEBAR_BUTTON
        )
        time_table.setToolTip('Time Table')
        self.time_table(time_table)

        user=self.button(self.SIDEBAR,14, 585, self.AREA,PhotoLib.get(12),
        size=28,style=SIDEBAR_BUTTON
        )
        user.setToolTip('User')
        self.user(user)
        
        setting=self.button(self.SIDEBAR,14, 645, self.AREA,PhotoLib.get(13),
        size=28,style=SIDEBAR_BUTTON
        )
        setting.setToolTip('Setting')
        self.setting(setting)

        guid=self.button(self.SIDEBAR,14, 695, self.AREA,PhotoLib.get(15),
        size=28,style=SIDEBAR_BUTTON
        )
        guid.setToolTip('Guid')
        self.guid(guid)

    def record(self,master):

        master.clicked.connect(lambda:[
        self.RECORD.show(),
        self.USER.hide(),
        self.PROFESSOR.hide(),
        self.TIME_TABLE.hide(),
        self.SETTING.hide(),
        self.GUID.hide()])

    def professor(self,master):

        MASTER=self.PROFESSOR

        insert=self.button(MASTER,220,275,self.AREA,PhotoLib.get(25),
        size=28,style=NORMAL_BUTTON)

        pdf=self.button(MASTER,10, 388,self.AREA,PhotoLib.get(4),
        size=28,style=NORMAL_BUTTON)

        excle=self.button(MASTER, 60, 388,self.AREA,PhotoLib.get(27),
        size=28,style=NORMAL_BUTTON)

        master.clicked.connect(lambda:[
        self.PROFESSOR.show(),
        self.RECORD.hide(),
        self.USER.hide(),
        self.TIME_TABLE.hide(),
        self.SETTING.hide(),
        self.GUID.hide(),
        self.SUBJECT.hide()])
    
    def subject(self,master):

        MASTER=self.SUBJECT

        insert=self.button(MASTER,220,235,self.AREA,PhotoLib.get(25),
        size=28,style=NORMAL_BUTTON)

        pdf=self.button(MASTER, 10, 355,self.AREA,PhotoLib.get(4),
        size=28,style=NORMAL_BUTTON)
        
        excle=self.button(MASTER, 60, 355,self.AREA,PhotoLib.get(27),
        size=28,style=NORMAL_BUTTON)

        master.clicked.connect(lambda:[
        self.SUBJECT.show(),
        self.RECORD.hide(),
        self.PROFESSOR.hide(),
        self.TIME_TABLE.hide(),
        self.SETTING.hide(),
        self.GUID.hide(),
        self.USER.hide()])

    def time_table(self,master):
        MASTER=self.TIME_TABLE
        manage_subject=self.button(MASTER,150, 275,self.AREA,PhotoLib.get(2),
        size=23,style=NORMAL_BUTTON)

        conform=self.button(MASTER,220, 510,self.AREA+2,PhotoLib.get(6),
        size=28,style=NORMAL_BUTTON)
        
        save=self.button(MASTER,10, 610,self.AREA,PhotoLib.get(18),
        size=20,style=NORMAL_BUTTON)

        email=self.button(MASTER,60, 610,self.AREA,PhotoLib.get(3),
        size=28,style=NORMAL_BUTTON)

        pdf=self.button(MASTER, 110, 610,self.AREA,PhotoLib.get(4),
        size=28,style=NORMAL_BUTTON)
        
        excle=self.button(MASTER, 160, 610,self.AREA,PhotoLib.get(27),
        size=28,style=NORMAL_BUTTON)

        master.clicked.connect(lambda:[
        self.TIME_TABLE.show(),
        self.RECORD.hide(),
        self.PROFESSOR.hide(),
        self.USER.hide(),
        self.SETTING.hide(),
        self.GUID.hide(),
        self.SUBJECT.hide()])

    def user(self,master):

        MASTER=self.USER
        sign_up=self.button(MASTER, 1088, 581,self.AREA+5,PhotoLib.get(29),
        size=32,style=NORMAL_BUTTON+'''QPushButton{ border-radius: 20px;
        background-color:#191D20;}''')

        current_user=self.button(MASTER, 1230, 10,self.AREA+12,PhotoLib.get(30),
        size=46,style=NORMAL_BUTTON+'''QPushButton{ border-radius: 23px; 
        background-color:#191D20;}''')

        show_hide_pass=self.button(MASTER, 1014, 421,self.AREA,PhotoLib.get(31),
        size=20,style=NORMAL_BUTTON+'''QPushButton{ background-color:#191D20;}''')
        self.show_hide_password(show_hide_pass)

        generate_password=self.button(MASTER, 1054, 421,self.AREA,PhotoLib.get(33),
        size=22,style=NORMAL_BUTTON+'''QPushButton{ background-color:#191D20;}''')


        master.clicked.connect(lambda:[
        self.USER.show(),
        self.RECORD.hide(),
        self.PROFESSOR.hide(),
        self.TIME_TABLE.hide(),
        self.SETTING.hide(),
        self.GUID.hide(),
        self.SUBJECT.hide()])

    def setting(self,master):
        master.clicked.connect(lambda:[
        self.SETTING.show(),
        self.RECORD.hide(),
        self.PROFESSOR.hide(),
        self.TIME_TABLE.hide(),
        self.USER.hide(),
        self.GUID.hide(),
        self.SUBJECT.hide()])

    def guid(self,master):
        master.clicked.connect(lambda:[
        self.GUID.show(),
        self.RECORD.hide(),
        self.PROFESSOR.hide(),
        self.TIME_TABLE.hide(),
        self.SETTING.hide(),
        self.USER.hide(),
        self.SUBJECT.hide()])