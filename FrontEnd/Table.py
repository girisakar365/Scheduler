try : from src import *

except Exception: from .src import *

class Table:

    def __init__(self, master, x:int, y:int, width:int, height:int):
        self.Table = self.table(master, x, y, width, height)

    def table(self, master, x, y, width, height):
        _table = QTableWidget(master)
        _table.setStyleSheet(TABLE)
        _table.move(x, y)
        _table.resize(width, height)
        _table.hide()

        return _table

    def row_and_cols(self):pass