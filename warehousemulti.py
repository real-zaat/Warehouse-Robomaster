import robomaster
from robomaster import *
import cv2
import time
import threading
import math
from multi_robomaster import multi_robot
from datetime import datetime
import os

# this is the code for a multi-agent pickup/dropoff scenerio

# everything from new_defs.py is duplicated into 1,2 for easy compatability along with some additions
# it's kind of difficult to read / make changes, and there is definitely a better implementation, especially if more robots were introduced

ProgramFinished = False
position1 = [0,0]
position2 = [0,0]
angle1 = 0
angle2 = 0
dist1 = 999 #placeholder
dist2 = 999 #placeholder
origin1 = [0,0,0]
origin2 = [0,0,0]
markerlists1 = [[0,0,0,0,'0']]
markerlists2 = [[0,0,0,0,'0']]
markers1 = []
markers2 = []
multi = False
def forward(x, v):
    x.chassis.drive_speed(x=v,y=0,z=0)
def backward(x,v):
    x.chassis.drive_speed(x=-v,y=0,z=0)
def right(x,v):
    x.chassis.drive_speed(x=0,y=v,z=0)
def left(x,v):
    x.chassis.drive_speed(x=0,y=-v,z=0)
def rotate_right(x,v):
    x.chassis.drive_speed(x=0,y=0,z=v)
def rotate_left(x,v):
    x.chassis.drive_speed(x=0,y=0,z=-v)
def halt(x):
    x.chassis.drive_speed(x=0,y=0,z=0,timeout=None)
    time.sleep(0.25)
def sub_data_handler_d1(sub_info):
    distance = sub_info
    global dist1
    dist1 = distance[0]
def sub_data_handler_d2(sub_info):
    distance = sub_info
    global dist2
    dist2 = distance[0]
def sub_data_handler_p1(sub_info):
    global position1
    position1 = sub_info[:2]
def sub_data_handler_p2(sub_info):
    global position2
    position2 = sub_info[:2]
def sub_data_handler_z1(sub_info):
    global angle1
    angle1 = sub_info[0]
def sub_data_handler_z2(sub_info):
    global angle2
    angle2 = sub_info[0]
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
    @property
    def width(self):
        return self._w
def on_detect_marker1(marker_info):
    number = len(marker_info)
    global markerlists1
    markers1.clear()
    for i in range(0, number):
        x, y, w, h, info = marker_info[i]
        markers1.append(MarkerInfo(x, y, w, h, info))
        # print("marker:{0} x:{1}, y:{2}, w:{3}, h:{4}".format(info, x, y, w, h))

        markerlists1 = marker_info
        markerlists1 = marker_info + [[0,0,0,0,'0'], [0,0,0,0,'0'],[0,0,0,0,'0'],[0,0,0,0,'0']] # iteration placeholder
    if(len(markerlists1) == 0):
            markerlists1 = [[0,0,0,0,'0']] # iteration placeholder
def on_detect_marker2(marker_info):
    number = len(marker_info)
    global markerlists2
    markers2.clear()
    for i in range(0, number):
        x, y, w, h, info = marker_info[i]
        markers2.append(MarkerInfo(x, y, w, h, info))
        # print("marker:{0} x:{1}, y:{2}, w:{3}, h:{4}".format(info, x, y, w, h))
        markerlists2 = marker_info
        markerlists2 = marker_info + [[0,0,0,0,'0'],[0,0,0,0,'0'],[0,0,0,0,'0'],[0,0,0,0,'0']] # iteration placeholder
    if(len(markerlists2) == 0):
            markerlists2 = [[0,0,0,0,'0']] # iteration placeholder
