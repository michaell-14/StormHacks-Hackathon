import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C
from adafruit_pn532 import PN532

i2C = busio.I2C(board.SCL. board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

pn532.SAM_configuration()

print("Waiting for RFID/NFC card...")
while True:
    uid = pn532.read_passive_target(timeout=100)
    if uid is None:
        continue
    print("Found card with UID:", [hex(i) for i in uid]) # Print UID of card
    # Add code here to do something when a card is detected
