from source import * 
from StyleSheet import NORMAL_BUTTON


class Button:
    def __init__(self,*arg):
        self.WINDOW, self.SIDEBAR, self.TIME_TABLE, self.PROFESSOR, self.SUBJECT, self.RECORD = arg

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

    def side_bar(self):

        SIDEBAR_BUTTON=NORMAL_BUTTON+'QPushButton{background-color: #24292E;}'

        record=self.button(self.SIDEBAR,14, 30, self.AREA,PhotoLib.get(10),
        size=24,style=SIDEBAR_BUTTON
        )
        self.record(record)

        professor=self.button(self.SIDEBAR,14, 90, self.AREA,PhotoLib.get(8),
        size=24,style=SIDEBAR_BUTTON
        )
        self.professor(professor)

        subject=self.button(self.SIDEBAR,14, 150, self.AREA,PhotoLib.get(9),
        size=24,style=SIDEBAR_BUTTON
        )
        self.subject(subject)
        
        time_table=self.button(self.SIDEBAR,14, 210, self.AREA,PhotoLib.get(7),
        size=24,style=SIDEBAR_BUTTON
        )
        self.time_table(time_table)

        user=self.button(self.SIDEBAR,14, 585, self.AREA,PhotoLib.get(12),
        size=28,style=SIDEBAR_BUTTON
        )
        
        setting=self.button(self.SIDEBAR,14, 645, self.AREA,PhotoLib.get(13),
        size=28,style=SIDEBAR_BUTTON
        )

        guid=self.button(self.SIDEBAR,14, 695, self.AREA,PhotoLib.get(15),
        size=28,style=SIDEBAR_BUTTON
        )

    def record(self,master):

        master.clicked.connect(lambda:[
        self.RECORD.show(),
        self.PROFESSOR.hide(),
        self.TIME_TABLE.hide(),
        self.SUBJECT.hide()])

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
        self.SUBJECT.hide(),
        self.TIME_TABLE.hide(),
        self.RECORD.hide()])

    
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
        self.RECORD.hide()])
        self.PROFESSOR.hide(),
        self.TIME_TABLE.hide(),

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
        self.PROFESSOR.hide(),
        self.SUBJECT.hide(),
        self.RECORD.hide()])
