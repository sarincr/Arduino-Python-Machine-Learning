import pyfirmata
import numpy as np
import time
board = pyfirmata.Arduino('/dev/ttyUSB0')
switch_pin = board.get_pin('d:7:i')
it = pyfirmata.util.Iterator(board)
it.start()
switch_pin.enable_reporting()
m=[]
while True:
    k = switch_pin.read()
    m=m+[k]
    print(m)
    
    if k == False:
        print('Button Not Pressed')
        time.sleep(0.2)
