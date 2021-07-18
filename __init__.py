from source import * 
from Lable import Label
from Button import Button
from Box import Box

class FrontEnd(QMainWindow):

    def __init__(self,app):

        super().__init__()

        scren_resoluction = app.desktop().screenGeometry()
        WIDTH, HEIGHT = scren_resoluction.width(), scren_resoluction.height()
        self.resize(WIDTH,HEIGHT)

        self.setStyleSheet('''QWidget{
		color:#ffffff;
		background-color:#1F2428;}''')

        WINDOW=self
        

        SIDE_BAR=side_bar(self)
        
        TIME_TABLE=frame(self)
        # TIME_TABLE.hide()
        
        PROFESSOR=frame(self)
        PROFESSOR.hide()
        
        SUBJECT=frame(self)
        SUBJECT.hide()

        lable_manager=Label(WINDOW,SIDE_BAR,TIME_TABLE,PROFESSOR,SUBJECT)
        button_manager=Button(WINDOW,SIDE_BAR,TIME_TABLE,PROFESSOR,SUBJECT)
        box_manager=Box(WINDOW,SIDE_BAR,TIME_TABLE,PROFESSOR,SUBJECT)

        self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    root=FrontEnd(app)
    sys.exit(app.exec_())