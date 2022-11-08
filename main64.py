import threading
import time
from main66 import *
from main67 import *
from main68 import *


s = threading.Thread(target=func1)
o = threading.Thread(target=func2)
sq = threading.Thread(target= func3)

s.start()
o.start()
sq.start()
