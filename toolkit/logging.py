
from wpilib import DataLogManager

class LoggedCommand():
    def __init__(self, command, label, value):
        super().__init__()
        self.command = command
        self.label = label
        self.value = value

    def initialize(self):
        self.command.initialize()
        self.logData(self.label, self.value)

    def execute(self):
        self.command.execute()

    def isFinished(self):
        return self.command.isFinished()

    def end(self, interrupted):
        self.command.end(interrupted)

    def logData(self, label, value):
        DataLogManager.log(label, value)

