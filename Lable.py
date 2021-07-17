from source import * 
from StyleSheet import LABLE

class Label:

    def __init__(self,*arg):
        
        self.WINDOW,self.SIDEBAR,self.TIME_TABLE,self.PROFESSOR,self.SUBJECT=arg
        
        self.time_table()

    def lable(self,master,X,Y,HEIGHT,WIDTH,text,font_type='normal'):
        
        label=QLabel(text,master)
        label.setFont(font(font_type))
        label.setStyleSheet(LABLE)
        label.setGeometry(QRect(X,Y,HEIGHT,WIDTH))
        
        return label

    def time_table(self):
        
        WIDTH,HEIGHT=166, 28

        line(self.TIME_TABLE,270,0,10,1000,'v')

        title=self.lable(self.TIME_TABLE,10, 10, WIDTH,HEIGHT,'Time Table','title')

        routine=self.lable(self.TIME_TABLE,300,70,WIDTH,HEIGHT,'Routine','title')

        empty=self.lable(self.TIME_TABLE,501,301,WIDTH+400,HEIGHT+100,'No Routine Generated Yet!','huge')
        empty.setStyleSheet('color:#6A737D')

        faculty_info=self.lable(self.TIME_TABLE,10, 70, WIDTH,HEIGHT,'Faculty Information','subtitle')
        
        _class=self.lable(self.TIME_TABLE,10, 120, WIDTH,HEIGHT,'Class')

        faculty=self.lable(self.TIME_TABLE,10, 160, WIDTH,HEIGHT,'Faculty')

        shift=self.lable(self.TIME_TABLE,10, 200, WIDTH,HEIGHT,'Shift')

        total_section=self.lable(self.TIME_TABLE,10, 240, WIDTH,HEIGHT,'Total Section')

        manage_subject=self.lable(self.TIME_TABLE,10, 280, WIDTH,HEIGHT,'Manage Subject')

        line(self.TIME_TABLE,0,320,270,5)

        period_info=self.lable(self.TIME_TABLE,10, 350, WIDTH,HEIGHT,'Period Information','subtitle')
        
        total_period=self.lable(self.TIME_TABLE,10, 390, WIDTH,HEIGHT,'Total Period')

        time=self.lable(self.TIME_TABLE,10, 430, WIDTH,HEIGHT,'Time')

        time_per_period=self.lable(self.TIME_TABLE,10, 470, WIDTH,HEIGHT,'Time Per Period')

        line(self.TIME_TABLE,0,540,270,5)

        option=self.lable(self.TIME_TABLE,10, 570, WIDTH,HEIGHT,'Tools','subtitle')
