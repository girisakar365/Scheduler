try:
    from .src import *

except Exception:
    from src import *


class Box:
    def __init__(self, *arg):
        (
            self.WINDOW,
            self.SIDEBAR,
            self.TIME_TABLE,
            self.PROFESSOR,
            self.SUBJECT,
            self.RECORD,
            self.USER,
            self.SETTING,
            self.GUID,
            self.SETTING_CHILD,
            self.BAR,
            self.LOCK
        ) = arg

        self.Widget = {'professor_entry': []}
        self.Ui={'entry':[], 'combo':[], 'lentry':[], 'spin-box':[],
        'time-dial':[]}

        self.professor()
        self.subject()
        self.time_table()
        self.user()
        self.setting()
        self.lock()

    def spinbox(self, master, x, y, width, height):
        spinbox = QSpinBox(master)
        spinbox.setStyleSheet(Style('SPINBOX'))
        spinbox.setGeometry(QRect(x, y, width, height))
        return spinbox

    def time_dial(self, master, x, y, width, height):
        time_dial = QTimeEdit(master)
        time_dial.setStyleSheet(Style('TIMEDIAL'))
        time_dial.setGeometry(QRect(x, y, width, height))
        return time_dial

    def entry(self, master, x, y, width, height, style=Style('ENTRY')):
        entry = QLineEdit(master)
        entry.setStyleSheet(style)
        entry.setGeometry(QRect(x, y, width, height))
        return entry

    def completer(self, qline, clist: list):
        completer = QCompleter(clist)
        # completer.popup().setStyleSheet(COMPLETER)
        qline.setCompleter(completer)
        return completer

    def combo_box(self, master, x, y, width, height, combolist: list = []):
        combo_box = QComboBox(master)
        combo_box.setStyleSheet(Style('COMBO'))
        combo_box.setGeometry(QRect(x, y, width, height))

        for i in range(len(combolist)):
            combo_box.addItem("")
            combo_box.setItemText(i, str(combolist[i]))

        return combo_box
    
    def ui_theme(self):
        for l_entry in self.Ui['lentry']:
            l_entry.setStyleSheet(Style('LENTRY'))

        for entry in self.Ui['entry']:
            entry.setStyleSheet(Style('ENTRY'))

        for combo in self.Ui['combo']:
            combo.setStyleSheet(Style('COMBO'))

        for spinbox in self.Ui['spin-box']:
            spinbox.setStyleSheet(Style('SPINBOX'))
        
        self.Ui['time-dial'][0].setStyleSheet(Style('TIMEDIAL'))

    def professor(self):
        MASTER = self.PROFESSOR

        E_WIDTH, E_HEIGHT = 80, 21

        CB_WIDTH, CB_HEIGHT = 50, 21

        name = self.entry(MASTER, 80, 125, E_WIDTH, E_HEIGHT)
        name.setPlaceholderText("First Name")

        surname = self.entry(MASTER, 175, 125, E_WIDTH, E_HEIGHT)
        surname.setPlaceholderText("Last Name")

        email = self.entry(MASTER, 80, 165, E_WIDTH + 96, E_HEIGHT)
        email.setPlaceholderText('example@gmail.com')

        subject = self.entry(MASTER, 80, 205, E_WIDTH + 96, E_HEIGHT)
        subject.setPlaceholderText('Subject taughted')

        classes = self.combo_box(MASTER, 80, 245, CB_WIDTH, CB_HEIGHT, [11, 12, "both"])

        search = self.entry(MASTER, 300, 80, 766, 30, Style('LENTRY'))
        search.setFont(font("entry"))
        search.setPlaceholderText("Search")
        self.Widget['professor_search'] = search

        for i in [name, surname, email, subject, classes]:
            self.Ui['entry'].append(i)
        self.Ui['lentry'].append(search)

        for _ in [name, surname, email, subject]:
            self.Widget['professor_entry'].append(_)
        
        self.Widget['professor_classes'] = classes

    def subject(self):
        MASTER = self.SUBJECT

        E_WIDTH, E_HEIGHT = 80, 21

        CB_WIDTH, CB_HEIGHT = 50, 21

        subject = self.entry(MASTER, 80, 125, E_WIDTH + 76, E_HEIGHT)
        subject.setPlaceholderText('Name of subject')

        faculty_list = ["Science", "Management", "Law"]
        faculty = self.combo_box(
            MASTER, 80, 205, CB_WIDTH + 20, CB_HEIGHT, faculty_list
        )

        class_ = self.combo_box(MASTER, 80, 240, CB_WIDTH, CB_HEIGHT, [11, 12, "both"])

        self.Ui['entry'].append(subject)

        for i in [faculty,class_]:
            self.Ui['combo'].append(i)

    def time_table(self):

        MASTER = self.TIME_TABLE

        SB_WIDTH, SB_HEIGHT = 50, 21

        CB_WIDTH, CB_HEIGHT = 50, 21

        class_ = self.combo_box(MASTER, 150, 125, CB_WIDTH, CB_HEIGHT, [11, 12])

        faculty_list = ["Science", "Management", "Law"]
        faculty = self.combo_box(
            MASTER, 150, 165, CB_WIDTH + 20, CB_HEIGHT, faculty_list
        )

        shift = self.combo_box(
            MASTER, 150, 205, CB_WIDTH + 20, CB_HEIGHT, ["Morning", "Day"]
        )

        total_section = self.spinbox(MASTER, 150, 245, SB_WIDTH, SB_HEIGHT)

        total_period = self.spinbox(MASTER, 150, 395, SB_WIDTH, SB_HEIGHT)

        time = self.time_dial(MASTER, 150, 435, SB_WIDTH + 20, SB_HEIGHT)

        time_per_period = self.spinbox(MASTER, 150, 475, SB_WIDTH, SB_HEIGHT)
        am_pm = self.combo_box(MASTER, 215, 475, CB_WIDTH, CB_HEIGHT, ["Min", "Hr"])

        for i in [class_, faculty, am_pm, shift]:
            self.Ui['combo'].append(i)
        
        for i in [total_period, time_per_period, total_section]:
            self.Ui['spin-box'].append(i)

        self.Ui['time-dial'].append(time)

    def user(self):
        MASTER = self.USER

        E_WIDTH, E_HEIGHT = 190, 30

        name = self.entry(MASTER, 810, 301, E_WIDTH, E_HEIGHT, Style('LENTRY'))
        name.setFont(font("entry"))
        name.setPlaceholderText("User Name")

        email = self.entry(MASTER, 810, 361, E_WIDTH, E_HEIGHT, Style('LENTRY'))
        email.setFont(font("entry"))
        email.setPlaceholderText("Example@gmail.com")

        password = self.entry(MASTER, 810, 421, E_WIDTH, E_HEIGHT, Style('LENTRY'))
        password.setFont(font("entry"))
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)

        college = self.entry(MASTER, 810, 481, E_WIDTH, E_HEIGHT, Style('LENTRY'))
        college.setFont(font("entry"))
        college.setPlaceholderText("Name of College")

        for i in [name,email,password,college]:
            self.Ui['lentry'].append(i)

        self.collect(up=password)

    def setting(self):
        MASTER = self.SETTING
        CHILD = self.SETTING_CHILD

        E_WIDTH, E_HEIGHT = 190,30
        SE_WIDTH, SE_HEIGHT = 810, 30

        search = self.entry(MASTER, 268, 20, SE_WIDTH, SE_HEIGHT, Style('LENTRY'))
        search.setFont(font("entry"))
        search.setPlaceholderText("Search Setting")

        self.Ui['lentry'].append(search)

        def security_():
            # use this when sys locked  + 'QLineEdit{ border-color:#26d815; }'

            current_password = self.entry(CHILD, 80, 680, E_WIDTH, E_HEIGHT, Style('LENTRY'))
            current_password.setPlaceholderText('Current Password')
            current_password.setFont(font('entry'))
            current_password.setEchoMode(QLineEdit.Password)

            self.Widget['current-password'] = current_password

            new_password = self.entry(CHILD, 80, 760, E_WIDTH, E_HEIGHT, Style('LENTRY'))
            new_password.setPlaceholderText('New Password')
            new_password.setFont(font('entry'))
            new_password.setEchoMode(QLineEdit.Password)
            self.Widget['new-password'] = new_password

            re_enter_password = self.entry(CHILD, 80, 840, E_WIDTH, E_HEIGHT, Style('LENTRY'))
            re_enter_password.setPlaceholderText('Re-Enter New Password')
            re_enter_password.setFont(font('entry'))
            re_enter_password.setEchoMode(QLineEdit.Password)

            self.Widget['security-entries'] = [current_password, new_password, re_enter_password]

            list_encry_mtdh = ['Normal', 'Strong']
            encry_mtdh = self.combo_box(CHILD, 785, 765, 90, 25, list_encry_mtdh)
            self.Ui['combo'].append(encry_mtdh)

            self.collect(
                cp = current_password, np = new_password, rep = re_enter_password
            )

            for i in [current_password,new_password,re_enter_password]:
                self.Ui['lentry'].append(i)

        def shortcut_():
            WIDTH, HEIGHT = 60, 25

            specific_key = ['Ctrl', 'Alt']
            shift_key = ['None', 'Shift']
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            num = '0123456789'
            normal_key = [j for i in (alpha, num) for j in i]

            record_specific_key = self.combo_box(CHILD, 200, 1200, WIDTH, HEIGHT, specific_key)
            record_shift_key = self.combo_box(CHILD, 300, 1200, WIDTH, HEIGHT, shift_key)
            record_normal_key = self.combo_box(CHILD, 400, 1200, WIDTH, HEIGHT, normal_key)
            record_normal_key.setCurrentText('r')

            professor_specific_key = self.combo_box(CHILD, 200, 1280, WIDTH, HEIGHT, specific_key)
            professor_shift_key = self.combo_box(CHILD, 300, 1280, WIDTH, HEIGHT, shift_key)
            professor_normal_key = self.combo_box(CHILD, 400, 1280, WIDTH, HEIGHT, normal_key)
            professor_normal_key.setCurrentText('p')
            
            subject_specific_key = self.combo_box(CHILD, 200, 1360, WIDTH, HEIGHT, specific_key)
            subject_shift_key = self.combo_box(CHILD, 300, 1360, WIDTH, HEIGHT, shift_key)
            subject_normal_key = self.combo_box(CHILD, 400, 1360, WIDTH, HEIGHT, normal_key)
            subject_normal_key.setCurrentText('s')

            time_table_specific_key = self.combo_box(CHILD, 200, 1440, WIDTH, HEIGHT, specific_key)
            time_table_shift_key = self.combo_box(CHILD, 300, 1440, WIDTH, HEIGHT, shift_key)
            time_table_normal_key = self.combo_box(CHILD, 400, 1440, WIDTH, HEIGHT, normal_key)
            time_table_normal_key.setCurrentText('t')
            
            user_specific_key = self.combo_box(CHILD, 200, 1520, WIDTH, HEIGHT, specific_key)
            user_shift_key = self.combo_box(CHILD, 300, 1520, WIDTH, HEIGHT, shift_key)
            user_normal_key = self.combo_box(CHILD, 400, 1520, WIDTH, HEIGHT, normal_key)
            user_normal_key.setCurrentText('u')
            
            guid_specific_key = self.combo_box(CHILD, 690, 1200, WIDTH, HEIGHT, specific_key)
            guid_shift_key = self.combo_box(CHILD, 790, 1200, WIDTH, HEIGHT, shift_key)
            guid_normal_key = self.combo_box(CHILD, 890, 1200, WIDTH, HEIGHT, normal_key)
            guid_normal_key.setCurrentText('g')

            manage_specific_key = self.combo_box(CHILD, 690, 1280, WIDTH, HEIGHT, specific_key)
            manage_shift_key = self.combo_box(CHILD, 790, 1280, WIDTH, HEIGHT, shift_key)
            manage_normal_key = self.combo_box(CHILD, 890, 1280, WIDTH, HEIGHT, normal_key)
            manage_normal_key.setCurrentText('m')

            email_specific_key = self.combo_box(CHILD, 690, 1360, WIDTH, HEIGHT, specific_key)
            email_shift_key = self.combo_box(CHILD, 790, 1360, WIDTH, HEIGHT, shift_key)
            email_normal_key = self.combo_box(CHILD, 890, 1360, WIDTH, HEIGHT, normal_key)
            email_normal_key.setCurrentText('e')

            for  i in [record_normal_key,record_shift_key,record_specific_key,
            professor_normal_key,professor_shift_key,professor_specific_key,
            subject_normal_key,subject_specific_key,subject_shift_key,
            time_table_normal_key,time_table_shift_key,time_table_specific_key,
            user_specific_key,user_shift_key,user_normal_key,
            guid_normal_key,guid_shift_key,guid_specific_key,
            email_normal_key,email_shift_key,email_specific_key]:
                self.Ui['combo'].append(i)
    
        security_()
        shortcut_()

    def lock(self):
        MASTER = self.LOCK

        user_name = self.entry(MASTER, 543, 370, 250, 30, Style('LENTRY'))
        user_name.setFont(font("entry"))
        user_name.setPlaceholderText('User Name')
        
        password = self.entry(MASTER, 543, 420, 250, 30, Style('LENTRY'))
        password.setFont(font("entry"))
        password.setPlaceholderText('Password')
        password.setEchoMode(QLineEdit.Password)
        self.Widget['lp'] = password

        self.Ui['lentry'].extend([user_name, password])

        self.Widget['lock-password'] = password

    def collect(self, **kwarg):

        for key, value in kwarg.items():
            self.Widget[key] = value
