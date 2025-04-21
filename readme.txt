This project is intended for use with the RoboMaster EP Core, programmed with the developer SDK.
Official SDK documentation: https://robomaster-dev.readthedocs.io/en/latest/
Official manuals / product info + app download: https://www.dji.com/downloads/products/robomaster-ep-core#other

Before using the SDK:

Be sure to calibrate both the arm and wheels of the robomaster (can be done in the official app^).
If there are 2 or more robots, make sure they are calibrated the exact same way.

For SDK installation:

Follow the instructions in the above SDK documentation. A virtual environment is reccomended (as an older
version of python is needed to run the SDK, all code here was ran on Python 3.7.8).
If the installation fails, uninstall everything then try again.

While using the SDK:

Ensure that markers have minimal obstruction (if using tape, put it on the back of the markers).
Ensure that the markers are high enough to not be obstructed by the arm or the object the arm is holding.
Ensure that the robot(s) are close enough to the router to avoid any sort of potential lag.
Ensure that your code accounts for exceptions/outliers, as the sensors often give highly inaccurate information or no information at all.
If the robot is rotating to search for markers, try to keep it below 20deg/s, as it will typically fail to recognize the marker if going faster.
If attempting to view 2+ camera feeds, use CV2 to access frames instead of the traditional "display=True" method.
If attempting to download the camera feed, use only 30fps, as any slower/faster will speed up / slow down camera footage.


