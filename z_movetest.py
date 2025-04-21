from robomaster import robot
import time

# this is an edited version of the chassis move example, which can be found
# in the robomaster sdk examples folder

#note the forward/backward/right/left values may be different due to miscalibration

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_chassis = ep_robot.chassis

    x_val = 0.5
    y_val = 0.6
    z_val = 90

    # 前进 0.5米
    # ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()
    # ep_chassis.drive_speed(x=0,y=1,z=0) # RIGHT
    # ep_chassis.drive_speed(x=0,y=-1,z=0) # LEFT
    # ep_chassis.drive_speed(x=1,y=0,z=0) # FORWARD
    # ep_chassis.drive_speed(x=1,y=0,z=0, timeout=None) # BACKWARD
    ep_chassis.drive_speed(x=-1,y=0,z=0, timeout=None)
    time.sleep(0.5)
    ep_chassis.drive_speed(x=0,y=0,z=0,timeout=None)
    #ep_chassis.drive_wheels(0, 0, 0, 0)
    time.sleep(0.2)
    ep_robot.close()
