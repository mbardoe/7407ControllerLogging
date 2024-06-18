# xbox_controller_wrapper.py
from wpilib import XboxController, DataLogManager
from wpiutil.log import DataLog, FloatLogEntry, BooleanLogEntry, StringLogEntry


class XboxControllerWrapper(XboxController):
    def __init__(self, name, port):
        super().__init__(port)
        self.name = name
        self.data_log=DataLogManager.getLog()
        base_path = f"Controller/{self.name}/"
        self.logLeftX=FloatLogEntry(self.data_log, base_path + "LeftX" )
        self.logLeftY=FloatLogEntry(self.data_log, base_path + "LeftY" )
        self.logRightX=FloatLogEntry(self.data_log, base_path + "RightX" )
        self.logRightY=FloatLogEntry(self.data_log, base_path+"RightY")
        self.logLeftTriggerAxis=FloatLogEntry(self.data_log, base_path+ "LeftTrigger")
        self.logRightTriggerAxis=FloatLogEntry(self.data_log, base_path+ "RightTrigger")
        self.logAButton=BooleanLogEntry(self.data_log, base_path+"AButton")

        self.logBButton = BooleanLogEntry(self.data_log, base_path + "BButton")
        self.logXButton = BooleanLogEntry(self.data_log, base_path + "XButton")
        self.logYButton = BooleanLogEntry(self.data_log, base_path + "YButton")
        self.logLeftBumper = BooleanLogEntry(self.data_log, base_path + "LeftBumper")
        self.logRightBumper = BooleanLogEntry(self.data_log, base_path + "RightBumper")
        self.logBackButton = BooleanLogEntry(self.data_log, base_path + "BackButton")
        self.logStartButton = BooleanLogEntry(self.data_log, base_path + "StartButton")
        self.logLeftStickButtonPressed = BooleanLogEntry(self.data_log, base_path + "LeftStickButtonPressed")
        self.logRightStickButtonPressed = BooleanLogEntry(self.data_log, base_path + "RightStickButtonPressed")
        self.logLeftStickButtonReleased = BooleanLogEntry(self.data_log, base_path + "LeftStickButtonReleased")
        self.logRightStickButtonReleased = BooleanLogEntry(self.data_log, base_path + "RightStickButtonReleased")

    def logState(self):


        # Log axis states
        self.logLeftX.append(self.getLeftX())
        self.logLeftY.append(self.getLeftY())
        self.logRightX.append(self.getRightX())
        self.logRightY.append(self.getRightY())
        self.logLeftTriggerAxis.append(self.getLeftTriggerAxis())
        self.logRightTriggerAxis.append(self.getRightTriggerAxis())


        # Log button states
        self.logAButton.append(self.getAButton())
        self.logBButton.append(self.getBButton())
        self.logXButton.append(self.getXButton())
        self.logYButton.append(self.getYButton())
        self.logLeftBumper.append(self.getLeftBumper())
        self.logRightBumper.append(self.getRightBumper())
        self.logBackButton.append(self.getBackButton())
        self.logStartButton.append(self.getStartButton())
        self.logLeftStickButtonPressed.append(self.getLeftStickButtonPressed())
        self.logRightStickButtonPressed.append(self.getRightStickButtonPressed())
        self.logLeftStickButtonReleased.append(self.getLeftStickButtonReleased())
        self.logRightStickButtonReleased.append(self.getRightStickButtonReleased())


