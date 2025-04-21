import robomaster
from robomaster import *
import cv2
import time
import threading
import math
# this is the code for a single agent pickup/dropoff scenerio


# important variables / functions!!

dist = 999 #placeholder
origin = [0,0,0]
markerlists = [[0,0,0,0,'0']]


def forward(v):
    ep_chassis.drive_speed(x=v,y=0,z=0)
def backward(v):
    ep_chassis.drive_speed(x=-v,y=0,z=0)
def right(v):
    ep_chassis.drive_speed(x=0,y=v,z=0)
def left(v):
    ep_chassis.drive_speed(x=0,y=-v,z=0)
def rotate_right(v):
    ep_chassis.drive_speed(x=0,y=0,z=v)
def rotate_left(v):
    ep_chassis.drive_speed(x=0,y=0,z=-v)
def halt():
    ep_chassis.drive_speed(x=0,y=0,z=0,timeout=None)
    time.sleep(0.25)

def sub_data_handler_d(sub_info):
    distance = sub_info
    #print("tof1:{0}  tof2:{1}  tof3:{2}  tof4:{3}".format(distance[0], distance[1], distance[2], distance[3]))
    global dist
    dist = distance[0]
def sub_data_handler_p(sub_info):
    #print("x:{0}  y:{1}".format(sub_info[0], sub_info[1]))
    global position
    position = sub_info[:2]
def sub_data_handler_z(sub_info):
    #print("yaw:{0}  pitch:{1}, roll{2}".format(sub_info[0], sub_info[1], sub_info[2]))
    global angle
    angle = sub_info[0]
    # global plz
    # plz = sub_info

    # use above commentedprint statements / global variables if you need to check values while running

class MarkerInfo:

    def __init__(self, x, y, w, h, info):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._info = info

    @property
    def pt1(self):
        return int((self._x - self._w / 2) * 1280), int((self._y - self._h / 2) * 720)

    @property
    def pt2(self):
        return int((self._x + self._w / 2) * 1280), int((self._y + self._h / 2) * 720)

    @property
    def center(self):
        return int(self._x * 1280), int(self._y * 720)

    @property
    def text(self):
        return self._info


markers = []

def on_detect_marker(marker_info):
    number = len(marker_info)
    global markerlists
    check = False
    markers.clear()
    for i in range(0, number):
        x, y, w, h, info = marker_info[i]
        markers.append(MarkerInfo(x, y, w, h, info))
        # print("marker:{0} x:{1}, y:{2}, w:{3}, h:{4}".format(info, x, y, w, h))
        check = True
        markerlists = marker_info + [[0,0,0,0,'0']] # iteration placeholder
    if check == False:
        markerlists = markerlists + [[0,0,0,0,'0']] # iteration placeholder


# centers on marker by moving left/right until centered
def recenter_marker(id):
    while True:
        count = 0
        markerlist = []
        for list in markerlists:
            if id in list:
                markerlist = list
        if id in markerlist:
            while(markerlist[markerlist.index(id) - 4] < .498 or markerlist[markerlist.index(id) - 4] > .502):
                for list in markerlists:
                 if id in list:
                    markerlist = list
                if(markerlist[markerlist.index(id) - 4] < .495 ):
                    halt()
                    right(0.1)
                    time.sleep(0.2)
                    print(markerlist)
                if(markerlist[markerlist.index(id) - 4] > .502):
                    halt()
                    left(0.1)
                    time.sleep(0.2)
                    print(markerlist)
            halt()
            # print(markerlist)
            return True
        else:
            print(f'I CANT SEE MARKER {id} SORRY, TRYING AGAIN')
            time.sleep(0.5)
            count = count + 1
            if(count > 5):
                ('COULD NOT FIND THE MARKER')
                return False
def rotate_recenter_marker(id):
    variance = 0
    if(id == 'heart'): # heart marker was slightly off from the object i was picking up
        variance = 0.075 # which is what this variance value was for, feel free to remove/ignore in alternate setups
    while True:
        count = 0
        markerlist = []
        for list in markerlists:
            if id in list:
                markerlist = list
        if id in markerlist:
            while(markerlist[markerlist.index(id) - 4] + variance < .498 or markerlist[markerlist.index(id) - 4] + variance > .502):
                for list in markerlists:
                 if id in list:
                    markerlist = list
                if(markerlist[markerlist.index(id) - 4] + variance > 0.5):
                    x = (markerlist[markerlist.index(id) - 4] + variance - 0.5) * 50 + 1
                else:
                    x = (0.5 - markerlist[markerlist.index(id) - 4] + variance) * 50 + 1
                if(markerlist[markerlist.index(id) - 4] + variance < .495 ):
                    rotate_left(x)
                    time.sleep(0.1)
                    # print(markerlist)
                if(markerlist[markerlist.index(id) - 4] + variance > .502):
                    rotate_right(x)
                    time.sleep(0.1)
                    # print(markerlist)
            halt()
            # print(markerlist)
            return True
        else:
            print(f'I CANT SEE MARKER {id} SORRY, TRYING AGAIN')
            time.sleep(0.5)
            count = count + 1
            if(count > 5):
                ('COULD NOT FIND THE MARKER')
                return False
            # if it cant find it 5+ times in a row it gives up
            # so make sure it sees the marker before running this function
