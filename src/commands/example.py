import wpilib
from wpilib.command import Command
from subsystems import LEDSubsystem


class BlinkyCommand(Command):
    def __init__(self):
        super().__init__()
        self.leds = LEDSubsystem.getInstance()
        self.requires(self.leds)
        self.timer = wpilib.Timer()
        self.state = False

    def initialize(self):
        self.leds.clearStrip()
        self.timer.start()

    def execute(self):
        # this method is executed approximately once every 5 ms
        if self.timer.get() > 0.5:
            self.timer.reset()
            if self.state:
                self.leds.setPixel(1, 135, 206, 250)
            else:
                self.leds.setPixel(1, 135, 0, 0)

            self.state = not self.state
            self.leds.show()

    def isFinished(self):
        pass

    def end(self):
        self.leds.clearStrip()


class OtherBlinkyCommand(Command):
    def __init__(self):
        super().__init__()
        self.leds = LEDSubsystem.getInstance()
        self.requires(self.leds)
        self.timer = wpilib.Timer()
        self.state = False
        self.counter = 0

    def initialize(self):
        self.leds.clearStrip()
        self.timer.start()

    def execute(self):
        # this method is executed approximately once every 5 ms
        if self.timer.get() > 0.5:
            self.counter += 1
            self.timer.reset()
            if self.state:
                self.leds.setPixel(1, 135, 206, 250)
            else:
                self.leds.setPixel(1, 0, 0, 234)

            self.state = not self.state
            self.leds.show()

    def isFinished(self):
        return self.counter > 10

    def end(self):
        self.leds.clearStrip()
