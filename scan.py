import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C
import time

i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)
pn532.SAM_configuration()

print("Waiting for an NFC card...")
while True:
    print("Waiting for an NFC card..." + "\n")
    uid = pn532.read_passive_target() #attempts to read a card
    print([hex(i) for i in uid])
    if uid is not None:
        print("Found card with UID:", [hex(i) for i in uid])
        tag1 = [hex(i) for i in uid]
        print("tag1: ", tag1)
        continue
    time.sleep(.25)
    if uid is tag1:
        print("Same card")
        continue
    if uid is not tag1: 
        tag2 = [hex(i) for i in uid]
        print("tag2: ", tag2)
        break
if tag1 and tag2 != None:
    print("Both tags found")

