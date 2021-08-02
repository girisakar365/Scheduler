from Source import * 
from Lable import Label
from Button import Button
from Box import Box
from StyleSheet import FRAME, WIDGET
from Connect import Connect

class FrontEnd(QMainWindow):

    def __init__(self,app):

        super().__init__()

        scren_resoluction = app.desktop().screenGeometry()
        WIDTH, HEIGHT = scren_resoluction.width() - 10, scren_resoluction.height() - 35
        self.resize(WIDTH,HEIGHT)
        self.setMinimumSize(WIDTH,HEIGHT)

        self.setStyleSheet(WIDGET)

        WINDOW = self

        SIDE_BAR = side_bar(WINDOW)

        RECORD=frame(WINDOW)
                
        PROFESSOR=frame(WINDOW)
        PROFESSOR.hide()
        
        SUBJECT = frame(WINDOW)
        SUBJECT.hide()
        
        TIME_TABLE = frame(WINDOW)
        TIME_TABLE.hide()
        
        USER = frame(WINDOW)
        USER.hide()
        
        SETTING = frame(WINDOW)
        MENU_BAR = frame(SETTING)
        MENU_BAR.setStyleSheet(FRAME)
        MENU_BAR.setFixedSize(280,370)
        MENU_BAR.setGraphicsEffect(shadow(100))
        MENU_BAR.move(2,215)
        SETTING.hide()
        
        GUID = frame(WINDOW)
        GUID.hide()
        
        frames = (WINDOW, SIDE_BAR, TIME_TABLE, PROFESSOR, SUBJECT, RECORD, USER, SETTING, GUID, MENU_BAR)
        self.lable_manager = Label(*frames)
        self.button_manager = Button(*frames)
        self.box_manager = Box(*frames)

        connect=Connect(self.lable_manager,self.button_manager,self.box_manager)

        WINDOW.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    root=FrontEnd(app)
    sys.exit(app.exec_())