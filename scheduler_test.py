import wpilib
from unittest.mock import MagicMock
from wpilib.command import Scheduler, Subsystem, Command

wpilib.RobotState.impl = MagicMock()
wpilib.RobotState.impl.isDisabled.return_value = False
wpilib.RobotState.impl.isEnabled.return_value = True
wpilib.RobotState.impl.isAutonomous.return_value = False
wpilib.RobotState.impl.isOperatorControl.return_value = True
wpilib.RobotState.impl.isTest.return_value = False

class Subsystem1(Subsystem):
    def __init__(self):
        super().__init__('s1')

    def initDefaultCommand(self):
        self.setDefaultCommand(C1())

s1 = Subsystem1()

class C1(Command):
    def __init__(self):
        super().__init__('c1')
        self.requires(s1)

    def execute(self):
        print ('tacos')
scheduler = Scheduler.getInstance()
print (scheduler)

for subsystem in scheduler.subsystems:
    subsystem.initDefaultCommand()

for i in range(10):
    try:
        scheduler.run()
    except Exception as error:
        scheduler.removeAll()
