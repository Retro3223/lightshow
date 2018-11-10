from .apa102 import APA102
from wpilib.command import Subsystem


class LEDSubsystem(Subsystem, APA102):
    @classmethod
    def getInstance(cls):
        return cls.instance

    def __init__(self):
        Subsystem.__init__(self)
        APA102.__init__(self,
                        num_led=144,
                        global_brightness=5,
                        order='rgb',
                        max_speed_hz=1000000)
        LEDSubsystem.instance = self

