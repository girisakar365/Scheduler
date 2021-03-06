try:
    from .src import *
    from .Lable import Label
    from .Button import Button
    from .Box import Box
    from .Dialog import (Manage, Slot)

except Exception:
    from src import *
    from Lable import Label
    from Button import Button
    from Box import Box
    from Dialog import (Manage, Slot)

class FrontEnd(QMainWindow):
    def __init__(self, app):

        super().__init__()

        scren_resoluction = app.desktop().screenGeometry()
        WIDTH, HEIGHT = scren_resoluction.width() - 10, scren_resoluction.height() - 35
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(Style('WIDGET'))

        PROFESSOR = frame(self)
        PROFESSOR.hide()

        SUBJECT = frame(self)
        SUBJECT.hide()
        TIME_TABLE = frame(self)
        TIME_TABLE.hide()

        USER = frame(self)
        USER.hide()

        SETTING = frame(self)
        SETTING_CHILD, SCROLLAREA = scroll_bar(SETTING)
        SCROLLAREA.move(260, 65)
        SCROLLAREA.setFixedSize(1000, 768)
        bar = SCROLLAREA.verticalScrollBar()
        bar.setStyleSheet(SCROLL_BAR)
        SETTING.hide()

        GUID = frame(self)
        GUID.hide()

        RECORD = frame(self)
        RECORD.show()

        SIDE_BAR = side_bar(self)

        LOCK = frame(self)
        LOCK.move(0,0)
        LOCK.hide()

        frames = (
            self,
            SIDE_BAR,
            TIME_TABLE,
            PROFESSOR,
            SUBJECT,
            RECORD,
            USER,
            SETTING,
            GUID,
            SETTING_CHILD,
            bar,
            LOCK
        )
        self.lable_manager = Label(*frames)
        self.button_manager = Button(*frames)
        self.box_manager = Box(*frames)

        #connecting sub windows to buttons
        self.Manage = Manage()
        self.Slot = Slot()

        self.sub_windows()
        self.merge_widget()
    
    def sub_windows(self):
        self.Manage.collect(
            button = self.button_manager.button, 
            lable = self.lable_manager.lable,
            entry = self.box_manager.entry,
            check_button = self.button_manager.check_button,
            radio_button = self.button_manager.radio_button
            )

        self.Slot.collect(
            button = self.button_manager.button, 
            lable = self.lable_manager.lable,
            entry = self.box_manager.entry,
            )
            
        self.Manage.lable()
        self.Manage.box()
        self.Manage.button()
        self.Manage.ui_theme()

        self.Slot.lable()
        self.Slot.box()
        self.Slot.button()
        self.Slot.ui_theme()

        self.button_manager.Widget['manage'].clicked.connect(self.Manage.run)
        self.button_manager.Widget['slot'].clicked.connect(self.Slot.run)

    def merge_widget(self):

        def echo(button,entry):
            button.pressed.connect(
                lambda:[entry.setEchoMode(QLineEdit.Normal)]
                )
            button.released.connect(
                lambda:[entry.setEchoMode(QLineEdit.Password)]
                )
            
        btw = [self.button_manager.Widget['cp'], self.button_manager.Widget['np'], self.button_manager.Widget['rep'],
        self.button_manager.Widget['up'], self.button_manager.Widget['lb']]
        box = [self.box_manager.Widget['cp'], self.box_manager.Widget['np'], self.box_manager.Widget['rep'],
        self.box_manager.Widget['up'], self.box_manager.Widget['lp']]

        for button, entry in zip(btw,box):
            echo(button,entry)

# import sys
# app = QApplication(sys.argv)
# root = FrontEnd(app)
# root.show()
# sys.exit(app.exec_())