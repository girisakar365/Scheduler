from BackEnd import *
from FrontEnd.src import *

# table theme problem left to be solved!

class Function:
    def __init__(self,*args):
        Professor(*args)
        Setting(*args)

class Professor():

    def __init__(self,*args): 
        self.Lable, self.Button, self.Box, self.Manage, self.Slot = args
        self.table()

    def table(self):
        from FrontEnd.Table import Table

        professor = Table(self.Button.PROFESSOR, 300, 100, 800, 630)
        professor.setColumnCount(6)
        col = ['Name', 'Surname', 'ID', 'Subject', 'Email', 'Classes']
        professor.setColumnWidth(4, 250)
        professor.set_header(col)

        professor.load_data(DB.fetch()) # default value point to professor table so no parameters needed!

        self.Button.Widget['professor_insert'].clicked.connect(professor.show)

class Setting():
    def __init__(self,*args): 
        self.Lable, self.Button, self.Box, self.Manage, self.Slot = args

        #Secutiry-section: Un/Locked switch: __init__
        if type(Password.fetch('10100101')) == str:
            self.Lable.Widget['un/locked'].setText('Locked')
            self.Lable.Widget['un/locked'].setStyleSheet('color:#49ab81')
        else:
            self.Lable.Widget['un/locked'].setText('Unlocked')
            self.Lable.Widget['un/locked'].setStyleSheet('color:#d13429')
        self.Lable.Widget['un/locked'].adjustSize()

        if type(Password.fetch('10100101')) == str:
            self.Box.Widget['current-password'].setEnabled(True)
            self.sys_gate()
        else:
            self.Box.Widget['current-password'].setEnabled(False)

        # theme_button: __init__
        if Cache.fetch('switch','ui') == 0:
            self.Button.Widget['light-mode-btw'].setStyleSheet(Style('NBUTTON')  + 'QPushButton{ border:3px solid #1f2428; }')
            self.Button.Widget['dark-mode-btw'].setStyleSheet(Style('NBUTTON'))

        else:
            self.Button.Widget['dark-mode-btw'].setStyleSheet(Style('NBUTTON')  + 'QPushButton{ border:3px solid white; }')
            self.Button.Widget['light-mode-btw'].setStyleSheet(Style('NBUTTON'))
                    
        self.__setting__()
        
    def sys_gate(self):
        self.Button.LOCK.show()
        def check(password):

            if password == '':
                message(self.Button.LOCK, 'Incorrect Password!','w')

            else:
                c = Cryptography(password, 'dec')
                
                if c.result:
                    self.Lable.LOCK.hide()

                else:
                    message(self.Button.LOCK, 'Incorrect Password!','w')
                        
        self.Button.Widget['log-in'].clicked.connect(lambda: 
        check(self.Box.Widget['lock-password'].text()))

    def validity(self,data:list):
        for i in data:
            if i == '':
                return data.index(i)
        return True

    def check_password(self, data:list, master = None):

        if master == None: master = self.Button.SETTING

        if len(data[0]) >= 8:

            if len(set(data)) == 1: return True

            else:
                message(master, 'Warning: Password umatched!', 'w')
                return False

        else: 
            message(master, 'Warning: Password must contain 8 characters!', 'w')
            return False

    def __setting__(self):

        password_generator:QPushButton = self.Button.Widget['password-generator']
        password_generator.clicked.connect(lambda:self.generate_password())
        
        save_password:QPushButton = self.Button.Widget['save-password']
        save_password.clicked.connect(lambda:self.save_password())

        reset_password:QPushButton = self.Button.Widget['reset-password']
        reset_password.clicked.connect(lambda:self.reset_password())

        dark_mode: QPushButton = self.Button.Widget['dark-mode-btw']
        dark_mode.clicked.connect(lambda: self.ui_theme(1))
        
        light_mode: QPushButton = self.Button.Widget['light-mode-btw']
        light_mode.clicked.connect(lambda: self.ui_theme(0))
    
    def ui_theme(self, data):

        Cache.switch('ui', data)

        dark = self.Button.Widget['dark-mode-btw']
        light = self.Button.Widget['light-mode-btw']

        if Cache.fetch('switch','ui') == 0:
            dark.setStyleSheet(Style('NBUTTON'))
            light.setStyleSheet(Style('NBUTTON') + "QPushButton{ border:3px solid #1f2428;}")

        else: 
            dark.setStyleSheet(Style('NBUTTON') + "QPushButton{ border:3px solid #ffffff;}")
            light.setStyleSheet(Style('NBUTTON'))
        
        self.Lable.ui_theme()
        self.Button.ui_theme()
        self.Box.ui_theme()
        self.Slot.ui_theme()
        self.Manage.ui_theme()

    def generate_password(self):     
        new_password:QLineEdit = self.Box.Widget['new-password']
        new_password.clear()
        new_password.insert(randomPassword())

    def save_password(self):
        if self.Box.Widget['current-password'].isEnabled():
            entries = self.Box.Widget['security-entries']
        
        else:
            entries = self.Box.Widget['security-entries'][1:]

        data = []
        for i in entries:
            data.append(i.text())

        if len(data) == 3: check_data = data[1:]
        
        else: check_data = data

        if type(self.validity(data)) == bool:
            
            if  len(data) == 3: #check_current_password and new_password
                decrypt = Cryptography(data[0], 'dec')

                if decrypt.result:
                    
                    if self.check_password(check_data):
                        encrypt = Cryptography(data[2], 'enc')
                        message(self.Button.SETTING, 'Note: Password successfully saved!','s')
                        for i in entries: 
                            i.clear()
                            i.setStyleSheet(Style('LENTRY'))
                        self.Lable.Widget['un/locked'].setStyleSheet('color: #49ab81')
                        self.Lable.Widget['un/locked'].setText('Locked')

                    else:
                        for i in entries[1:]:
                            i.setStyleSheet(
                        Style('LENTRY') + 'QLineEdit{ border-color: #a50f29}')

                else:
                    message(self.Button.SETTING, 'Warning: Incorrect Password!', 'w')
                    entries[0].setStyleSheet(
                        Style('LENTRY') + 'QLineEdit{ border-color: #a50f29}')
            
            else:
                if self.check_password(check_data):
                    encrypt = Cryptography(data[1], 'enc')
                    message(self.Button.SETTING, 'Note: Password successfully saved!','s')
                    for i in entries:
                        i.clear()
                        i.setStyleSheet(Style('LENTRY'))
                    self.Lable.Widget['un/locked'].setStyleSheet('color: #49ab81')
                    self.Lable.Widget['un/locked'].setText('Locked')
                    self.Box.Widget['current-password'].setEnabled(True)

                else:
                    for i in entries:
                        i.setStyleSheet(
                    Style('LENTRY') + 'QLineEdit{ border-color: #a50f29}')

        else:
            message(self.Button.SETTING, 'Warring: Empty Input(s)!', 'w')
            entries[self.validity(data)].setStyleSheet(
                 Style('LENTRY') + 'QLineEdit{ border-color: #a50f29}'
            )
    
    def reset_password(self):
        
        if Password.fetch('10100101') != None:
            Password.insert('10100101', None)
            self.Lable.Widget['un/locked'].setStyleSheet('color: #d13429')
            self.Lable.Widget['un/locked'].setText('Unlocked')
            self.Box.Widget['current-password'].setEnabled(False)
            self.Box.Widget['current-password'].clear()

            message(self.Button.SETTING, 'Note: Password successfully removed.', 's')
        
        else:
            message(self.Button.SETTING, 'Note: No password set yet!', 'w')