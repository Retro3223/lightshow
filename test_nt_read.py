from networktables import NetworkTables
import time

import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize("127.0.0.1")


table = NetworkTables.getTable("LEDS")
time.sleep(.2)
nacho = table.getString("nacho", None)
time.sleep(.2)
print("nacho: %s" % (nacho,))
