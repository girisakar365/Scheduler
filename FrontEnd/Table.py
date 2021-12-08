try : from src import *

except Exception: from .src import *

class Table(QTableWidget):

    def __init__(self, master, x:int, y:int, width:int, height:int):
        super().__init__(master)
        self.setStyleSheet(Style('TABLE'))
        self.move(x, y)
        self.resize(width, height)
        self.hide()
        
    def table(self): return self

    def set_header(self, header: list):
        for i in range( len(header) ):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(header[i]))
            

    def load_data(self, data: list): 
        self.setRowCount(len(data))
        data.reverse()
        
        row = col = 0
        for i in data:
            for j in i:
                self.setItem(row, col, QTableWidgetItem(j))
                col += 1
                
            col = 0
            row += 1