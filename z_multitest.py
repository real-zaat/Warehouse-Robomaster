from multi_robomaster import multi_robot
import time

# this is an edited version of the multi-agent example, which can be found
# in the robomaster sdk examples folder

# ep_chassis.drive_speed(x=v,y=0,z=0)
def group_task(robot_group):
    robot_group.chassis.drive_speed(1,0,0)
    time.sleep(0.5)
    robot_group.chassis.drive_speed(0,0,0)

def group_task1(robot_group):
    robot_group.chassis.drive_speed(1,0,0)
    time.sleep(0.5)
    robot_group.chassis.drive_speed(0,0,0)



if __name__ == '__main__':
    #get robot sn by run the exmaples of /15_multi_robot/multi_ep/01_scan_robot_sn.py
    robots_sn_list = ['3JKCK7E0030C29', '3JKCK6U0030AB0']
    multi_robots = multi_robot.MultiEP()
    multi_robots.initialize()
    number = multi_robots.number_id_by_sn([0, robots_sn_list[0]], [1, robots_sn_list[1]])
    print("The number of robots is: {0}".format(number))
    robot_group = multi_robots.build_group([0,1])
    robot1 = robot_group.get_robot(0)
    robot2 = robot_group.get_robot(1)

    # robot1 = robot_group.get_robot(0)
    # robot1.chassis.drive_speed(x=1,y=0,z=0)
    # time.sleep(0.5)
    # robot1.chassis.drive_speed(x=0,y=0,z=0)
    # robot2 = robot_group.get_robot(1)
    # robot2.chassis.drive_speed(x=-1,y=0,z=0)
    # time.sleep(0.5)
    # robot2.chassis.drive_speed(x=0,y=0,z=0)
    print("Game over")
    print(robot_group)
    multi_robots.close()