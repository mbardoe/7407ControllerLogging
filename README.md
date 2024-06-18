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