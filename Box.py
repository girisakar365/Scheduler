from source import * 
from StyleSheet import COMBO_BOX, ENTRY, COMPLETER, SPINBOX

class Box:

    def __init__(self,*arg):
        self.WINDOW, self.SIDEBAR, self.TIME_TABLE, self.PROFESSOR, self.SUBJECT, self.RECORD = arg

        self.professor()
        self.subject()
        self.time_table()

    def spinbox(self,master,x,y,width,height):
        spinbox=QSpinBox(master)
        spinbox.setStyleSheet(SPINBOX)
        spinbox.setGeometry(QRect(x,y,width,height))
        return spinbox

    def entry(self,master,x,y,height,width):
        entry=QLineEdit(master)
        entry.setStyleSheet(ENTRY)
        entry.setGeometry(QRect(x,y,height,width))
        return entry

    def completer(self,qline,clist:list):
        completer=QCompleter(clist)
        completer.popup().setStyleSheet(COMPLETER)
        qline.setCompleter(completer)
        return completer
    
    def combo_box(self,master,x,y,height,width,combolist:list=[]):
        combo_box=QComboBox(master)
        combo_box.setStyleSheet(COMBO_BOX)
        combo_box.setGeometry(QRect(x,y,height,width))

        for i in range(len(combolist)):
            combo_box.addItem("")
            combo_box.setItemText(i,str(combolist[i]))

        return combo_box

    def professor(self):
        MASTER=self.PROFESSOR
        
        E_WIDTH,E_HEIGHT=80,21

        CB_WIDTH,CB_HEIGHT=50,21

        name=self.entry(MASTER, 80, 125, E_WIDTH, E_HEIGHT)
        name.setPlaceholderText('First Name')
        
        surname=self.entry(MASTER, 175, 125, E_WIDTH, E_HEIGHT)
        surname.setPlaceholderText('Last Name')

        email=self.entry(MASTER, 80, 165, E_WIDTH+96, E_HEIGHT)
        
        subject=self.entry(MASTER,80, 205, E_WIDTH+96, E_HEIGHT)

        classes=self.combo_box(MASTER,80, 245,CB_WIDTH,CB_HEIGHT,[11,12,'both'])

    def subject(self):
        MASTER=self.SUBJECT

        E_WIDTH,E_HEIGHT=80,21

        CB_WIDTH,CB_HEIGHT=50,21

        subject=self.entry(MASTER, 80, 125, E_WIDTH+76, E_HEIGHT)

        faculty_list=['Science','Management','Law']
        faculty = self.combo_box(MASTER,80, 165,CB_WIDTH+20,CB_HEIGHT,faculty_list)

        class_ = self.combo_box(MASTER,80, 205,CB_WIDTH,CB_HEIGHT,[11,12,'both'])

    def time_table(self):

        SB_WIDTH,SB_HEIGHT=50,21

        MASTER=self.TIME_TABLE

        CB_WIDTH,CB_HEIGHT=50,21


        class_ = self.combo_box(MASTER,150, 125,CB_WIDTH,CB_HEIGHT,[11,12])
        
        faculty_list=['Science','Management','Law']
        faculty = self.combo_box(MASTER,150, 165,CB_WIDTH+20,CB_HEIGHT,faculty_list)
        
        shift = self.combo_box(MASTER,150, 205,CB_WIDTH+20,CB_HEIGHT,['Morning','Day'])

        total_section = self.spinbox(MASTER,150, 245, SB_WIDTH, SB_HEIGHT)

        total_period = self.spinbox(MASTER,150, 395, SB_WIDTH, SB_HEIGHT)

        time = self.spinbox(MASTER,150, 435, SB_WIDTH, SB_HEIGHT)
        time.setRange(1,12)
        am_pm = self.combo_box(MASTER,215, 435, CB_WIDTH, CB_HEIGHT,['AM','PM'])

        time_per_period = self.spinbox(MASTER,150, 475,SB_WIDTH,SB_HEIGHT)
        am_pm = self.combo_box(MASTER,215, 475, CB_WIDTH, CB_HEIGHT,['Min','Hr']) 