def return_to_origin():

    while ((angle - 0.02 > 0) or (angle + 0.02 < 0)): # centering back on the power-on orientation
         x = (math.fabs(angle)) + 1
         if(angle > 0):
            rotate_left(x)
         else:
            rotate_right(x)
         time.sleep(0.1)
    halt()

    # above part is needed since the robot bases its xy coordinates on
    # the orientation that the robot was in when it was powered on, which varies

    while((position[0] - 0.04 > origin[0]) or (position[0] + 0.04 < origin[0])): # centering forward/backward to the position the robot started in
        x = 0.1 + (math.fabs(origin[0] - position[0]))
        if(position[0] < origin[0]):
            forward(x)
        else:
            backward(x)
        print(origin)
        print(position)
        time.sleep(0.1)
    halt()

    while((position[1] - 0.04 > origin[1]) or (position[1] + 0.04 < origin[1])): # centering right/left to the position the robot started in
        x = 0.1 + (math.fabs(origin[1] - position[1]))
        if(position[1] < origin[1]):
            right(x)
        else:
            left(x)
        print(origin)
        print(position)
        time.sleep(0.1)
    halt()

    # while ((angle - 0.02 > origin[2]) or (angle + 0.02 < origin[2])): # centering back on the original orientation that the robot started in
    #     x = 1 + (math.fabs(angle - origin[2]))
    #     if(angle > origin[2]):
    #         rotate_left(x)
    #     else:
    #         rotate_right(x)
    #     time.sleep(0.1)
    #     print(angle)
    # print(f"{origin[2] - angle} degrees from the origin, {origin} Origin, {position} Position")
    # halt()

    # this part above seems redundant, leaving it just in case it is needed later
    # all it is doing is putting it back to the startup angle
def grab_marker(id):
    ct = 0
    markerlist = []
    check = False
    while (check == False):
            time.sleep(1)
            for list in markerlists:
                if id in list:
                  check = True
                  markerlist = list
            rotate_right(25)
    rotate_recenter_marker(id)
    while(markerlist[3] < .17 and (id in markerlist)):
            seen = False
            for list in markerlists:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt()
    rotate_recenter_marker(id)
    while(markerlist[3] < .285 and (id in markerlist)):
            seen = False
            for list in markerlists:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt()
    robotic_arm_ctrl.moveto(175, -30)
    time.sleep(2)
    gripper_ctrl.close()
    time.sleep(2)
    robotic_arm_ctrl.moveto(150, 85)
    time.sleep(2)
    halt()
    return_to_origin()
def drop_marker(id):
    ct = 0
    check = False
    markerlist = []
    while (check == False):
            time.sleep(1)
            for list in markerlists:
                if id in list:
                  check = True
                  markerlist = list
            rotate_right(25)
    rotate_recenter_marker(id)
    while(markerlist[3] < .17 and (id in markerlist)):
            seen = False
            for list in markerlists:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt()
    rotate_recenter_marker(id)
    while(markerlist[3] < .285 and (id in markerlist)):
            seen = False
            for list in markerlists:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt()
    robotic_arm_ctrl.moveto(175, -30)
    time.sleep(2)
    gripper_ctrl.open()
    time.sleep(2)
    robotic_arm_ctrl.moveto(150, 85)
    time.sleep(2)
    halt()
    return_to_origin()
def dropzone_multi(id): # 0 is pickup, 1 is dropoff
    ct = 0
    check = False
    markerlist = []
    while (check == False):
            time.sleep(1)
            for list in markerlists:
                if 'heart' in list:
                  check = True
                  markerlist = list
            rotate_right(25)
    rotate_recenter_marker('heart')
    while(markerlist[3] < .242 and ('heart' in markerlist)):
            seen = False
            for list in markerlists:
                if 'heart' in list:
                    markerlist = list
                    ct = 0
                    seen = True
            forward(0.12)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
            print(markerlists)
    halt()
    robotic_arm_ctrl.moveto(175, -30)
    time.sleep(2)
    if id == 0:
        gripper_ctrl.close()
    else:
        gripper_ctrl.open()
    time.sleep(2)
    robotic_arm_ctrl.moveto(150, 85)
    time.sleep(2)
    halt()
    return_to_origin()

    # omitting all of the ct and seen code should cause minimal/no error
    # they were only there to troubleshoot

if __name__ == '__main__':
    # initializing the robot, setting better variable names
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")
    ep_chassis = ep_robot.chassis
    ep_vision = ep_robot.vision
    ep_sensor = ep_robot.sensor
    ep_camera = ep_robot.camera
    gripper_ctrl = ep_robot.gripper
    robotic_arm_ctrl = ep_robot.robotic_arm
    led_ctrl = ep_robot.led
    gripper_ctrl.open()
    time.sleep(1)
    robotic_arm_ctrl.moveto(150, 85) # this might give error depending on calibration
    time.sleep(1)
    # setting up sub data collection
    ep_sensor.sub_distance(freq=5, callback=sub_data_handler_d) # updating global distance value
    ep_chassis.sub_attitude(freq=5, callback=sub_data_handler_z) # updating angle value
    ep_chassis.sub_position(cs=0, freq=5, callback=sub_data_handler_p) # updating position(xy) values
    time.sleep(5)
    origin = [position[0], position[1], angle] # setting origin to position at start of program
    # turning video on
    ep_camera.start_video_stream(display=True)
    result = ep_vision.sub_detect_info(name="marker", callback=on_detect_marker)
    time.sleep(2)

    # actual code goes under here

    # code

    # remember 0.5m/s is a good value to minimize compounding error
    # remember 0 is pickup, 1 is dropoff for dropzone

    # shutting down the robot
    halt()
    ep_camera.stop_video_stream()
    result = ep_vision.unsub_detect_info(name="marker")
    ep_sensor.unsub_distance()
    ep_chassis.unsub_position()
    ep_chassis.unsub_attitude()
    ep_robot.close()
