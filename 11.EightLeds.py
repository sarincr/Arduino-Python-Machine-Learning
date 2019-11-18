import pyfirmata

board = pyfirmata.Arduino("/dev/ttyUSB0")
ledPins = [6,7,8,9,10,11,12,13]

while True:
    for x in range(0,8):
        board.digital[ledPins[x]].write(1)
        board.pass_time(1)
        board.digital[ledPins[x]].write(0)
        board.pass_time(1)
