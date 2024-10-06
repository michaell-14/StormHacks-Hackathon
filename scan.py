from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C
import time
import board
import busio
import threading

i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)
pn532.SAM_configuration()

tags = []
lock = threading.Lock()

def scan_tag():

    while True:
        
        uid = pn532.read_passive_target() 
        if uid is not None:
            tag = [hex(i) for i in uid]
            with lock: 
                if tag not in tags:
                    tags.append(tag)
                    print("New tag found: ", tag)
                if tags.__len__() == 2:
                    print("Two tags found")
                    time.sleep(0.05)
                break
        else: 
            continue

def scan_multi(): 
    threads = []
    for i in range(2):
        t = threading.Thread(target=scan_tag)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

scan_tag()
scan_multi()
