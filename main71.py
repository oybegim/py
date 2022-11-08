import threading
import time 

def x1():
    for x in range(0, 150, 1):
    
        time.sleep(0.1)
        print(x)
def b1():
    for b in range(0, 150, 1):
        time.sleep(0.1)
        print(b)
def c1():
    for c in range(0, 150, 1):
        time.sleep(0.1)
        print(c)
x2 = threading.Thread(target=x1)
b2 = threading.Thread(target=b1)
c2 = threading.Thread(target=c1)

x2.start()
b2.start()
c2.start()