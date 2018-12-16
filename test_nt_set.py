from networktables import NetworkTables
import time
import sys

import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize("10.32.23.14")


table = NetworkTables.getTable("LEDS")
time.sleep(0.2)
key = "nacho"
val = sys.argv[1] if len(sys.argv) > 1 else key
print("setting %r to %r" % (key, val))
table.putString(key, val)
time.sleep(0.2)
