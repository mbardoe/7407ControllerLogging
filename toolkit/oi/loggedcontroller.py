# A subclass of the XboxController class
# that allows for state of the controller to
# be logged.

from wpilib import XboxController, DataLogManager
from wpiutil.log import DataLog, FloatLogEntry, BooleanLogEntry, StringLogEntry


class LoggedXboxController(XboxController):
    """
    A subclass of XboxController whose state can be logged.
    """
    def __init__(self, name, port):
        """
        Initializer for LoggedXboxController.

        :param name: The name of the XboxController. Name will be used in logs.
        :param port: The port of the XboxController.
        """
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
        self.logPOVValues=FloatLogEntry(self.data_log, base_path+ "POVValues")

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
        #self.logPOVUpButton = BooleanLogEntry(self.data_log, base_path + "POVUpButton")
        #self.logPOVDownButton = BooleanLogEntry(self.data_log, base_path + "POVDownButton")
        #self.logPOVRightButton = BooleanLogEntry(self.data_log, base_path + "POVRightButton")
        #self.logPOVLeftButton = BooleanLogEntry(self.data_log, base_path + "POVLeftButton")


    def logState(self, timestamp=0):
        """
        Log the state of the XboxController.

        :param timestamp: The timestamp of the state.

        """
        # Log axis states
        self.logLeftX.append(self.getLeftX(), timestamp)
        self.logLeftY.append(self.getLeftY(), timestamp)
        self.logRightX.append(self.getRightX(), timestamp)
        self.logRightY.append(self.getRightY(), timestamp)
        self.logLeftTriggerAxis.append(self.getLeftTriggerAxis(), timestamp)
        self.logRightTriggerAxis.append(self.getRightTriggerAxis(), timestamp)
        self.logPOVValues.append(self.getPOV(), timestamp)


        # Log button states
        self.logAButton.append(self.getAButton(), timestamp)
        self.logBButton.append(self.getBButton(), timestamp)
        self.logXButton.append(self.getXButton(), timestamp)
        self.logYButton.append(self.getYButton(), timestamp)
        self.logLeftBumper.append(self.getLeftBumper(), timestamp)
        self.logRightBumper.append(self.getRightBumper(), timestamp)
        self.logBackButton.append(self.getBackButton(), timestamp)
        self.logStartButton.append(self.getStartButton(), timestamp)
        self.logLeftStickButtonPressed.append(self.getLeftStickButtonPressed(), timestamp)
        self.logRightStickButtonPressed.append(self.getRightStickButtonPressed(), timestamp)
        self.logLeftStickButtonReleased.append(self.getLeftStickButtonReleased(), timestamp)
        self.logRightStickButtonReleased.append(self.getRightStickButtonReleased(), timestamp)
        #self.logPOVUpButton.append(self.POVUp())
        self.data_log.flush()


