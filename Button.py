from source import * 
from StyleSheet import NORMAL_BUTTON


class Button:
    def __init__(self,*arg):
        self.WINDOW,self.SIDEBAR,self.TIME_TABLE,self.PROFESSOR,self.SUBJECT=arg

        self.HEIGHT,self.WIDTH=36,36

        self.GRID_LAYOUT=QVBoxLayout()

        self.side_bar()



    def button(self,master,X,Y,HEIGHT,WIDTH,img,style=None,size=32,
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
        button.setGeometry(QRect(X,Y,HEIGHT,WIDTH))

        return button

    def side_bar(self):

        SIDEBAR_BUTTON=NORMAL_BUTTON+'QPushButton{background-color: #24292E;}'

        record=self.button(self.SIDEBAR,14, 30, self.HEIGHT,self.WIDTH,PhotoLib.get(10),
        size=24,style=SIDEBAR_BUTTON
        )

        professor=self.button(self.SIDEBAR,14, 90, self.HEIGHT,self.WIDTH,PhotoLib.get(8),
        size=24,style=SIDEBAR_BUTTON
        )
        self.professor(professor)

        subject=self.button(self.SIDEBAR,14, 150, self.HEIGHT,self.WIDTH,PhotoLib.get(9),
        size=24,style=SIDEBAR_BUTTON
        )
        
        time_table=self.button(self.SIDEBAR,14, 210, self.HEIGHT,self.WIDTH,PhotoLib.get(7),
        size=24,style=SIDEBAR_BUTTON
        )
        self.time_table(time_table)

        user=self.button(self.SIDEBAR,14, 585, self.HEIGHT,self.WIDTH,PhotoLib.get(12),
        size=28,style=SIDEBAR_BUTTON
        )
        
        setting=self.button(self.SIDEBAR,14, 645, self.HEIGHT,self.WIDTH,PhotoLib.get(13),
        size=28,style=SIDEBAR_BUTTON
        )

        guid=self.button(self.SIDEBAR,14, 695, self.HEIGHT,self.WIDTH,PhotoLib.get(15),
        size=28,style=SIDEBAR_BUTTON
        )

    def time_table(self,master):

        manage_subject=self.button(self.TIME_TABLE,150, 275,self.HEIGHT,self.WIDTH,PhotoLib.get(2),
        size=23,style=NORMAL_BUTTON)

        conform=self.button(self.TIME_TABLE,220, 500,self.HEIGHT+2,self.WIDTH+2,PhotoLib.get(6),
        size=32,style=NORMAL_BUTTON)
        
        save=self.button(self.TIME_TABLE,10, 610,self.HEIGHT,self.WIDTH,PhotoLib.get(18),
        size=20,style=NORMAL_BUTTON)

        email=self.button(self.TIME_TABLE,60, 610,self.HEIGHT,self.WIDTH,PhotoLib.get(3),
        size=28,style=NORMAL_BUTTON)


        master.clicked.connect(lambda:[
        self.TIME_TABLE.show(),
        self.PROFESSOR.hide(),
        self.SUBJECT.hide()])

    def professor(self,master):
        master.clicked.connect(lambda:[self.PROFESSOR.show(),self.TIME_TABLE.hide(),
        self.SUBJECT.hide()])