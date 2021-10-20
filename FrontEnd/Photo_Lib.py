try: 
    from .src import (QApplication,PhotoLib, image, Cache)

except Exception: 
    from src import (QApplication,PhotoLib, image, Cache)

import sys

__init__ = QApplication(sys.argv) # APPLICATION BUILD BEFORE PIXMAP

DELETE = image( PhotoLib.get(1) )
MAIL = image( PhotoLib.get(3) )
PDF = image( PhotoLib.get(4) )
TIME_TABLE = image( PhotoLib.get(7) )
PROFESSOR = image( PhotoLib.get(8) )
SUBJECT = image( PhotoLib.get(9) )
RECORD = image( PhotoLib.get(10) )
XLSX = image( PhotoLib.get(27) )
LOGIN = image( PhotoLib.get(29) )
ACCOUNT = image( PhotoLib.get(30) )
SCHOLAR = PhotoLib.get(28) # PIXMAP
EYE_CLOSED = image( PhotoLib.get(31) )
EYE_OPENED = image( PhotoLib.get(32) )
KEY = image( PhotoLib.get(33) )
UI_L = image( PhotoLib.get(38) )
UI_D = image( PhotoLib.get(39) )

__ = {'SCOPE':{
    0: image( PhotoLib.get(5) ),
    1: image( PhotoLib.get(44) )
},
'USER':{
    0:image( PhotoLib.get(11) ),
    1:image( PhotoLib.get(12) )
},
'GEAR':{
    0:image( PhotoLib.get(14) ),
    1:image( PhotoLib.get(13) )
},
'WHAT':{
    0: image( PhotoLib.get(16) ),
    1: image( PhotoLib.get(15) )
},
'PEN':{
    0: image( PhotoLib.get(17) ),
    1: image( PhotoLib.get(2) )
},
'MARK':{
    0:image( PhotoLib.get(19) ),
    1:image( PhotoLib.get(18) )
},
'GENERATOR':{
    0:image( PhotoLib.get(20) ),
    1:image( PhotoLib.get(6) )
},
'NEXT':{
    0:image( PhotoLib.get(26) ),
    1:image( PhotoLib.get(25) )
},
'SECURE':{
    0:image( PhotoLib.get(34) ),
    1:image( PhotoLib.get(35) )
},
'KEYBOARD':{
    0:image( PhotoLib.get(36) ),
    1:image( PhotoLib.get(37) )
},
'TICK':{
    0:image( PhotoLib.get(40) ),
    1:image( PhotoLib.get(41) )
},
'BACK':{
    0:image( PhotoLib.get(42) ),
    1:image( PhotoLib.get(43) )
}
}


def ico(NAME):
    return __[NAME][Cache.fetch('switch','ui')]