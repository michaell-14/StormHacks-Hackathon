from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C
import time
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)
pn532.SAM_configuration()

tags = []
f = 0

while f == 0:
    uid = pn532.read_passive_target()  # attempts to read a card
    if uid is not None:
        tag = [hex(i) for i in uid]
        if tag not in tags:
            tags.append(tag)
            print("New tag found: ", tag)
        else:
            print("Same card")

        if tags.__len__() == 2:
            f=1
            print("Two tags found")
    time.sleep(0.05)

