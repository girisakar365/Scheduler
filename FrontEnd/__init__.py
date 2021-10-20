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