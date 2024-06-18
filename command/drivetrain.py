from toolkit.logging import LoggedCommand
from subsystem import Drivetrain

class DriveSwerveCustom(LoggedCommand):
    def __init__(self, drivetrain: Drivetrain):
        super().__init__()
        self.drivetrain = drivetrain
        self.addRequirements(drivetrain)

    def execute(self):
        self.drivetrain.drive_swerve_custom()

    def isFinished(self):
        return True

    def end(self):
        self.drivetrain.drive_swerve_custom(0, 0, 0)