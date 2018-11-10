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
        self.leds.clear_strip()
        self.timer.start()

    def execute(self):
        # this method is executed approximately once every 5 ms
        if self.timer.get() > 0.5:
            self.timer.reset()
            if self.state:
                self.leds.set_pixel(1, 135, 206, 250)
            else:
                self.leds.set_pixel(1, 135, 0, 0)

            self.state = not self.state
            self.leds.show()

    def isFinished(self):
        pass

    def end(self):
        self.leds.clear_strip()


class OtherBlinkyCommand(Command):
    def __init__(self):
        super().__init__()
        self.leds = LEDSubsystem.getInstance()
        self.requires(self.leds)
        self.timer = wpilib.Timer()
        self.state = False
        self.counter = 0

    def initialize(self):
        self.leds.clear_strip()
        self.timer.start()

    def execute(self):
        # this method is executed approximately once every 5 ms
        if self.timer.get() > 0.5:
            self.counter += 1
            self.timer.reset()
            if self.state:
                self.leds.set_pixel(1, 135, 206, 250)
            else:
                self.leds.set_pixel(1, 0, 0, 234)

            self.state = not self.state
            self.leds.show()

    def isFinished(self):
        return self.counter > 10

    def end(self):
        self.leds.clear_strip()


class StrafeCommand(Command):
    def __init__(self):
        super().__init__()
        self.leds = LEDSubsystem.getInstance()
        self.requires(self.leds)
        self.timer = wpilib.Timer()

        self.color1 = (135, 206, 250)

        self.pos = 0

    def initialize(self):
        self.leds.clear_strip()
        self.timer.start()
        self.paint()

    def execute(self):
        if self.timer.get() > 0.015:
            print (self.timer.get())
            self.timer.reset()
            self.pos = (self.pos + 1) % self.leds.num_led
            self.paint()
        

    def paint(self):
        for i in range(0, self.leds.num_led):
            self.leds.set_pixel(i, 0,0,0)
        for i in range(self.pos, min(self.pos+10, self.leds.num_led)):
            self.leds.set_pixel(i, *self.color1)

        self.leds.show()

    def isFinished(self):
        return False

    def end(self):
        self.leds.clear_strip()
