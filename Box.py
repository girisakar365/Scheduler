try:
    from .Source import *

except Exception:
    from Source import *


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
            self.BAR
        ) = arg

        self.Widget = {}

        self.professor()
        self.subject()
        self.time_table()
        self.user()
        self.setting()

    def spinbox(self, master, x, y, width, height):
        spinbox = QSpinBox(master)
        spinbox.setStyleSheet(SPINBOX)
        spinbox.setGeometry(QRect(x, y, width, height))
        return spinbox

    def time_dial(self, master, x, y, width, height):
        time_dial = QTimeEdit(master)
        time_dial.setStyleSheet(TIME_DIAL)
        time_dial.setGeometry(QRect(x, y, width, height))
        return time_dial

    def entry(self, master, x, y, height, width, style=ENTRY):
        entry = QLineEdit(master)
        entry.setStyleSheet(style)
        entry.setGeometry(QRect(x, y, height, width))
        return entry

    def completer(self, qline, clist: list):
        completer = QCompleter(clist)
        completer.popup().setStyleSheet(COMPLETER)
        qline.setCompleter(completer)
        return completer

    def combo_box(self, master, x, y, width, height, combolist: list = []):
        combo_box = QComboBox(master)
        combo_box.setStyleSheet(COMBO_BOX)
        combo_box.setGeometry(QRect(x, y, width, height))

        for i in range(len(combolist)):
            combo_box.addItem("")
            combo_box.setItemText(i, str(combolist[i]))

        return combo_box

    def professor(self):
        MASTER = self.PROFESSOR

        E_WIDTH, E_HEIGHT = 80, 21

        CB_WIDTH, CB_HEIGHT = 50, 21

        name = self.entry(MASTER, 80, 125, E_WIDTH, E_HEIGHT)
        name.setPlaceholderText("First Name")

        surname = self.entry(MASTER, 175, 125, E_WIDTH, E_HEIGHT)
        surname.setPlaceholderText("Last Name")

        email = self.entry(MASTER, 80, 165, E_WIDTH + 96, E_HEIGHT)

        subject = self.entry(MASTER, 80, 205, E_WIDTH + 96, E_HEIGHT)

        classes = self.combo_box(MASTER, 80, 245, CB_WIDTH, CB_HEIGHT, [11, 12, "both"])

    def subject(self):
        MASTER = self.SUBJECT

        E_WIDTH, E_HEIGHT = 80, 21

        SB_WIDTH, SB_HEIGHT = 50, 21

        CB_WIDTH, CB_HEIGHT = 50, 21

        subject = self.entry(MASTER, 80, 125, E_WIDTH + 76, E_HEIGHT)

        faculty_list = ["Science", "Management", "Law"]
        faculty = self.combo_box(
            MASTER, 80, 205, CB_WIDTH + 20, CB_HEIGHT, faculty_list
        )

        class_ = self.combo_box(MASTER, 80, 240, CB_WIDTH, CB_HEIGHT, [11, 12, "both"])

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

    def user(self):
        MASTER = self.USER

        E_WIDTH, E_HEIGHT = 190, 30

        name = self.entry(MASTER, 810, 301, E_WIDTH, E_HEIGHT, LOGIN_ENTRY)
        name.setFont(font("entry"))
        name.setPlaceholderText("User Name")

        email = self.entry(MASTER, 810, 361, E_WIDTH, E_HEIGHT, LOGIN_ENTRY)
        email.setFont(font("entry"))
        email.setPlaceholderText("Example@gmail.com")

        password = self.entry(MASTER, 810, 421, E_WIDTH, E_HEIGHT, LOGIN_ENTRY)
        password.setFont(font("entry"))
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)

        college = self.entry(MASTER, 810, 481, E_WIDTH, E_HEIGHT, LOGIN_ENTRY)
        college.setFont(font("entry"))
        college.setPlaceholderText("Name of College")

        self.collect(up=password)

    def setting(self):
        MASTER = self.SETTING
        CHILD = self.SETTING_CHILD

        E_WIDTH, E_HEIGHT = 190,30
        SE_WIDTH, SE_HEIGHT = 810, 30

        name = self.entry(MASTER, 268, 20, SE_WIDTH, SE_HEIGHT, LOGIN_ENTRY)
        name.setFont(font("entry"))
        name.setPlaceholderText("Search Setting")

        def security_():
            STYLE = LOGIN_ENTRY# use this when sys locked  + 'QLineEdit{ border-color:#26d815; }'

            current_password = self.entry(CHILD, 80, 680, E_WIDTH, E_HEIGHT, STYLE)
            current_password.setPlaceholderText('Current Password')
            current_password.setFont(font('entry'))
            current_password.setEchoMode(QLineEdit.Password)

            new_password = self.entry(CHILD, 80, 760, E_WIDTH, E_HEIGHT, STYLE)
            new_password.setPlaceholderText('New Password')
            new_password.setFont(font('entry'))
            new_password.setEchoMode(QLineEdit.Password)

            re_enter_password = self.entry(CHILD, 80, 840, E_WIDTH, E_HEIGHT, STYLE)
            re_enter_password.setPlaceholderText('Re-Enter New Password')
            re_enter_password.setFont(font('entry'))
            re_enter_password.setEchoMode(QLineEdit.Password)

            list_encry_mtdh = ['Normal', 'Strong']
            encry_mtdh = self.combo_box(CHILD, 785, 765, 90, 25, list_encry_mtdh)
            
            list_ask_password = ['At starting only', 'Major security area', 'Every step']
            ask_password = self.combo_box(CHILD, 785, 840, 120, 25, list_ask_password)

            self.collect(
                cp = current_password, np = new_password, rep = re_enter_password
            )

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
    
        security_()
        shortcut_()

    def collect(self, **kwarg):

        for key, value in kwarg.items():
            self.Widget[key] = value
