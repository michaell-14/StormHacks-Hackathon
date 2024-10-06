import time

#module that provides access to the board's pin mappings
import board

#used for handling I2C and SPI communication
import busio

#DigitalInOut class that handles digital input/output pins
from digitalio import DigitalInOut

#class from Adafruit that interfaces with PN532 chip (over I2C)
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL, board.SDA)

#creates an instance of the PN532_I2C class
    #argument 1: passes the I2C interface to the class instance
    #argument 2: debug set to false (will not print debug messages)
pn532 = PN532_I2C(i2c, debug=False)

#SAM stands for "Selective Anti-collision Mechanism"
#configures the PN532 chip to operate in "card emulation" mode
    #In this mode, PN532 pretends to be a card that can be read by an NFC reader (allows 2-way communication between NFC devices)
pn532.SAM_configuration()

tagsAndNames = {
    "d9da2303": "Lion",
    "95382303": "Banana",
    "0a451d03": "Bunny",
    "81512303": "Carrot",
    "7c172403": "Monkey",
    "5d787800": "Meat",
}

animalsAndFoods = {
    "lion": "Meat",
    "Bunny": "Carrot",
    "Monkey": "Banana"
}

def readTag():
    while True:
        uid = pn532.read_passive_target(timeout = 5) #attempts to read a card
        if uid is not None:
            uidKey = ''.join([hex(i)[2:].zfill(2) for i in uid])
            return tagsAndNames.get(uidKey)
        else:
            continue

def checkMatch(animal, food):
    if animalsAndFoods.get(animal) == food:
        return True
    else:
        return False