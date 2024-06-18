from toolkit.logging import LoggedCommand


class MoveForward(LoggedCommand):
    def __init__(self, drivetrain, speed):
        super().__init__(self, "MoveForward", speed)
        self.drivetrain = drivetrain
        self.speed = speed

    def initialize(self):
        self.drivetrain.drive_distance(self.speed)

    def isFinished(self):
        return False

    def end(self, interrupted):
        self.drivetrain.stop()
        super().end(interrupted)