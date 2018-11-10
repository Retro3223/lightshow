from commands.example import BlinkyCommand, OtherBlinkyCommand, StrafeCommand
from controller import Controller
from subsystems import LEDSubsystem
from networktables import NetworkTables


import logging
logging.basicConfig(level=logging.DEBUG)

class MyController(Controller):
    def __init__(self):
        super().__init__()
        NetworkTables.initialize("10.32.23.14")
        self.table = NetworkTables.getTable("LEDS")
        self.table.addEntryListener(self.valueChanged)
        self.leds = LEDSubsystem()

        self.leds.setDefaultCommand(StrafeCommand())

    def shutdown(self):
        self.leds.clear_strip()


    def valueChanged(self, table, key, value, isNew):
        if key == 'nacho':
            OtherBlinkyCommand().start()


if __name__ == '__main__':
    controller = MyController()
    controller.start()


