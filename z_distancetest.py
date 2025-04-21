import robomaster
from robomaster import robot
import time


# this is an edited version of the distance example, which can be found
# in the robomaster sdk examples folder

dist = None
def sub_data_handler(sub_info):
    distance = sub_info
    print("tof1:{0}  tof2:{1}  tof3:{2}  tof4:{3}".format(distance[0], distance[1], distance[2], distance[3]))
    global dist
    dist = distance[0]
    # if dist > kjkj:
    #     # move
    # else:


    


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_sensor = ep_robot.sensor

    ep_sensor.sub_distance(freq=5, callback=sub_data_handler)
    time.sleep(0.5)
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{dist}|||||||||||||||||||||||||')
    time.sleep(600)
    ep_sensor.unsub_distance()
    ep_robot.close()