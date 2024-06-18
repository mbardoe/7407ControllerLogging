# Controller Logging Example 
## 7407 Robot Code

### Goals

In this repository we are going to create a robot that can drive in real life and in simulation. 
We are going to practice the philosophy of "Hardware Abstraction", and then use those hardware abstractions 
to log essential information about the inputs that are necessary to run the code in replay, or at
least show the information on the dashboard. 

* Create a robot that can run in sim
* Start some kind of logging
* Run the robot in simulator and see if the logging works
* Replay the log in the simulator


### The Setup

As always you may need to install `robotpy`. To do this

    ```bash
    python3 -m pip install robotpy
    python3 -m robotpy init
    python3 -m robotpy sync
    ```

### Setting up `robot.py`

In `robot.py` we use the WPILib DataLogManager to create a log, and to use the `startDataLog` method
to record the DS control and joystick data (but it doesn't seem that the xboxcontroller is being recorded).
We will log the inputs of the controllers. To do this we subclass the `Xboxcontroller` class in WPILib, and 
this we will create a method called, `logState`. This method can take a timestamp and add it to the log
for the following values of the XboxController:

| State Variable           | Type|
|--------------------------|-----|
| LeftX                    | float|
| LeftY                    | float|
| RightX                   | float|
| RightY                   | float|
| LeftTriggerAxis          | float|
| RightTriggerAxis         | float|
| POVValues                | float|
| AButton                  | boolean|
| BButton                  | boolean|
| XButton                  | boolean|
| YButton                  | boolean|
| LeftBumper               | boolean|
| RightBumper              | boolean|
| BackButton               | boolean|
| StartButton              | boolean|
| LeftStickButtonPressed   | boolean|
| LeftStickButtonReleased  | boolean|
| RightStickButtonPressed  | boolean|
| RightStickButtonReleased | boolean|

### Drive Sim

We want to setup a swerve drive that is logged as well, in the way similar to what is happening with AdvantageKit.
We will need to create an "interface" that describes the methods that come from a motor or a simulated motor. Those
values are logged regularly. We will look to take the swerve drive from 7407's swerve drive subsystem and commands. Then
we will make changes to that so that it can be logged regularly.

#### Changes to the swerve drive from 7407 2024


