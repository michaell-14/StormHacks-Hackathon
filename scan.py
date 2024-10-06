import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C
import time

i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)
pn532.SAM_configuration()

print("Waiting for an NFC card...")
tag1 = None
tag2 = None

while True:
    print("Waiting for an NFC card..." + "\n")
    uid = pn532.read_passive_target() #attempts to read a card
    if tag1 is None:
            tag1 = [hex(i) for i in uid]
            print("tag1: ", tag1)
    elif [hex(i) for i in uid] == tag1:
        print("Same card")
    else:
        tag2 = [hex(i) for i in uid]
        print("tag2: ", tag2)
        break
    time.sleep(0.25)
if tag1 and tag2 != None:
    print("Both tags found")