def recenter_marker1(agent, id):
    while True:
        count = 0
        markerlist = []
        for list in markerlists1:
            if id in list:
                markerlist = list
        if id in markerlist:
            while(markerlist[markerlist.index(id) - 4] < .498 or markerlist[markerlist.index(id) - 4] > .502):
                for list in markerlists1:
                 if id in list:
                    markerlist = list
                if(markerlist[markerlist.index(id) - 4] < .495 ):
                    halt(agent)
                    right(agent, 0.1)
                    time.sleep(0.2)
                if(markerlist[markerlist.index(id) - 4] > .502):
                    halt(agent)
                    left(agent, 0.1)
                    time.sleep(0.2)
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
def recenter_marker2(agent, id):
    while True:
        count = 0
        markerlist = []
        for list in markerlists2:
            if id in list:
                markerlist = list
        if id in markerlist:
            while(markerlist[markerlist.index(id) - 4] < .498 or markerlist[markerlist.index(id) - 4] > .502):
                for list in markerlists2:
                 if id in list:
                    markerlist = list
                if(markerlist[markerlist.index(id) - 4] < .495 ):
                    halt(agent)
                    right(agent, 0.1)
                    time.sleep(0.2)
                if(markerlist[markerlist.index(id) - 4] > .502):
                    halt(agent)
                    left(agent, 0.1)
                    time.sleep(0.2)
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
def rotate_recenter_marker1(agent, id, z):
    variance = 0
    if(id == 'heart'):
        variance = .0875
        if(z == 1):
            variance = variance + 0.08
    while True:
        count = 0
        markerlist = []
        for list in markerlists1:
            if id in list:
                markerlist = list
        if id in markerlist:
            while(markerlist[markerlist.index(id) - 4] + variance < .498 or markerlist[markerlist.index(id) - 4] + variance > .502):
                for list in markerlists1:
                 if id in list:
                    markerlist = list
                if(markerlist[markerlist.index(id) - 4] + variance > 0.5):
                    x = (markerlist[markerlist.index(id) - 4] + variance - 0.5) * 50 + 1
                else:
                    x = (0.5 - markerlist[markerlist.index(id) - 4] + variance) * 50 + 1
                if(markerlist[markerlist.index(id) - 4] + variance < .495 ):
                    rotate_left(agent,x)
                    time.sleep(0.1)
                    # print(markerlist)
                if(markerlist[markerlist.index(id) - 4] + variance > .502):
                    rotate_right(agent,x)
                    time.sleep(0.1)
                    # print(markerlist)
            halt(agent)
            # print(markerlist)
            return True
        else:
            print(f'I CANT SEE MARKER {id} SORRY, TRYING AGAIN')
            time.sleep(0.5)
            count = count + 1
            if(count > 5):
                ('COULD NOT FIND THE MARKER')
                return False
def rotate_recenter_marker2(agent, id, z):
    variance = 0
    if(id == 'heart'):
        variance = 0.065
        if(z == 1):
            variance = variance + 0.1
    while True:
        count = 0
        markerlist = []
        for list in markerlists2:
            if id in list:
                markerlist = list
        if id in markerlist:
            while(markerlist[markerlist.index(id) - 4] + variance < .498 or markerlist[markerlist.index(id) - 4] + variance > .502):
                for list in markerlists2:
                 if id in list:
                    markerlist = list
                if(markerlist[markerlist.index(id) - 4] + variance > 0.5):
                    x = (markerlist[markerlist.index(id) - 4] + variance - 0.5) * 50 + 1
                else:
                    x = (0.5 - markerlist[markerlist.index(id) - 4] + variance) * 50 + 1
                if(markerlist[markerlist.index(id) - 4] + variance < .495 ):
                    rotate_left(agent,x)
                    time.sleep(0.1)
                    # print(markerlist)
                if(markerlist[markerlist.index(id) - 4] + variance > .502):
                    rotate_right(agent,x)
                    time.sleep(0.1)
                    # print(markerlist)
            halt(agent)
            # print(markerlist)
            return True
        else:
            print(f'I CANT SEE MARKER {id} SORRY, TRYING AGAIN')
            time.sleep(0.5)
            count = count + 1
            if(count > 5):
                ('COULD NOT FIND THE MARKER')
                return False
