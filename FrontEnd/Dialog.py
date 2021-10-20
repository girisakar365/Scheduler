try:
    from .src import *
    from .Photo_Lib import ico

except Exception:
    from src import *
    from Photo_Lib import ico


class Manage(QDialog):

    def __init__(self):

        super().__init__()
        
        self.resize(353,510)
        
        self.setMaximumSize(QSize(323,510))

        self.setStyleSheet(Style('DIALOG'))
        
        self.mousePressEvent = lambda event : self.setFocus()

        self.Widget = {}
        self.Ui = {'lable':[],
        'entry':[],
        'check-button':[],
        'button':[],
        'radio-button':[],
        }

    def ui_theme(self):
        self.setStyleSheet(Style('DIALOG'))

        for lable in self.Ui['lable']:
            lable.setStyleSheet(Style('LABLE'))

        for entry in self.Ui['entry']:
            entry.setStyleSheet(Style('ENTRY'))

        for button in self.Ui['button']:
            button.setStyleSheet(Style('NBUTTON'))
        
        for radio_button in self.Ui['radio-button']:
            radio_button.setStyleSheet(Style('RBUTTON'))

        for check_button in self.Ui['check-button']:
            check_button.setStyleSheet(Style('RBUTTON'))

        self.Ui['button'][0].setIcon(ico('TICK'))

    def lable(self):
        lable:QLabel = self.Widget['lable']

        title = lable(self, 8, 15, 'Manage Section', 'title')
        
        opt_sub_i = lable(self, 10, 70, 'Optional Subject I:', 'normal')

        opt_sub_ii = lable(self, 10, 180, 'Optional Subject II:', 'normal')

        lab = lable(self, 10, 347, 'Lab Settings:', 'normal')

        brk = lable(self, 10, 430, 'Breaks', 'normal')

        for i in [title, opt_sub_i, opt_sub_ii, lab, brk]:
            self.Ui['lable'].append(i)

    def box(self):
        entry:QLineEdit = self.Widget['entry']
        check_button:QCheckBox = self.Widget['check_button']

        maths = check_button(self, 'Basic Mathematics:', 10, 110)
        social = check_button(self, 'Social:', 10, 140)
        computer = check_button(self, 'Computer:', 10, 220)
        biology = check_button(self, 'Biology:', 10, 250)
        business_std = check_button(self, 'Business Studies:', 10, 280)
        hotel_mgt = check_button(self, 'Hotel Management:', 10, 310)

        lab_mgt = check_button(self, 'Included', 10, 380)
        lab_mgt.setChecked(True)
        
        def lab_mgt_func():
            if lab_mgt.isChecked(): lab_mgt.setText('Included') 
            else: lab_mgt.setText('Excluded')

        lab_mgt.stateChanged.connect(lab_mgt_func)

        maths_ = entry(self, 148, 110, 50, 20)        
        social_ = entry(self, 148, 140, 50, 20)
        computer_ = entry(self, 148, 220, 50, 20)
        biology_ = entry(self, 148, 250, 50, 20)
        business_std_ = entry(self, 148, 280, 50, 20)
        hotel_mgt_ = entry(self, 148, 310, 50, 20)

        for i in [maths_, social_, computer_, biology_, business_std_, hotel_mgt_]:
            i.setPlaceholderText('Seciton')
            i.setEnabled(False)
            i.setStyleSheet(Style('ENTRY') + 'QLineEdit{ background-color: #1F2428}')

        maths.stateChanged.connect(lambda: self.on_off(maths, maths_))
        social.stateChanged.connect(lambda: self.on_off(social, social_))
        computer.stateChanged.connect(lambda: self.on_off(computer, computer_))
        biology.stateChanged.connect(lambda: self.on_off(biology, biology_))
        business_std.stateChanged.connect(lambda: self.on_off(business_std, business_std_))
        hotel_mgt.stateChanged.connect(lambda: self.on_off(hotel_mgt, hotel_mgt_))

        for i in [lab_mgt, maths, social, computer, biology, business_std, hotel_mgt]:
            self.Ui['check-button'].append(i)

        for i in [maths_, social_, computer_, biology_, business_std_, hotel_mgt_]:
            self.Ui['entry'].append(i)

    def button(self):
        button = self.Widget['button']
        radio_button = self.Widget['radio_button']

        same_time = radio_button(self, 'Same time', 10, 460)
        
        split_time = radio_button(self, 'Split according to optional subjects', 10, 480)

        conform = button(self, 280, 468, 36, img = ico('TICK'), size = 20)

        for i in [same_time, split_time]:
            self.Ui['radio-button'].append(i)

        self.Ui['button'].append(conform)

    def on_off(self,master,child,):

        if master.isChecked():
            child.setEnabled(True)
            child.setFocus()

        else:
            child.clear()
            child.setEnabled(False)

    def collect(self, **kwarg):
        for key, value in kwarg.items():
            self.Widget[key] = value

    def run(self):
        self.exec_()


class Slot(QDialog):

    def __init__(self):

        super().__init__()
        
        self.resize(409,510)
        
        self.setMaximumSize(QSize(409,510))

        self.setStyleSheet(Style('DIALOG'))

        self.Widget = {}
        self.Ui = {'lable':[],
        'entry':[],
        'button':[]}

        self.mousePressEvent = lambda event : self.setFocus()

    def ui_theme(self):
        self.setStyleSheet(Style('DIALOG'))
        self.Ui['entry'][0].setStyleSheet(Style('LENTRY'))
        self.Ui['lable'][0].setStyleSheet(Style('LABLE'))
        self.Ui['button'][0].setStyleSheet(Style('NBUTTON'))
        self.Ui['button'][0].setIcon(ico('SCOPE'))

    def lable(self):

        lable = self.Widget['lable']

        title = lable(self, 8, 15, 'Subject Slot', 'title')

        empty = lable(self, 8, 230, "No Subject Searched!", "huge")
        empty.setStyleSheet("color:#6A737D")

        self.Ui['lable'].append(title)

    def box(self):
        entry = self.Widget['entry']

        search = entry(self, 8, 85, 180, 30, Style('LENTRY'))
        search.setFont(font("entry"))
        search.setPlaceholderText('Search Subject')
        self.Ui['entry'].append(search)

    def button(self):
        button = self.Widget['button']

        search = button(self, 198, 83, 36, img = ico('SCOPE'), style = Style('NBUTTON'), size = 18)
        self.Ui['button'].append(search)

    def collect(self, **kwarg):
        for key, value in kwarg.items():
            self.Widget[key] = value
    
    def run(self):
        self.exec_()