from FrontEnd import FrontEnd
from FrontEnd.src import QApplication
from Function import Function

import sys
app = QApplication(sys.argv)
root = FrontEnd(app)
Conn = Function(root.lable_manager, root.button_manager, root.box_manager, root.Manage, root.Slot)
root.show()
sys.exit(app.exec_())