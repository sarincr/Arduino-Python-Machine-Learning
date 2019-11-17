import pyfirmata
import time
board = pyfirmata.Arduino('/dev/ttyUSB0')
switch_pin = board.get_pin('d:7:i')
it = pyfirmata.util.Iterator(board)
it.start()
switch_pin.enable_reporting()
while True:
    input_state = switch_pin.read()
    if input_state == False:
        print('Button Not Pressed')
        time.sleep(0.2)
