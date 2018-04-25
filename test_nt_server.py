from networktables import NetworkTables
import time

import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize()


while True:
    time.sleep(1)
