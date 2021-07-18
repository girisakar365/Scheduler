from source import * 
from StyleSheet import LABLE

class Label:

    def __init__(self,*arg):
        
        self.WINDOW, self.SIDEBAR, self.TIME_TABLE, self.PROFESSOR, self.SUBJECT, self.RECORD = arg
        
        self.professor()
        self.subject()
        self.time_table()

    def lable(self,master,X,Y,HEIGHT,WIDTH,text,font_type='normal'):
        
        label=QLabel(text,master)
        label.setFont(font(font_type))
        label.setStyleSheet(LABLE)
        label.setGeometry(QRect(X,Y,HEIGHT,WIDTH))
        
        return label

    def professor(self):
        WIDTH,HEIGHT=166, 28
        MASTER=self.PROFESSOR

        info_table=self.lable(MASTER,300,70,WIDTH+120,HEIGHT,'Record of Professors','title')

        line(MASTER,270,0,10,1000,'v')

        title=self.lable(MASTER,10, 10, WIDTH,HEIGHT,'Professor','title')

        form=self.lable(MASTER,10, 70, WIDTH,HEIGHT,'Entry Form','subtitle')
        
        name=self.lable(MASTER,10, 120, WIDTH,HEIGHT,'Name')
        
        email=self.lable(MASTER,10, 160, WIDTH,HEIGHT,'Email')
        
        subject=self.lable(MASTER,10, 200, WIDTH,HEIGHT,'Subject')
        
        classes=self.lable(MASTER,10, 240, WIDTH,HEIGHT,'Classes')

        line(MASTER,0,330,270,5)

        tool=self.lable(MASTER,10, 350, WIDTH,HEIGHT,'Tools','subtitle')

    def subject(self):
        WIDTH,HEIGHT=166, 28
        MASTER=self.SUBJECT

        title=self.lable(MASTER,10, 10, WIDTH,HEIGHT,'Subject','title')

        info=self.lable(MASTER,300,50,WIDTH+120,HEIGHT+50,'Subject List','title')

        line(MASTER,270,0,10,1000,'v')

        form=self.lable(MASTER,10, 70, WIDTH,HEIGHT,'Subject From','subtitle')
        
        sub_name=self.lable(MASTER,10, 120, WIDTH,HEIGHT,'Subject')
        
        faculty=self.lable(MASTER,10, 160, WIDTH,HEIGHT,'Faculty')
        
        class_=self.lable(MASTER,10, 200, WIDTH,HEIGHT,'Class')

        line(MASTER,0,280,270,5)

        tool=self.lable(MASTER,10, 310, WIDTH,HEIGHT,'Tools','subtitle')


    def time_table(self):
        
        WIDTH,HEIGHT=166, 28
        MASTER=self.TIME_TABLE

        line(MASTER,270,0,10,1000,'v')

        title=self.lable(MASTER,10, 10, WIDTH,HEIGHT,'Time Table','title')

        routine=self.lable(MASTER,300,70,WIDTH,HEIGHT,'Routine','title')

        empty=self.lable(MASTER,501,301,WIDTH+400,HEIGHT+100,'No Routine Generated Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

        faculty_info=self.lable(MASTER,10, 70, WIDTH,HEIGHT,'Faculty Form','subtitle')
        
        _class=self.lable(MASTER,10, 120, WIDTH,HEIGHT,'Class')

        faculty=self.lable(MASTER,10, 160, WIDTH,HEIGHT,'Faculty')

        shift=self.lable(MASTER,10, 200, WIDTH,HEIGHT,'Shift')

        total_section=self.lable(MASTER,10, 240, WIDTH,HEIGHT,'Total Section')

        manage_subject=self.lable(MASTER,10, 280, WIDTH,HEIGHT,'Manage Subject')

        line(MASTER,0,320,270,5)

        period_info=self.lable(MASTER,10, 350, WIDTH,HEIGHT,'Period Form','subtitle')
        
        total_period=self.lable(MASTER,10, 390, WIDTH,HEIGHT,'Total Period')

        time=self.lable(MASTER,10, 430, WIDTH,HEIGHT,'Time')

        time_per_period=self.lable(MASTER,10, 470, WIDTH,HEIGHT,'Time Per Period')

        line(MASTER,0,550,270,5)

        option=self.lable(MASTER,10, 570, WIDTH,HEIGHT,'Tools','subtitle')