def return_to_origin1(agent):
    while ((angle1 - 0.02 > 0) or (angle1 + 0.02 < 0)): # centering back on the base orientation encoded in the robot to allow easier manuevering
         x = (math.fabs(angle1)) + 1
         if(angle1 > 0):
            rotate_left(agent, x)
         else:
            rotate_right(agent, x)
         time.sleep(0.1)
    halt(agent)
    while((position1[0] - 0.04 > origin1[0]) or (position1[0] + 0.04 < origin1[0])): # centering forward/backward to the position the robot started in
        x = 0.1 + (math.fabs(origin1[0] - position1[0]))
        if(position1[0] < origin1[0]):
            forward(agent, x)
        else:
            backward(agent, x)
        time.sleep(0.1)
    halt(agent)

    while((position1[1] - 0.04 > origin1[1]) or (position1[1] + 0.04 < origin1[1])): # centering right/left to the position the robot started in
        x = 0.1 + (math.fabs(origin1[1] - position1[1]))
        if(position1[1] < origin1[1]):
            right(agent,x)
        else:
            left(agent,x)
        time.sleep(0.1)
    halt(agent)

def return_to_origin2(agent):
    while ((angle2 - 0.02 > 0) or (angle2 + 0.02 < 0)): # centering back on the base orientation encoded in the robot to allow easier manuevering
         x = (math.fabs(angle2)) + 1
         if(angle2 > 0):
            rotate_left(agent, x)
         else:
            rotate_right(agent, x)
         time.sleep(0.1)
    halt(agent)
    while((position2[0] - 0.04 > origin2[0]) or (position2[0] + 0.04 < origin2[0])): # centering forward/backward to the position the robot started in
        x = 0.1 + (math.fabs(origin2[0] - position2[0]))
        if(position2[0] < origin2[0]):
            forward(agent, x)
        else:
            backward(agent, x)
        time.sleep(0.1)
    halt(agent)
    while((position2[1] - 0.04 > origin2[1]) or (position2[1] + 0.04 < origin2[1])): # centering right/left to the position the robot started in
        x = 0.1 + (math.fabs(origin2[1] - position2[1]))
        if(position2[1] < origin2[1]):
            right(agent,x)
        else:
            left(agent,x)
        time.sleep(0.1)
    halt(agent)

