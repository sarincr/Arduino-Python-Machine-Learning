import pyfirmata

import time


board = pyfirmata.Arduino('/dev/ttyUSB0')


while True:

    board.digital[13].write(1)

    time.sleep(.5)

    board.digital[13].write(0)

    time.sleep(.5)
