from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyUSB0')
print('Start')
for i in range(10):
    board.digital[13].write(1)
    time.sleep(.2)
    board.digital[13].write(0)
    time.sleep(.2)
print ('End')
