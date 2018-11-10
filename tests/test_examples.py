from commands.example import BlinkyCommand, OtherBlinkyCommand
from subsystems import LEDSubsystem


def test_blinky(spidev):
    leds = LEDSubsystem()
    b = BlinkyCommand()
    b.initialize()
    b.execute()
    b.isFinished()
    b.end()


def test_otherblinky(spidev):
    leds = LEDSubsystem()
    b = OtherBlinkyCommand()
    b.initialize()
    b.execute()
    b.isFinished()
    b.end()
