# xbox_controller_wrapper.py
from wpilib import XboxController, DataLogManager


class XboxControllerWrapper:
    def __init__(self, name, port):
        self.name = name
        self.controller = XboxController(port)

    def logState(self):
        base_path = f"Controller/{self.name}/"

        # Log axis states
        DataLogManager.log(base_path + "LeftX", self.controller.getX(XboxController.Hand.kLeft))
        DataLogManager.log(base_path + "LeftY", self.controller.getY(XboxController.Hand.kLeft))
        DataLogManager.log(base_path + "RightX", self.controller.getX(XboxController.Hand.kRight))
        DataLogManager.log(base_path + "RightY", self.controller.getY(XboxController.Hand.kRight))
        DataLogManager.log(base_path + "LeftTrigger", self.controller.getTriggerAxis(XboxController.Hand.kLeft))
        DataLogManager.log(base_path + "RightTrigger", self.controller.getTriggerAxis(XboxController.Hand.kRight))

        # Log button states
        DataLogManager.log(base_path + "AButton", self.controller.getAButton())
        DataLogManager.log(base_path + "BButton", self.controller.getBButton())
        DataLogManager.log(base_path + "XButton", self.controller.getXButton())
        DataLogManager.log(base_path + "YButton", self.controller.getYButton())
        DataLogManager.log(base_path + "LeftBumper", self.controller.getBumper(XboxController.Hand.kLeft))
        DataLogManager.log(base_path + "RightBumper", self.controller.getBumper(XboxController.Hand.kRight))
        DataLogManager.log(base_path + "BackButton", self.controller.getBackButton())
        DataLogManager.log(base_path + "StartButton", self.controller.getStartButton())
        DataLogManager.log(base_path + "LeftStickButton", self.controller.getStickButton(XboxController.Hand.kLeft))
        DataLogManager.log(base_path + "RightStickButton", self.controller.getStickButton(XboxController.Hand.kRight))

    # Add any additional methods to access controller state
    def getLeftX(self):
        return self.controller.getX(XboxController.Hand.kLeft)

    def getLeftY(self):
        return self.controller.getY(XboxController.Hand.kLeft)

    def getRightX(self):
        return self.controller.getX(XboxController.Hand.kRight)

    def getRightY(self):
        return self.controller.getY(XboxController.Hand.kRight)

    def getAButton(self):
        return self.controller.getAButton()

    # Add other methods as needed
