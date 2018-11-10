from networktables import NetworkTables
import time

import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize("10.32.23.14")


table = NetworkTables.getTable("LEDS")
table.putString("nacho", "nacho")
time.sleep(1)
