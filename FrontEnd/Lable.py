try:
    from .src import *
    from .Photo_Lib import SCHOLAR, ico

except Exception:
    from src import *
    from Photo_Lib import SCHOLAR, ico
    
class Label:
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
        self.Widget = {}
        self.Ui={'frame':[]}

        self.record()
        self.professor()
        self.subject()
        self.time_table()
        self.user()
        self.setting()
        self.guid()
        self.lock()

    def lable(
        self,master,x: int = 0,y: int = 0,text="text",font_type="normal",style=None ):

        label = QLabel(text, master)
        label.setFont(font(font_type))
        if style != None: label.setStyleSheet(style)
        label.setGeometry(QRect(x, y, 0, 0))
        label.adjustSize()

        return label

    def frame(self, master, w: int, h: int, style=Style('LFRAME')):

        _frame = frame(master)
        _frame.setFixedSize(w, h)
        _frame.setStyleSheet(style)
        _frame.setGraphicsEffect(shadow(65))

        return _frame
    
    def ui_theme(self):
        for i in self.Ui['frame']:
            i.setStyleSheet(Style('LFRAME'))

        self.Ui['lock-bg'].setPixmap(ico('LOGIN_BG'))
        self.Ui['lock-logo'].setPixmap(ico('LOGO'))

    def record(self):

        MASTER = self.RECORD

        title = self.lable(MASTER, 10, 10, "Records", "title")

        empty = self.lable(MASTER, 401, 301, "No Records Saved Yet!", "huge")
        empty.setStyleSheet("color:#6A737D")

    def professor(self):

        MASTER = self.PROFESSOR

        info_table = self.lable(MASTER, 300, 30, "Record of Professors", "title")

        line(MASTER, 270, 0, "v")

        empty = self.lable(MASTER, 501, 301, "No Records Saved Yet!", "huge")
        empty.setStyleSheet("color:#6A737D")

        title = self.lable(MASTER, 10, 10, "Professor", "title")

        form = self.lable(MASTER, 10, 70, "Entry Form", "subtitle")

        name = self.lable(MASTER, 10, 120, "Name")

        email = self.lable(MASTER, 10, 160, "Email")

        subject = self.lable(MASTER, 10, 200, "Subject")

        classes = self.lable(MASTER, 10, 240, "Classes")

        line(MASTER, 0, 330, length=270)

        tool = self.lable(MASTER, 10, 350, "Tools", "subtitle")

    def subject(self):

        MASTER = self.SUBJECT

        title = self.lable(MASTER, 10, 3, "Subject", "title")

        info = self.lable(MASTER, 300, 40, "Subject List", "title")

        empty = self.lable(MASTER, 501, 301, "No Records Saved Yet!", "huge")
        empty.setStyleSheet("color:#6A737D")

        line(MASTER, 270, 0, "v")

        form = self.lable(MASTER, 10, 70, "Subject From", "subtitle")

        sub_name = self.lable(MASTER, 10, 120, "Subject")

        slot = self.lable(MASTER, 10, 160, "Slots")

        faculty = self.lable(MASTER, 10, 200, "Faculty")

        class_ = self.lable(MASTER, 10, 240, "Class")

        line(MASTER, 0, 300, length=270)

        tool = self.lable(MASTER, 10, 312, "Tools", "subtitle")

    def time_table(self):

        MASTER = self.TIME_TABLE

        line(MASTER, 270, 0, "v")

        title = self.lable(MASTER, 10, 10, "Time Table", "title")

        routine = self.lable(MASTER, 300, 70, "Routine", "title")

        empty = self.lable(MASTER, 501, 301, "No Routine Generated Yet!", "huge")
        empty.setStyleSheet("color:#6A737D")

        faculty_info = self.lable(MASTER, 10, 70, "Faculty Form", "subtitle")

        _class = self.lable(MASTER, 10, 120, "Class")

        faculty = self.lable(MASTER, 10, 160, "Faculty")

        shift = self.lable(MASTER, 10, 200, "Shift")

        total_section = self.lable(MASTER, 10, 240, "Total Section")

        manage_subject = self.lable(MASTER, 10, 280, "Manage Section")

        line(MASTER, 0, 320, length=270)

        period_info = self.lable(MASTER, 10, 350, "Period Form", "subtitle")

        total_period = self.lable(MASTER, 10, 390, "Total Period")

        time = self.lable(MASTER, 10, 430, "Time")

        time_per_period = self.lable(MASTER, 10, 470, "Time Per Period")

        line(MASTER, 0, 550, length=270)

        option = self.lable(MASTER, 10, 570, "Tools", "subtitle")

    def user(self):

        MASTER = self.USER
        font_ = font("fancy_subtitle")
        font_.setBold(True)
        font_.setPointSize(30)

        title = self.lable(MASTER, 10, 10, "Welcome User")
        title.setStyleSheet("color:#7CCAFB")
        title.setFixedSize(300, 50)
        title.setFont(font_)

        logo = self.lable(MASTER, 50, 130, text="")
        logo.setPixmap( SCHOLAR )
        logo.setFixedSize(512, 512)

        CHILD = self.frame(MASTER, 480, 480)
        CHILD.move(670, 160)

        sub_title = self.lable(CHILD, 170, 50, "SIGN UP", "fancy_title")
        sub_title.setStyleSheet("color:#7CCAFB")

        name = self.lable(CHILD, 25, 140, "User Name:", "fancy_subtitle")
        name.setStyleSheet("color:#73AAFA")

        email = self.lable(CHILD, 25, 200, "Email:", "fancy_subtitle")
        email.setStyleSheet("color:#79C0FB")

        password = self.lable(CHILD, 25, 260, "Password:", "fancy_subtitle")
        password.setStyleSheet("color:#74ADFA")

        college = self.lable(CHILD, 25, 320, "College:", "fancy_subtitle")
        college.setStyleSheet("color:#74ADFA")
        
        self.Ui['frame'].append(CHILD)

    def setting(self):

        MASTER = self.SETTING
        CHILD = self.SETTING_CHILD

        title = self.lable(MASTER, 10, 10, "Settings", "fancy_title")

        layout = QVBoxLayout()
        layout.setSpacing(500)

        line(MASTER, 0, 65)

        line(MASTER, 260, 65, "v")

        general = self.lable(CHILD, 400, 100, "General", "fancy_title")

        security = self.lable(CHILD, 400, 100, "Security", "fancy_title")

        shortcut = self.lable(
            CHILD, 400, 100, "Manage Keyboard Shorcuts", "fancy_title"
        )

        manage_account = self.lable(CHILD, 10, 900, "Manage Account", "fancy_title")

        space = self.lable(CHILD, 10, 900, " ", "fancy_title")

        for i in general, security, shortcut, manage_account, space:
            layout.addWidget(i)

        CHILD.setLayout(layout)

        def general_():
            light_mode_lable = self.lable(CHILD, 200, 460, 'Light Mode','fancy_subtitle')

            dark_mode_lable = self.lable(CHILD, 660, 460, 'Dark Mode','fancy_subtitle')

        def security_():
            line(CHILD, 480, 620, 'v', 350)

            system_status=self.lable(CHILD, 605, 680, 'System Status:', 'fancy_subtitle')
            
            encry_mthd=self.lable(CHILD, 605, 760, 'Encryption Method:', 'fancy_subtitle')

            rm_password = self.lable(CHILD, 605, 840, 'Unlock system:', 'fancy_subtitle')
            
            answer_ss = self.lable(CHILD, 785, 685, 'None', 'fancy_subtitle')
            
            self.Widget['un/locked'] = answer_ss
        
        def shortcut_():
            line(CHILD, 500, 1190, 'v', 370)

            record = self.lable(CHILD, 60, 1200, 'Record', 'fancy_subtitle')
            professor = self.lable(CHILD, 60, 1280, 'Professor', 'fancy_subtitle')
            subject = self.lable(CHILD, 60, 1360, 'Subject', 'fancy_subtitle')
            time_table = self.lable(CHILD, 60, 1440, 'Time Table', 'fancy_subtitle')
            user = self.lable(CHILD, 60, 1520, 'User', 'fancy_subtitle')
            guid = self.lable(CHILD, 530, 1200, 'Guid', 'fancy_subtitle')
            manage_subject = self.lable(CHILD, 530, 1280, 'Manage Subject', 'fancy_subtitle')
            email = self.lable(CHILD, 530, 1360, 'Emailing', 'fancy_subtitle')

        def manage_account_():
            self.lable(CHILD, 280, 1900, 'No account signed in.', 'fancy_huge', 'color:#6A737D')

        general_()
        security_()
        shortcut_()
        manage_account_()


    def guid(self):
        MASTER = self.GUID

        title = self.lable(MASTER, 10, 10, "Guid", "title")

    def lock(self):
        MASTER = self.LOCK

        bg = QLabel(self.LOCK)
        bg.setFixedSize(1900,900)
        bg.setScaledContents(True)        
        bg.setPixmap(ico('LOGIN_BG'))
        
        CHILD = self.frame(MASTER, 400, 500)
        CHILD.move(473, 130)
        CHILD.setFixedHeight(512)

        logo = self.lable(CHILD, 100, 80, text="")
        logo.setPixmap( ico('LOGO') )
        logo.setFixedSize(198, 90)

        self.Ui['frame'].append(CHILD)
        self.Ui['lock-bg'] = bg
        self.Ui['lock-logo'] = logo

    def collect(self, **kwarg):

        for key, value in kwarg.items():
            self.Widget[key] = value
