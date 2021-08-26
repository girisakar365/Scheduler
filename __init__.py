import sys
try:
    from .Source import * 
    from .Lable import Label
    from .Button import Button
    from .Box import Box
    from .StyleSheet import WIDGET
    from .Connect import Connect

except Exception:
    from Source import * 
    from Lable import Label
    from Button import Button
    from Box import Box
    from StyleSheet import WIDGET
    from Connect import Connect


class FrontEnd(QMainWindow):

    def __init__(self,app):

        super().__init__()

        scren_resoluction = app.desktop().screenGeometry()
        WIDTH, HEIGHT = scren_resoluction.width() - 10, scren_resoluction.height() - 35
        self.resize(WIDTH,HEIGHT)
        self.setStyleSheet(WIDGET)

        WINDOW = self

        SIDE_BAR = side_bar(WINDOW)
                
        PROFESSOR=frame(WINDOW)
        PROFESSOR.hide()
        
        SUBJECT = frame(WINDOW)
        SUBJECT.hide()
        
        TIME_TABLE = frame(WINDOW)
        TIME_TABLE.hide()
        
        USER = frame(WINDOW)
        USER.hide()
        
        SETTING = frame(WINDOW)
        SETTING.hide()

        RECORD=frame(WINDOW)
        RECORD.show()
        
        GUID = frame(WINDOW)
        GUID.hide()
        
        frames = (WINDOW, SIDE_BAR, TIME_TABLE, PROFESSOR, SUBJECT, RECORD, USER, SETTING, GUID)
        self.lable_manager = Label(*frames)
        self.button_manager = Button(*frames)
        self.box_manager = Box(*frames)

        connect = Connect(self.lable_manager, self.button_manager, self.box_manager)

        WINDOW.show()

app = QApplication(sys.argv)
root=FrontEnd(app)
sys.exit(app.exec_())