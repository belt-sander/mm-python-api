#!/usr/bin/python

# System imports
import sys
# Custom imports
sys.path.append("..")

from MachineMotion import *

# Define a callback to process controller gCode responses (if desired)
def templateCallback(data):
   print ( "Controller gCode responses " + data )

machine_motion_example = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows, templateCallback)

#When starting a program, one must remove the software stop before moving
print("--> Removing software stop")
machine_motion_example.releaseEstop()
print("--> Resetting system")
machine_motion_example.resetSystem()

# Send a stop command to the Machine (even if it is not moving yet !)

for i in range(0, 50):
   machine_motion_example.emitStop()
   machine_motion_example.emitRelativeMove(1, "positive", 10)

print ( "--> Machine Stopped" )
