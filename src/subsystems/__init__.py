from .apa102 import APA102
from wpilib.command import Subsystem


class LEDSubsystem(Subsystem, APA102):
    @classmethod
    def getInstance(cls):
        return cls.instance

    def __init__(self):
        Subsystem.__init__(self)
        APA102.__init__(self,
                        numLEDs=144,
                        globalBrightness=5,
                        order='rgb')
        LEDSubsystem.instance = self

