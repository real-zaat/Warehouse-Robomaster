import time
import robomaster
from robomaster import robot

# this is an edited version of the arm example, which can be found
# in the robomaster sdk examples folder

# if __name__ == '__main__':
#     ep_robot = robot.Robot()
#     ep_robot.initialize(conn_type="sta")

#     ep_gripper = ep_robot.gripper

#     ep_gripper.open(power=50)
#     time.sleep(1)
#     ep_gripper.pause()

#     ep_gripper.close(power=50)
#     time.sleep(1)
#     ep_gripper.pause()

#     ep_robot.close()

import robomaster
from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_arm = ep_robot.robotic_arm

    # 向前移动20毫米
    ep_arm.move(x=20, y=0).wait_for_completed()
    # 向后移动20毫米
    ep_arm.move(x=-20, y=0).wait_for_completed()
    # 向上移动20毫米
    ep_arm.move(x=0, y=20).wait_for_completed()
    # 向下移动20毫米
    ep_arm.move(x=0, y=-20).wait_for_completed()

    ep_arm.recenter()

    ep_robot.close()