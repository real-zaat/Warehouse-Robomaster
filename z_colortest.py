import time
from robomaster import robot
from robomaster import led

# this is an edited version of the color example, which can be found
# in the robomaster sdk examples folder

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_led = ep_robot.led

    # 设置灯效为常亮，亮度递增
    bright = 1
    for i in range(0, 8):
        ep_led.set_led(comp=led.COMP_ALL, r=25 << i, g=10 << i, b=1 << i, effect=led.EFFECT_ON)
        time.sleep(1)
        print("brightness: {0}".format(bright << i))

    ep_robot.close()