def grab_marker1(agent, id):
    ct = 0
    markerlist = []
    check = False
    while (check == False):
            time.sleep(1)
            for list in markerlists1:
                if id in list:
                  check = True
                  markerlist = list
            if(id == '3'):
                rotate_right(agent,25)
            else:
                rotate_left(agent,25)
    rotate_recenter_marker1(agent, id, 0)
    while(markerlist[3] < .17 and (id in markerlist)):
            seen = False
            for list in markerlists1:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(agent, 0.4)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt(agent)
    rotate_recenter_marker1(agent, id, 0)
    while(markerlist[3] < .285 and (id in markerlist)):
            seen = False
            for list in markerlists1:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(agent, 0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt(agent)
    agent.robotic_arm.moveto(175, -30)
    time.sleep(2)
    agent.gripper.close()
    time.sleep(2)
    agent.robotic_arm.moveto(150, 85)
    time.sleep(2)
    halt(agent)
    return_to_origin1(agent)

def grab_marker2(agent, id):
    ct = 0
    markerlist = []
    check = False
    while (check == False):
            time.sleep(1)
            for list in markerlists2:
                if id in list:
                  check = True
                  markerlist = list
            rotate_right(agent,25)
    rotate_recenter_marker2(agent, id, 0)
    while(markerlist[3] < .17 and (id in markerlist)):
            seen = False
            for list in markerlists2:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(agent, 0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt(agent)
    rotate_recenter_marker2(agent, id, 0)
    while(markerlist[3] < .32 and (id in markerlist)):
            seen = False
            for list in markerlists2:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(agent, 0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt(agent)
    agent.robotic_arm.moveto(175, -30)
    time.sleep(2)
    agent.gripper.close()
    time.sleep(2)
    agent.robotic_arm.moveto(150, 85)
    time.sleep(2)
    halt(agent)
    return_to_origin2(agent)

def drop_marker1(agent, id):
    ct = 0
    markerlist = []
    check = False
    while (check == False):
            time.sleep(1)
            for list in markerlists1:
                if id in list:
                  check = True
                  markerlist = list
            rotate_right(agent,25)
    rotate_recenter_marker1(agent, id, 0)
    while(markerlist[3] < .17 and (id in markerlist)):
            seen = False
            for list in markerlists1:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(agent, 0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt(agent)
    rotate_recenter_marker1(agent, id, 0)
    while(markerlist[3] < .32 and (id in markerlist)):
            seen = False
            for list in markerlists1:
                if id in list:
                    markerlist = list
                    seen = True
                    ct = 0
            forward(agent, 0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
    halt(agent)
    agent.robotic_arm.moveto(175, -30)
    time.sleep(2)
    agent.gripper.open()
    time.sleep(2)
    agent.robotic_arm.moveto(150, 85)
    time.sleep(2)
    halt(agent)
    return_to_origin1(agent)

def drop_marker2(agent, id):
    markerlist = []
    check = False
    while (check == False):
            time.sleep(1)
            for list in markerlists2:
                if id in list:
                  check = True
                  markerlist = list
            if(id =='1' or id == '2'):
                rotate_left(agent,25)
            else:
                rotate_right(agent,25)
    rotate_recenter_marker2(agent, id, 0)
    while(markerlist[3] < .17 and (id in markerlist)):
            for list in markerlists2:
                if id in list:
                    markerlist = list
            forward(agent, 0.15)
            time.sleep(0.1)
    halt(agent)
    rotate_recenter_marker2(agent, id, 0)
    while(markerlist[3] < .32 and (id in markerlist)):
            for list in markerlists2:
                if id in list:
                    markerlist = list
            forward(agent, 0.15)
            time.sleep(0.1)
    halt(agent)
    agent.robotic_arm.moveto(175, -30)
    time.sleep(2)
    agent.gripper.open()
    time.sleep(2)
    agent.robotic_arm.moveto(150, 85)
    time.sleep(2)
    halt(agent)
    return_to_origin2(agent)

def dropzone_multi1(agent, id): # 0 is pickup, 1 is dropoff
    ct = 0
    global multi
    check = False
    markerlist = []
    while (check == False):
            time.sleep(1)
            for list in markerlists1:
                if 'heart' in list:
                  check = True
                  markerlist = list
            rotate_right(agent, 25)
    rotate_recenter_marker1(agent,'heart', 0)
    while(markerlist[3] < .19 and ('heart' in markerlist)):
            seen = False
            for list in markerlists1:
                if 'heart' in list:
                    markerlist = list
                    ct = 0
                    seen = True
            forward(agent, 0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
            print(markerlists1)
    halt(agent)
    rotate_recenter_marker1(agent,'heart',1)
    while(markerlist[3] < .268 and ('heart' in markerlist)):
            seen = False
            for list in markerlists1:
                if 'heart' in list:
                    markerlist = list
                    ct = 0
                    seen = True
            forward(agent, 0.15)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
            print(markerlists1)
    halt(agent)
    agent.robotic_arm.moveto(175, -30)
    time.sleep(2)
    if id == 0:
        agent.gripper.close()
    else:
        agent.gripper.open()
    time.sleep(2)
    agent.robotic_arm.moveto(150, 85)
    time.sleep(2)
    halt(agent)
    multi = True
    return_to_origin1(agent)
    halt(agent)

def dropzone_multi2(agent, id): # 0 is pickup, 1 is dropoff
    ct = 0
    check = False
    markerlist = []
    while (check == False):
            time.sleep(1)
            for list in markerlists2:
                if 'heart' in list:
                  check = True
                  markerlist = list
            rotate_right(agent,25)
    rotate_recenter_marker2(agent,'heart', 0)
    while(markerlist[3] < .19 and ('heart' in markerlist)):
            seen = False
            for list in markerlists2:
                if 'heart' in list:
                    markerlist = list
                    ct = 0
                    seen = True
            forward(agent, 0.2)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
            print(markerlists2)
    halt(agent)
    rotate_recenter_marker2(agent,'heart', 1)
    WaitASecPlz()
    while(markerlist[3] < .239 and ('heart' in markerlist)):
            seen = False
            for list in markerlists2:
                if 'heart' in list:
                    markerlist = list
                    ct = 0
                    seen = True
            forward(agent, 0.12)
            time.sleep(0.1)
            if seen == False:
                ct = ct + 1
            if(ct > 8):
                markerlist = [0,0,0,0,'0']
            print(markerlists2)
    halt(agent)
    agent.robotic_arm.moveto(175, -30)
    time.sleep(2)
    if id == 0:
        agent.gripper.close()
    else:
        agent.gripper.open()
    time.sleep(2)
    agent.robotic_arm.moveto(150, 85)
    time.sleep(2)
    halt(agent)
    return_to_origin2(agent)
    halt(agent)

def WaitASecPlz(): # making sure the object is there for the second robot to pick it up
    global multi
    while multi == False:
        time.sleep(1)
    multi = False


def Agent1exec(robot_group):
    time.sleep(5)
    robot1 = robot_group.get_robot(0)
    grab_marker1(robot1, '1')
    dropzone_multi1(robot1, 1)
    grab_marker1(robot1, '3')
    dropzone_multi1(robot1, 1)
    grab_marker1(robot1, '2')
    dropzone_multi1(robot1, 1)
def Agent2exec(robot_group):
    global ProgramFinished
    time.sleep(5)
    robot2 = robot_group.get_robot(1)
    dropzone_multi2(robot2, 0)
    drop_marker2(robot2, '1')
    dropzone_multi2(robot2, 0)
    drop_marker2(robot2, '3')
    dropzone_multi2(robot2, 0)
    drop_marker2(robot2, '4') 
    ProgramFinished = True
    
def camera_task1(robot_group):
    global result1
    global result2
    # Get video stream for specific robot(1)
    robot = robot_group.get_robot(0)
    robot.camera.start_video_stream(display=False, resolution='720p') # resolution here
    result1 = robot.vision.sub_detect_info(name="marker", callback=on_detect_marker1)
    time.sleep(5)

    output_folder = "recordings"
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"robot1_{timestamp}.mp4")

    frame_size = (1280, 720)  # Should match your camera resolution
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID' for AVI
    out = cv2.VideoWriter(output_path, fourcc, 30.0, frame_size)

    while True:
     try:
        img = robot.camera.read_cv2_image(strategy = "newest", timeout = 0.1)
        if img is None:
            print("No frame received!")
            continue
        markers = markers1  
        for marker in markers:
            p1, p2 = marker.pt1, marker.pt2
            label = f"id: {marker.text}, width: {marker.width:.3f}"
            (label_w, label_h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

            cv2.rectangle(img, p1, p2, (0,0,220),2)
            cv2.rectangle(img, (p1[0],p1[1]-(label_h+baseline)), (p1[0]+label_w,p1[1]), (255,255,255),-1)
            cv2.rectangle(img, (p1[0],p1[1]-(label_h+baseline)), (p1[0]+label_w,p1[1]), (0,0,220),1)
            cv2.putText(img, label, (p1[0], p1[1] - baseline), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 220), 1)
        out.write(img)
        # Display the annotated image
        cv2.imshow(f'Robot {1} Markers', img)
        cv2.waitKey(1)
        if ProgramFinished:
            break
     except Exception as e:
            print(f"Robot 1 error: {type(e)}")
            continue   
    out.release()
    print(f"Robot 1 Video saved to: {os.path.abspath(output_path)}")  # Show full path
    time.sleep(3)
    cv2.destroyAllWindows()
    robot.camera.stop_video_stream()
    result1 = robot.vision.unsub_detect_info(name="marker")

def camera_task2(robot_group):
    global result2
    # Get video stream for specific robot(2)
    robot = robot_group.get_robot(1)
    robot.camera.start_video_stream(display=False, resolution='720p') # resolution here
    result2 = robot.vision.sub_detect_info(name="marker", callback=on_detect_marker2)
    time.sleep(5)

    output_folder = "recordings"
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"robot2_{timestamp}.mp4")

    frame_size = (1280, 720)  # Should match your camera resolution
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID' for AVI
    out = cv2.VideoWriter(output_path, fourcc, 30.0, frame_size)

    while True:
     try:
        img = robot.camera.read_cv2_image(strategy = "newest", timeout = 0.1)
        if img is None:
            print("No frame received!")
            continue
        markers = markers2
        
        for marker in markers:

            p1, p2 = marker.pt1, marker.pt2
            label = f"id: {marker.text}, width: {marker.width:.3f}"
            (label_w, label_h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

            cv2.rectangle(img, p1, p2, (196,200,0),2)
            cv2.rectangle(img, (p1[0],p1[1]-(label_h+baseline)), (p1[0]+label_w,p1[1]), (255,255,255),-1)
            cv2.rectangle(img, (p1[0],p1[1]-(label_h+baseline)), (p1[0]+label_w,p1[1]), (196,200,0),1)
            cv2.putText(img, label, (p1[0], p1[1] - baseline), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (196, 200, 0), 1)
        out.write(img)
        # Display the annotated image
        cv2.imshow(f'Robot {2} Markers', img)
        cv2.waitKey(1)
        if ProgramFinished:
            break
     except Exception as e:
            print(f"Robot 2 error: {type(e)}")
            continue
    out.release()
    print(f"Robot 2 Video saved to: {os.path.abspath(output_path)}")  # Show full path
    time.sleep(3)
    cv2.destroyAllWindows()
    robot.camera.stop_video_stream()
    result2 = robot2.vision.unsub_detect_info(name="marker")


if __name__ == '__main__':
    # get robot sn by running the exmaples of /15_multi_robot/multi_ep/01_scan_robot_sn.py
    robots_sn_list = ['3JKCK7E0030C29', '3JKCK6U0030AB0']
    multi_robots = multi_robot.MultiEP()
    multi_robots.initialize()
    number = multi_robots.number_id_by_sn([0, robots_sn_list[0]], [1, robots_sn_list[1]])
    robot_group1 = multi_robots.build_group([0])
    robot_group2 = multi_robots.build_group([1])
    robot1 = robot_group1.get_robot(0)
    robot2 = robot_group2.get_robot(1)
    print(robot_group1.robots_id_list)
    print(robot_group2.robots_id_list)
    # putting arm in a hopefully normal(?) spot
    # make sure to calibrate arm and wheels in robomaster app before using the sdk
    robot1.gripper.open()
    robot2.gripper.open()
    time.sleep(0.5)
    robot1.robotic_arm.moveto(150, 85)
    robot2.robotic_arm.moveto(150, 85) # 150 85
    time.sleep(0.5)

    # setting up data collection for both robots
    robot1.sensor.sub_distance(freq=5, callback=sub_data_handler_d1)
    robot1.chassis.sub_attitude(freq=5, callback=sub_data_handler_z1)
    robot1.chassis.sub_position(cs=0, freq=5, callback=sub_data_handler_p1)
    robot2.sensor.sub_distance(freq=5, callback=sub_data_handler_d2)
    robot2.chassis.sub_attitude(freq=5, callback=sub_data_handler_z2)
    robot2.chassis.sub_position(cs=0, freq=5, callback=sub_data_handler_p2)
    time.sleep(2)
    origin1 = [position1[0], position1[1], angle1]
    origin2 = [position2[0], position2[1], angle2]

    # task to complete here
    # multi_robots.run([], [] ....) is an easy way to multithread with this package
    # however, it requires a certain syntax. Check the multi sdk documentation for info

    multi_robots.run([robot_group1, camera_task1], [robot_group2, camera_task2],
                     [robot_group1, Agent1exec], [robot_group2, Agent2exec])

    # multi_robots.run([robot_group1, camera_task1], [robot_group2, camera_task2])

    # shutdown
    halt(robot1)
    halt(robot2)
    robot1.sensor.unsub_distance()
    robot1.chassis.unsub_position()
    robot1.chassis.unsub_attitude()
    robot2.sensor.unsub_distance()
    robot2.chassis.unsub_position()
    robot2.chassis.unsub_attitude()
    robot1.close()
    robot2.close()