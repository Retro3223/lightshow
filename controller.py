import wpilib
from unittest.mock import MagicMock
from wpilib.command import Scheduler, Subsystem, Command

wpilib.RobotState.impl = MagicMock()
wpilib.RobotState.impl.isDisabled.return_value = False
wpilib.RobotState.impl.isEnabled.return_value = True
wpilib.RobotState.impl.isAutonomous.return_value = False
wpilib.RobotState.impl.isOperatorControl.return_value = True
wpilib.RobotState.impl.isTest.return_value = False

class Controller:
    def __init__(self):
        pass

    def start(self):
        scheduler = Scheduler.getInstance()

        for subsystem in scheduler.subsystems:
            subsystem.initDefaultCommand()

        try:
            while True:
                scheduler.run()

        except KeyboardInterrupt:
            self.shutdown()

    def shutdown(self):
        raise NotImplemented('please clear the led strip before terminating!')
