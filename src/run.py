from threading import Thread

from commands.example import BlinkyCommand, OtherBlinkyCommand
from controller import Controller
from subsystems import LEDSubsystem
from networktables import NetworkTables


import logging
logging.basicConfig(level=logging.DEBUG)

class MyController(Controller):
    def __init__(self):
        super().__init__()
        NetworkTables.initialize("10.32.23.10")
        self.table = NetworkTables.getTable("LEDS")
        self.table.addEntryListener(self.valueChanged)
        self.leds = LEDSubsystem()

        self.leds.setDefaultCommand(BlinkyCommand())

    def shutdown(self):
        self.leds.clearStrip()


    def valueChanged(self, table, key, value, isNew):
        if key == 'nacho':
            OtherBlinkyCommand().start()



controller = MyController()
controller.start()


