#module that provides access to the board's pin mappings
import board

#used for handling I2C and SPI communication adfa
import busio

import threading
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
    "d9da2303": "lion",
    "95382303": "banana",
    "0a451d03": "bunny",
    "81512303": "carrot",
    "7c172403": "monkey",
    "5d787800": "meat",
}

animalsAndFoods = {
    "lion": "meat",
    "bunny": "carrot",
    "monkey": "banana"
}

def readTagBackground(tag_var):
    global input1, input2
    while True:
        uid = pn532.read_passive_target(timeout=5)  # Read NFC tag
        if uid is not None:
            # Convert UID to string key
            uidKey = ''.join([hex(i)[2:].zfill(2) for i in uid])
            print(f"Tag detected: {uidKey}")
            
            # Look up tag in dictionary and update the corresponding global variable
            if tag_var == "input1":
                input1 = tagsAndNames.get(uidKey)
                print(f"Animal tag detected: {input1}")
            elif tag_var == "input2":
                input2 = tagsAndNames.get(uidKey)
                print(f"Food tag detected: {input2}")
            return  # Exit the function once a tag is detected

def start_scan_animal():
    animal_thread = threading.Thread(target=readTagBackground, args=("input1",))
    animal_thread.start()

def start_scan_food():
    food_thread = threading.Thread(target=readTagBackground, args=("input2",))
    food_thread.start()