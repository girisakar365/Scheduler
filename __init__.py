import sys

try:
    from .Source import *
    from .Lable import Label
    from .Button import Button
    from .Box import Box
    from .Setting import Connect
    from .Dialog import (Manage, Slot)

except Exception:
    from Source import *
    from Lable import Label
    from Button import Button
    from Box import Box
    from Setting import Connect
    from Dialog import (Manage, Slot)


class FrontEnd(QMainWindow):
    def __init__(self, app):

        super().__init__()

        scren_resoluction = app.desktop().screenGeometry()
        WIDTH, HEIGHT = scren_resoluction.width() - 10, scren_resoluction.height() - 35
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(WIDGET)

        WINDOW = self

        PROFESSOR = frame(WINDOW)
        PROFESSOR.hide()

        SUBJECT = frame(WINDOW)
        SUBJECT.hide()

        TIME_TABLE = frame(WINDOW)
        TIME_TABLE.hide()

        USER = frame(WINDOW)
        USER.hide()

        SETTING = frame(WINDOW)
        SETTING.hide()

        RECORD = frame(WINDOW)
        RECORD.show()

        GUID = frame(WINDOW)
        GUID.hide()

        SIDE_BAR = side_bar(WINDOW)

        frames = (
            WINDOW,
            SIDE_BAR,
            TIME_TABLE,
            PROFESSOR,
            SUBJECT,
            RECORD,
            USER,
            SETTING,
            GUID,
        )
        self.lable_manager = Label(*frames)
        self.button_manager = Button(*frames)
        self.box_manager = Box(*frames)

        #connecting sub windows to buttons
        self.Manage = Manage()
        self.Slot = Slot()

        self.sub_windows()

        connect = Connect(self.lable_manager, self.button_manager, self.box_manager)

        WINDOW.show()

    
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

        self.Slot.lable()
        self.Slot.box()
        self.Slot.button()

        self.button_manager.Widget['manage'].clicked.connect(self.Manage.run)
        self.button_manager.Widget['slot'].clicked.connect(self.Slot.run)

app = QApplication(sys.argv)
root = FrontEnd(app)
sys.exit(app.exec_())