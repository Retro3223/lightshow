from threading import Thread

from commands.example import BlinkyCommand, OtherBlinkyCommand
from controller import Controller
from subsystems import LEDSubsystem


class MyController(Controller):
    def __init__(self):
        super().__init__()
        self.leds = LEDSubsystem()

        self.leds.setDefaultCommand(BlinkyCommand())

    def shutdown(self):
        self.leds.clearStrip()

    def scheduleit(self):
        import time
        time.sleep(2)
        OtherBlinkyCommand().start()



controller = MyController()
Thread(target=lambda: controller.scheduleit()).start()
controller.start()


