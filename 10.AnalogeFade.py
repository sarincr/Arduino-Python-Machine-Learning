from pyfirmata import Arduino, util
import time

board = pyfirmata.Arduino('/dev/ttyUSB0')
analog_pin = board.get_pin('a:0:i')
it = pyfirmata.util.Iterator(board)
it.start()
analog_pin.enable_reporting()
led = board.get_pin('d:9:p')   
while True:
    reading = analog_pin.read()
    led.write(reading)
    if reading != None:
        voltage = reading * 5.0
        print("Reading= %f\t Voltage= %f" % (reading, voltage))
        time.sleep(1)
