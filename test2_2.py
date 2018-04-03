from controller import Controller
from threading import Thread
from apa102 import APA102
import wpilib
from wpilib.command import Subsystem, Command

class LEDSubsystem(Subsystem, APA102):
    def __init__(self):
        Subsystem.__init__(self)
        APA102.__init__(self,
            numLEDs=144, 
            globalBrightness=5, 
            order='rgb') 

    def initDefaultCommand(self):
        self.setDefaultCommand(StrafeyCommand())

led_subsystem = None

class StrafeyCommand(Command):
    def __init__(self):
        super().__init__()
        self.leds = led_subsystem
        self.requires(self.leds)
        self.timer = wpilib.Timer()
        self.state = False

    def initialize(self):
        self.leds.clearStrip()
        self.timer.start()

    def execute(self):
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

class StrafeyCommand2(Command):
    def __init__(self):
        super().__init__()
        self.leds = led_subsystem
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


class MyController(Controller):
    def __init__(self):
        global led_subsystem
        super().__init__()
        led_subsystem = self.leds = LEDSubsystem()

    def shutdown(self):
        self.leds.clearStrip()

    def scheduleit(self):
        print('schiedule')
        import time
        time.sleep(2)
        StrafeyCommand2().start()



controller = MyController()
Thread(target=lambda: controller.scheduleit()).start()
controller.start()


