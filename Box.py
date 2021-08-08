from Source import * 
from StyleSheet import COMBO_BOX, ENTRY, COMPLETER, SPINBOX, LOGIN_ENTRY

class Box:

    def __init__(self,*arg):
        self.WINDOW,self.SIDEBAR,self.TIME_TABLE,self.PROFESSOR,self.SUBJECT,self.RECORD,self.USER,self.SETTING,self.GUID = arg

        self.Widget = {}
        
        self.professor()
        self.subject()
        self.time_table()
        self.user()
        self.setting()

    def spinbox(self,master,x,y,width,height):
        spinbox = QSpinBox(master)
        spinbox.setStyleSheet(SPINBOX)
        spinbox.setGeometry(QRect(x,y,width,height))
        return spinbox

    def entry(self,master,x,y,height,width,style = ENTRY):
        entry = QLineEdit(master)
        entry.setStyleSheet(style)
        entry.setGeometry(QRect(x,y,height,width))
        return entry

    def completer(self,qline,clist:list):
        completer = QCompleter(clist)
        completer.popup().setStyleSheet(COMPLETER)
        qline.setCompleter(completer)
        return completer
    
    def combo_box(self,master,x,y,width,height,combolist:list = []):
        combo_box = QComboBox(master)
        combo_box.setStyleSheet(COMBO_BOX)
        combo_box.setGeometry(QRect(x,y,width,height))

        for i in range(len(combolist)):
            combo_box.addItem("")
            combo_box.setItemText(i,str(combolist[i]))

        return combo_box

    def professor(self):
        MASTER = self.PROFESSOR
        
        E_WIDTH,E_HEIGHT = 80,21

        CB_WIDTH,CB_HEIGHT = 50,21

        name = self.entry(MASTER, 80, 125, E_WIDTH, E_HEIGHT)
        name.setPlaceholderText('First Name')
        
        surname = self.entry(MASTER, 175, 125, E_WIDTH, E_HEIGHT)
        surname.setPlaceholderText('Last Name')

        email = self.entry(MASTER, 80, 165, E_WIDTH+96, E_HEIGHT)
        
        subject = self.entry(MASTER,80, 205, E_WIDTH+96, E_HEIGHT)

        classes = self.combo_box(MASTER,80, 245,CB_WIDTH,CB_HEIGHT,[11,12,'both'])

    def subject(self):
        MASTER = self.SUBJECT

        E_WIDTH,E_HEIGHT = 80,21

        CB_WIDTH,CB_HEIGHT = 50,21

        subject = self.entry(MASTER, 80, 125, E_WIDTH+76, E_HEIGHT)

        faculty_list = ['Science','Management','Law']
        faculty = self.combo_box(MASTER,80, 165,CB_WIDTH+20,CB_HEIGHT,faculty_list)

        class_ = self.combo_box(MASTER,80, 205,CB_WIDTH,CB_HEIGHT,[11,12,'both'])

    def time_table(self):

        MASTER = self.TIME_TABLE

        SB_WIDTH,SB_HEIGHT = 50,21

        CB_WIDTH,CB_HEIGHT = 50,21


        class_ = self.combo_box(MASTER,150, 125,CB_WIDTH,CB_HEIGHT,[11,12])
        
        faculty_list = ['Science','Management','Law']
        faculty = self.combo_box(MASTER,150, 165,CB_WIDTH+20,CB_HEIGHT,faculty_list)
        
        shift = self.combo_box(MASTER,150, 205,CB_WIDTH+20,CB_HEIGHT,['Morning','Day'])

        total_section = self.spinbox(MASTER,150, 245, SB_WIDTH, SB_HEIGHT)

        total_period = self.spinbox(MASTER,150, 395, SB_WIDTH, SB_HEIGHT)

        time = self.spinbox(MASTER,150, 435, SB_WIDTH, SB_HEIGHT)
        time.setRange(1,12)
        am_pm = self.combo_box(MASTER,215, 435, CB_WIDTH, CB_HEIGHT,['AM','PM'])

        time_per_period = self.spinbox(MASTER,150, 475,SB_WIDTH,SB_HEIGHT)
        am_pm = self.combo_box(MASTER,215, 475, CB_WIDTH, CB_HEIGHT,['Min','Hr'])


    def user(self):
        MASTER = self.USER
        
        E_WIDTH,E_HEIGHT = 190,30

        name = self.entry(MASTER,810, 301, E_WIDTH, E_HEIGHT,LOGIN_ENTRY)
        name.setFont(font('entry'))
        name.setPlaceholderText('User Name')
        
        email = self.entry(MASTER,810, 361, E_WIDTH, E_HEIGHT,LOGIN_ENTRY)
        email.setFont(font('entry'))
        email.setPlaceholderText('Example@gmail.com')
        
        password = self.entry(MASTER,810, 421, E_WIDTH, E_HEIGHT,LOGIN_ENTRY)
        password.setFont(font('entry'))
        password.setPlaceholderText('Password')
        password.setEchoMode(QLineEdit.Password)

        college = self.entry(MASTER,810, 481, E_WIDTH, E_HEIGHT,LOGIN_ENTRY)
        college.setFont(font('entry'))
        college.setPlaceholderText('Name of College')

        self.collect(user_password_entry = password)

    def setting(self):
        MASTER = self.SETTING
        
        E_WIDTH,E_HEIGHT = 810, 30

        name = self.entry(MASTER, 268, 20, E_WIDTH, E_HEIGHT,LOGIN_ENTRY)
        name.setFont(font('entry'))
        name.setPlaceholderText('Search Setting')


    def collect(self,**kwarg):
        
        for key,value in kwarg.items():
            self.Widget[key] = value