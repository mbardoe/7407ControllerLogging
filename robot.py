#
from wpilib import DataLogManager, DriverStation
from toolkit.oi.loggedcontroller import LoggedXboxController

from commands2 import TimedCommandRobot, CommandScheduler

class SimRobot(TimedCommandRobot):
    def __init__(self):
        super().__init__(.02) # 20 ms period
        self.controller_wrappers = []

    def robotInit(self):

        DataLogManager.start() # Start the data logger

        # Record both DS control and joystick data
        DriverStation.startDataLog(DataLogManager.getLog())

        # (alternatively) Record only DS control data
        #DriverStation.startDataLog(DataLogManager.getLog(), False)

        # Initialize the Xbox controller wrappers with names (assuming ports 0 and 1 for two controllers)
        self.controller_wrappers.append(LoggedXboxController("Driver", 0))
        #self.controller_wrappers.append(XboxControllerWrapper("Operator", 1))

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # Log the full state of each controller
        for wrapper in self.controller_wrappers:
            wrapper.logState()

        # Update the command scheduler
        CommandScheduler.getInstance().run()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def testInit(self):
        pass

    def testPeriodic(self):
        pass
