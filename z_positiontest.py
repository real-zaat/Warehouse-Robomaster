import robomaster
from robomaster import robot
import time

# this is an edited version of the position example, which can be found
# in the robomaster sdk examples folder

angle = None
position = None
def sub_data_handlerp(sub_info):
    print("x:{0}  y:{1}".format(sub_info[0], sub_info[1], sub_info[2]))
    global position
    position = sub_info[:2]

def sub_data_handlerz(sub_info):
    print("yaw:{0}  pitch:{1}, roll{2}".format(sub_info[0], sub_info[1], sub_info[2]))
    global angle
    angle = sub_info[0]


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_chassis = ep_robot.chassis
    ep_chassis.sub_attitude(freq=50, callback=sub_data_handlerz)
    ep_chassis.sub_position(cs=0, freq=50, callback=sub_data_handlerp)
    time.sleep(5)

    ep_chassis.drive_speed(x=-1,y=0,z=0)
    time.sleep(1)
    ep_chassis.drive_speed(x=0,y=0,z=0)
    time.sleep(2)
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{angle}|||||||||||||||||||||||||')
    time.sleep(50)
    ep_chassis.unsub_position()
    ep_robot.close()