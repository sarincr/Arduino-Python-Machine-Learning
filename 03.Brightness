import time
import pyfirmata

delay = 0.3
brightness = 0

board = pyfirmata.Arduino("/dev/ttyUSB0")

led = board.get_pin('d:9:p')            
while True:
# increase
    for i in range(0, 10):
        brightness = brightness + 0.1
        print("Setting brightness to %s" % brightness)
        led.write(brightness)
        board.pass_time(delay)
