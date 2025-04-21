from robomaster import *
# THIS CODE DOES NOT WORK!!
# this is an example of what the code looks like in the app when converting block --> python code
# it is very inefficient, I reccomend only using block code to get a grasp of basics
# then use the SDK for more complicated instructions, and projects
variable_distance = 0
variable_marker1check = 0
variable_marker1seen = 0
variable_arm_pos = 0
variable_mark2xvalue = 0
variable_avg = 0
variable_gauge1 = 0
variable_gauge2 = 0
variable_wallrecursion_ct = 0
variable_exit = 0
variable_center_xvar = 0
variable_accum_distance = 0
variable_orientation = 0
variable_orientationvariation = 0
variable_overflow = 0
variable_dropcount = 0
variable_drop_direction = 0
list_MarkerList = RmList()
list_SightList = RmList()
list_arm_pos = RmList()
def user_defined_dropobject1():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one)):
        chassis_ctrl.move_degree_with_speed(0.1,-90)
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(12):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 11:
        variable_mark2xvalue = list_MarkerList[3]
    if list_MarkerList[7] == 11:
        variable_mark2xvalue = list_MarkerList[8]
    if list_MarkerList[12] == 11:
        variable_mark2xvalue = list_MarkerList[13]
    if list_MarkerList[17] == 11:
        variable_mark2xvalue = list_MarkerList[18]
    if list_MarkerList[22] == 11:
        variable_mark2xvalue = list_MarkerList[23]
    user_defined_centeron1_slide()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(12):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 11:
        variable_mark2xvalue = list_MarkerList[6]
    if list_MarkerList[7] == 11:
        variable_mark2xvalue = list_MarkerList[11]
    if list_MarkerList[12] == 11:
        variable_mark2xvalue = list_MarkerList[16]
    if list_MarkerList[17] == 11:
        variable_mark2xvalue = list_MarkerList[21]
    if list_MarkerList[22] == 11:
        variable_mark2xvalue = list_MarkerList[26]
    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one)) or 0.35 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(12):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 11:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 11:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 11:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 11:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 11:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_release_can()

def user_defined_drop_heart_circle():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_red_heart)):
        if variable_drop_direction == 0:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,4)
        else:
            chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,4)
    variable_mark2xvalue = 0
    user_defined_center_heart()

    variable_mark2xvalue = 0
    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_red_heart)) or 0.2 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 8:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 8:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 8:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 8:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 8:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_center_heart()

    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_red_heart)) or 0.35 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 8:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 8:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 8:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 8:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 8:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_release_can()

    time.sleep(2)
    user_defined_generic_centerslide()

    user_defined_reorient()

    user_defined_generic_centerslide()

    if variable_avg != 0:
        chassis_ctrl.set_trans_speed(0.5)
        chassis_ctrl.move_with_distance(-180,(110 - 0) / 100)
    else:
        chassis_ctrl.move_with_time(180,1.2)
    time.sleep(2)
def user_defined_dropobject_heart():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while not ((vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_red_heart)) and variable_mark2xvalue > 0.47 and 0.53 > variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 8:
            variable_mark2xvalue = list_MarkerList[3]
        if list_MarkerList[7] == 8:
            variable_mark2xvalue = list_MarkerList[8]
        if list_MarkerList[12] == 8:
            variable_mark2xvalue = list_MarkerList[13]
        if list_MarkerList[17] == 8:
            variable_mark2xvalue = list_MarkerList[18]
        if list_MarkerList[22] == 8:
            variable_mark2xvalue = list_MarkerList[23]
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,10)
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 8:
        variable_mark2xvalue = list_MarkerList[3]
    if list_MarkerList[7] == 8:
        variable_mark2xvalue = list_MarkerList[8]
    if list_MarkerList[12] == 8:
        variable_mark2xvalue = list_MarkerList[13]
    if list_MarkerList[17] == 8:
        variable_mark2xvalue = list_MarkerList[18]
    if list_MarkerList[22] == 8:
        variable_mark2xvalue = list_MarkerList[23]
    user_defined_centerheart_slide()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 8:
        variable_mark2xvalue = list_MarkerList[6]
    if list_MarkerList[7] == 8:
        variable_mark2xvalue = list_MarkerList[11]
    if list_MarkerList[12] == 8:
        variable_mark2xvalue = list_MarkerList[16]
    if list_MarkerList[17] == 8:
        variable_mark2xvalue = list_MarkerList[21]
    if list_MarkerList[22] == 8:
        variable_mark2xvalue = list_MarkerList[26]
    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_red_heart)) or 0.35 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 8:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 8:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 8:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 8:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 8:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_release_can()

def user_defined_reorient():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 11:
        variable_orientationvariation = 0
    if list_MarkerList[2] == 8:
        variable_orientationvariation = 42
    if list_MarkerList[2] == 12:
        variable_orientationvariation = 86
    if list_MarkerList[2] == 13:
        variable_orientationvariation = 180
        variable_overflow = 1
    if list_MarkerList[2] == 14:
        variable_orientationvariation = -92
    while not variable_exit == 1:
        if variable_overflow == 0:
            variable_orientation = 0 + chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate)
            if -0.01 + variable_orientationvariation < chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate) and chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate) < 0.01 + variable_orientationvariation:
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
                variable_exit = 1
            if chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate) > -0.01 + variable_orientationvariation:
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,1)
                time.sleep(0.1)
            else:
                if 0.01 + variable_orientationvariation > chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate):
                    chassis_ctrl.rotate_with_speed(rm_define.clockwise,1)
                    time.sleep(0.1)
        else:
            variable_exit = 1
            variable_orientation = abs(0 + chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate))
            if abs(chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate)) < 0.01 + variable_orientationvariation and -0.01 + variable_orientationvariation < abs(chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate)):
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
                variable_exit = 1
            if 179.9 > abs(chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate)) and 0 < chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate):
                chassis_ctrl.rotate_with_speed(rm_define.clockwise,1)
                time.sleep(0.1)
            else:
                if 179.9 > abs(chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate)) and chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate) < 0:
                    chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,1)
                    time.sleep(0.1)
                else:
                    pass
    variable_exit = 0
    variable_overflow = 0
def user_defined_generic_centerslide():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        variable_center_xvar = list_MarkerList[3]
        if 49.75 < 100 * variable_center_xvar:
            chassis_ctrl.move(90)
        else:
            if 100 * variable_center_xvar < 50.25:
                chassis_ctrl.move(-90)
        if 49.75 < 100 * variable_center_xvar and 100 * variable_center_xvar < 50.25:
            variable_exit = 1
def user_defined_centerheart_slide():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 8:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 8:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 8:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 8:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 8:
            variable_center_xvar = list_MarkerList[23]
        if 49.75 < 100 * variable_center_xvar and 100 * variable_center_xvar < 50.25:
            variable_exit = 1
        if 49.75 < 100 * variable_center_xvar:
            chassis_ctrl.move(90)
        else:
            if 100 * variable_center_xvar < 50.25:
                chassis_ctrl.move(-90)
def user_defined_centeron5_slide():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 15:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 15:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 15:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 15:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 15:
            variable_center_xvar = list_MarkerList[23]
        if 49.75 < 100 * variable_center_xvar and 100 * variable_center_xvar < 50.25:
            variable_exit = 1
        if 49.75 < 100 * variable_center_xvar:
            chassis_ctrl.move(90)
        else:
            if 100 * variable_center_xvar < 50.25:
                chassis_ctrl.move(-90)
def user_defined_grab3():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_drop_direction = 1
    user_defined_startup_condition()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    user_defined_center_marker3()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_45")):
        chassis_ctrl.move_degree_with_speed(0.2,0)
    chassis_ctrl.stop()
    user_defined_center_marker3()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_18")):
        chassis_ctrl.move_degree_with_speed(0.1,0)
    chassis_ctrl.stop()
    user_defined_grab_can()

    if ir_distance_sensor_ctrl.get_distance_info(1) < 15:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(2)
    else:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(2)
        rmexit()
def user_defined_grab5():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    user_defined_startup_condition()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    user_defined_center_marker5()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_45")):
        chassis_ctrl.move_degree_with_speed(0.2,0)
    chassis_ctrl.stop()
    user_defined_center_marker5()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_18")):
        chassis_ctrl.move_degree_with_speed(0.1,0)
    chassis_ctrl.stop()
    user_defined_grab_can()

    if ir_distance_sensor_ctrl.get_distance_info(1) < 15:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(2)
    else:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(2)
        rmexit()
def user_defined_centeron2_slide():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 12:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 12:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 12:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 12:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 12:
            variable_center_xvar = list_MarkerList[23]
        if 49.75 < 100 * variable_center_xvar and 100 * variable_center_xvar < 50.25:
            variable_exit = 1
        if 49.75 < 100 * variable_center_xvar:
            chassis_ctrl.move(90)
        else:
            if 100 * variable_center_xvar < 50.25:
                chassis_ctrl.move(-90)
def user_defined_centeron4_slide():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 14:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 14:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 14:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 14:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 14:
            variable_center_xvar = list_MarkerList[23]
        if 49.75 < 100 * variable_center_xvar and 100 * variable_center_xvar < 50.25:
            variable_exit = 1
        if 49.75 < 100 * variable_center_xvar:
            chassis_ctrl.move(90)
        else:
            if 100 * variable_center_xvar < 50.25:
                chassis_ctrl.move(-90)
def user_defined_centeron1_slide():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 11:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 11:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 11:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 11:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 11:
            variable_center_xvar = list_MarkerList[23]
        if 49.75 < 100 * variable_center_xvar and 100 * variable_center_xvar < 50.25:
            variable_exit = 1
        if 49.75 < 100 * variable_center_xvar:
            chassis_ctrl.move(90)
        else:
            if 100 * variable_center_xvar < 50.25:
                chassis_ctrl.move(-90)
def user_defined_centeron3_slide():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 13:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 13:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 13:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 13:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 13:
            variable_center_xvar = list_MarkerList[23]
        if 49.75 < 100 * variable_center_xvar and 100 * variable_center_xvar < 50.25:
            variable_exit = 1
        if 49.75 < 100 * variable_center_xvar:
            chassis_ctrl.move(90)
        else:
            if 100 * variable_center_xvar < 50.25:
                chassis_ctrl.move(-90)
def user_defined_dropobject3():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three)):
        chassis_ctrl.move_degree_with_speed(0.1,90)
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 13:
        variable_mark2xvalue = list_MarkerList[3]
    if list_MarkerList[7] == 13:
        variable_mark2xvalue = list_MarkerList[8]
    if list_MarkerList[12] == 13:
        variable_mark2xvalue = list_MarkerList[13]
    if list_MarkerList[17] == 13:
        variable_mark2xvalue = list_MarkerList[18]
    if list_MarkerList[22] == 26:
        variable_mark2xvalue = list_MarkerList[23]
    user_defined_centeron3_slide()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 13:
        variable_mark2xvalue = list_MarkerList[6]
    if list_MarkerList[7] == 13:
        variable_mark2xvalue = list_MarkerList[11]
    if list_MarkerList[12] == 13:
        variable_mark2xvalue = list_MarkerList[16]
    if list_MarkerList[17] == 13:
        variable_mark2xvalue = list_MarkerList[21]
    if list_MarkerList[22] == 13:
        variable_mark2xvalue = list_MarkerList[26]
    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three)) or 0.35 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 13:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 13:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 13:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 13:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 13:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_release_can()

def user_defined_wall_markercenter():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_exit = 0
    chassis_ctrl.set_trans_speed(0.1)
    while not variable_exit == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        if 49.75 < 100 * list_MarkerList[3] and 100 * list_MarkerList[3] < 50.25:
            variable_exit = 1
        if 49.75 < 100 * list_MarkerList[3]:
            chassis_ctrl.move(90)
        else:
            if 100 * list_MarkerList[3] < 50.25:
                chassis_ctrl.move(-90)
def user_defined_grab2():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_drop_direction = 1
    user_defined_startup_condition()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    user_defined_center_marker2()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_45")):
        chassis_ctrl.move_degree_with_speed(0.2,0)
    chassis_ctrl.stop()
    user_defined_center_marker2()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_18")):
        chassis_ctrl.move_degree_with_speed(0.1,0)
    chassis_ctrl.stop()
    user_defined_grab_can()

    if ir_distance_sensor_ctrl.get_distance_info(1) < 15:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(2)
    else:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(2)
        rmexit()
def user_defined_grab4():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_drop_direction = 0
    user_defined_startup_condition()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    user_defined_center_marker4()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_45")):
        chassis_ctrl.move_degree_with_speed(0.2,0)
    chassis_ctrl.stop()
    user_defined_center_marker4()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_18")):
        chassis_ctrl.move_degree_with_speed(0.1,0)
    chassis_ctrl.stop()
    user_defined_grab_can()

    if ir_distance_sensor_ctrl.get_distance_info(1) < 15:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(2)
    else:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(2)
        rmexit()
def user_defined_wall_locknest():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    if not 4 <= variable_wallrecursion_ct:
        chassis_ctrl.set_rotate_speed(6 - 1 * variable_wallrecursion_ct)
        user_defined_distance_avg()

        variable_gauge1 = variable_avg
        chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.1)
        user_defined_distance_avg()

        variable_gauge2 = variable_avg
        chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.1)
        if variable_gauge1 < variable_gauge2:
            variable_gauge1 = 0
            variable_gauge2 = 0
            while not variable_gauge2 < variable_gauge1:
                user_defined_distance_avg()

                variable_gauge2 = variable_avg
                chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.3)
                user_defined_distance_avg()

                variable_gauge1 = variable_avg
                time.sleep(0.01)
            chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.3)
        else:
            variable_gauge1 = 0
            variable_gauge2 = 0
            while not variable_gauge1 < variable_gauge2:
                user_defined_distance_avg()

                variable_gauge1 = variable_avg
                chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.3)
                user_defined_distance_avg()

                variable_gauge2 = variable_avg
                time.sleep(0.01)
            chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.3)
        variable_wallrecursion_ct = variable_wallrecursion_ct + 1
        user_defined_wall_locknest()

def user_defined_dropobject5():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_five)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 15:
        variable_mark2xvalue = list_MarkerList[3]
    if list_MarkerList[7] == 15:
        variable_mark2xvalue = list_MarkerList[8]
    if list_MarkerList[12] == 15:
        variable_mark2xvalue = list_MarkerList[13]
    if list_MarkerList[17] == 15:
        variable_mark2xvalue = list_MarkerList[18]
    if list_MarkerList[22] == 15:
        variable_mark2xvalue = list_MarkerList[23]
    user_defined_centeron5_slide()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 15:
        variable_mark2xvalue = list_MarkerList[6]
    if list_MarkerList[7] == 15:
        variable_mark2xvalue = list_MarkerList[11]
    if list_MarkerList[12] == 15:
        variable_mark2xvalue = list_MarkerList[16]
    if list_MarkerList[17] == 15:
        variable_mark2xvalue = list_MarkerList[21]
    if list_MarkerList[22] == 15:
        variable_mark2xvalue = list_MarkerList[26]
    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_five)) or 0.35 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 15:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 15:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 15:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 15:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 15:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_release_can()

def user_defined_dropobject4():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 14:
        variable_mark2xvalue = list_MarkerList[3]
    if list_MarkerList[7] == 14:
        variable_mark2xvalue = list_MarkerList[8]
    if list_MarkerList[12] == 14:
        variable_mark2xvalue = list_MarkerList[13]
    if list_MarkerList[17] == 14:
        variable_mark2xvalue = list_MarkerList[18]
    if list_MarkerList[22] == 14:
        variable_mark2xvalue = list_MarkerList[23]
    user_defined_centeron4_slide()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 14:
        variable_mark2xvalue = list_MarkerList[6]
    if list_MarkerList[7] == 14:
        variable_mark2xvalue = list_MarkerList[11]
    if list_MarkerList[12] == 14:
        variable_mark2xvalue = list_MarkerList[16]
    if list_MarkerList[17] == 14:
        variable_mark2xvalue = list_MarkerList[21]
    if list_MarkerList[22] == 14:
        variable_mark2xvalue = list_MarkerList[26]
    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four)) or 0.35 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 14:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 14:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 14:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 14:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 14:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_release_can()

def user_defined_dropobject2():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 12:
        variable_mark2xvalue = list_MarkerList[3]
    if list_MarkerList[7] == 12:
        variable_mark2xvalue = list_MarkerList[8]
    if list_MarkerList[12] == 12:
        variable_mark2xvalue = list_MarkerList[13]
    if list_MarkerList[17] == 12:
        variable_mark2xvalue = list_MarkerList[18]
    if list_MarkerList[22] == 12:
        variable_mark2xvalue = list_MarkerList[23]
    user_defined_centeron2_slide()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    for count in range(22):
        list_MarkerList.append(0)
    if list_MarkerList[2] == 12:
        variable_mark2xvalue = list_MarkerList[6]
    if list_MarkerList[7] == 12:
        variable_mark2xvalue = list_MarkerList[11]
    if list_MarkerList[12] == 12:
        variable_mark2xvalue = list_MarkerList[16]
    if list_MarkerList[17] == 12:
        variable_mark2xvalue = list_MarkerList[21]
    if list_MarkerList[22] == 12:
        variable_mark2xvalue = list_MarkerList[26]
    while not (not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two)) or 0.35 < variable_mark2xvalue):
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(22):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 12:
            variable_mark2xvalue = list_MarkerList[6]
        if list_MarkerList[7] == 12:
            variable_mark2xvalue = list_MarkerList[11]
        if list_MarkerList[12] == 12:
            variable_mark2xvalue = list_MarkerList[16]
        if list_MarkerList[17] == 12:
            variable_mark2xvalue = list_MarkerList[21]
        if list_MarkerList[22] == 12:
            variable_mark2xvalue = list_MarkerList[26]
        chassis_ctrl.move_degree_with_speed(0.1,0)
    user_defined_release_can()

def user_defined_wall_lock():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_wallrecursion_ct = 0
    chassis_ctrl.set_rotate_speed(5)
    user_defined_distance_avg()

    variable_gauge1 = variable_avg
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.3)
    user_defined_distance_avg()

    variable_gauge1 = variable_avg
    chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.3)
    user_defined_wall_locknest()

def user_defined_distance_avg():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_avg = 0
    for count in range(10):
        variable_avg = variable_avg + ir_distance_sensor_ctrl.get_distance_info(1)
        time.sleep(0.1)
    variable_avg = variable_avg / 10
def user_defined_center2():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_marker1check = 0
    variable_marker1seen = 0
    while not variable_marker1check == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(20):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 12:
            variable_mark2xvalue = list_MarkerList[3]
        if list_MarkerList[7] == 12:
            variable_mark2xvalue = list_MarkerList[8]
        if list_MarkerList[12] == 12:
            variable_mark2xvalue = list_MarkerList[13]
        if 0.49 < variable_mark2xvalue and variable_mark2xvalue < 0.51:
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
            variable_marker1seen = 1
            variable_marker1check = variable_marker1check + 1
        if variable_mark2xvalue > 0.49:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,5)
            variable_marker1seen = 1
            time.sleep(0.1)
        else:
            if 0.51 > variable_mark2xvalue:
                variable_marker1seen = 1
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,5)
                time.sleep(0.1)
        if list_MarkerList[1] == 0:
            rmexit()
        variable_mark2xvalue = 0
def user_defined_grab1():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_drop_direction = 0
    user_defined_startup_condition()

    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    user_defined_center_marker1()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_45")):
        chassis_ctrl.move_degree_with_speed(0.2,0)
    chassis_ctrl.stop()
    user_defined_center_marker1()

    while not (ir_distance_sensor_ctrl.check_condition("ir_distance_1_le_16")):
        chassis_ctrl.move_degree_with_speed(0.1,0)
    chassis_ctrl.stop()
    user_defined_grab_can()

    if ir_distance_sensor_ctrl.get_distance_info(1) < 15:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(2)
    else:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(2)
        rmexit()
def user_defined_sampledatatest():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    while True:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        list_SightList=RmList(media_ctrl.get_sight_bead_position())
        variable_distance = ir_distance_sensor_ctrl.get_distance_info(1)
        variable_orientation = chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate)
def user_defined_startup_condition():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    vision_ctrl.set_marker_detection_distance(3)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    media_ctrl.exposure_value_update(rm_define.exposure_value_large)
    gripper_ctrl.open()
    robotic_arm_ctrl.moveto(160, 80, wait_for_complete=True)
    ir_distance_sensor_ctrl.enable_measure(1)
    variable_orientation = chassis_ctrl.get_position_based_power_on(rm_define.chassis_rotate)
    variable_distance = 0
    time.sleep(2)
def user_defined_grab_can():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    chassis_ctrl.stop()
    list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    robotic_arm_ctrl.moveto(160, -30, wait_for_complete=True)
    time.sleep(2)
    robotic_arm_ctrl.moveto(175, -30, wait_for_complete=True)
    list_arm_pos=RmList(robotic_arm_ctrl.get_position())
    time.sleep(2)
    gripper_ctrl.close()
    time.sleep(2)
    robotic_arm_ctrl.moveto(160, 80, wait_for_complete=True)
    time.sleep(2)
    user_defined_reorient()

    user_defined_generic_centerslide()

    if variable_avg != 0:
        chassis_ctrl.set_trans_speed(0.5)
        chassis_ctrl.move_with_distance(-180,(variable_avg - 26) / 100)
    else:
        chassis_ctrl.move_with_time(180,1.2)
    time.sleep(2)
def user_defined_center_heart():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_marker1check = 0
    variable_marker1seen = 0
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_red_heart)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    while not variable_marker1check == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(25):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 8:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 8:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 8:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 8:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 8:
            variable_center_xvar = list_MarkerList[23]
        if 0.49 < variable_center_xvar and variable_center_xvar < 0.51:
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
            variable_marker1seen = 1
            variable_marker1check = variable_marker1check + 1
        if variable_center_xvar > 0.49:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,3)
            variable_marker1seen = 1
            time.sleep(0.1)
        else:
            if 0.51 > variable_center_xvar:
                variable_marker1seen = 1
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,3)
                time.sleep(0.1)
        if list_MarkerList[1] == 0:
            rmexit()
def user_defined_center_marker4():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_marker1check = 0
    variable_marker1seen = 0
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    while not variable_marker1check == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(25):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 14:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 14:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 14:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 14:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 14:
            variable_center_xvar = list_MarkerList[23]
        if 0.49 < variable_center_xvar and variable_center_xvar < 0.51:
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
            variable_marker1seen = 1
            variable_marker1check = variable_marker1check + 1
        if variable_center_xvar > 0.49:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,3)
            variable_marker1seen = 1
            time.sleep(0.1)
        else:
            if 0.51 > variable_center_xvar:
                variable_marker1seen = 1
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,3)
                time.sleep(0.1)
        if list_MarkerList[1] == 0:
            rmexit()
def user_defined_center_marker2():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_marker1check = 0
    variable_marker1seen = 0
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    while not variable_marker1check == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(25):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 12:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 12:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 12:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 12:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 12:
            variable_center_xvar = list_MarkerList[23]
        if 0.49 < variable_center_xvar and variable_center_xvar < 0.51:
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
            variable_marker1seen = 1
            variable_marker1check = variable_marker1check + 1
        if variable_center_xvar > 0.49:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,3)
            variable_marker1seen = 1
            time.sleep(0.1)
        else:
            if 0.51 > variable_center_xvar:
                variable_marker1seen = 1
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,3)
                time.sleep(0.1)
        if list_MarkerList[1] == 0:
            rmexit()
def user_defined_center_marker1():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_marker1check = 0
    variable_marker1seen = 0
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    while not variable_marker1check == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(25):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 11:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 11:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 11:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 11:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 11:
            variable_center_xvar = list_MarkerList[23]
        if 0.49 < variable_center_xvar and variable_center_xvar < 0.51:
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
            variable_marker1seen = 1
            variable_marker1check = variable_marker1check + 1
        if variable_center_xvar > 0.49:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,3)
            variable_marker1seen = 1
            time.sleep(0.1)
        else:
            if 0.51 > variable_center_xvar:
                variable_marker1seen = 1
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,3)
                time.sleep(0.1)
        if list_MarkerList[1] == 0:
            rmexit()
def user_defined_center_marker5():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_marker1check = 0
    variable_marker1seen = 0
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_five)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    while not variable_marker1check == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(20):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 15:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 15:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 15:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 15:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 15:
            variable_center_xvar = list_MarkerList[23]
        if 0.49 < variable_center_xvar and variable_center_xvar < 0.51:
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
            variable_marker1seen = 1
            variable_marker1check = variable_marker1check + 1
        if variable_center_xvar > 0.49:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,3)
            variable_marker1seen = 1
            time.sleep(0.1)
        else:
            if 0.51 > variable_center_xvar:
                variable_marker1seen = 1
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,3)
                time.sleep(0.1)
        if list_MarkerList[1] == 0:
            rmexit()
def user_defined_center_marker3():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    variable_marker1check = 0
    variable_marker1seen = 0
    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,15)
    while not variable_marker1check == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        for count in range(25):
            list_MarkerList.append(0)
        if list_MarkerList[2] == 13:
            variable_center_xvar = list_MarkerList[3]
        if list_MarkerList[7] == 13:
            variable_center_xvar = list_MarkerList[8]
        if list_MarkerList[12] == 13:
            variable_center_xvar = list_MarkerList[13]
        if list_MarkerList[17] == 13:
            variable_center_xvar = list_MarkerList[18]
        if list_MarkerList[22] == 13:
            variable_center_xvar = list_MarkerList[23]
        if 0.49 < variable_center_xvar and variable_center_xvar < 0.51:
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 100, 0, 100, rm_define.effect_always_on)
            variable_marker1seen = 1
            variable_marker1check = variable_marker1check + 1
        if variable_center_xvar > 0.49:
            chassis_ctrl.rotate_with_speed(rm_define.clockwise,3)
            variable_marker1seen = 1
            time.sleep(0.1)
        else:
            if 0.51 > variable_center_xvar:
                variable_marker1seen = 1
                chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,3)
                time.sleep(0.1)
        if list_MarkerList[1] == 0:
            rmexit()
def user_defined_release_can():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    chassis_ctrl.set_rotate_speed(3)
    chassis_ctrl.stop()
    if variable_dropcount == 0:
        robotic_arm_ctrl.moveto(175, -30, wait_for_complete=True)
        time.sleep(2)
        gripper_ctrl.open()
        time.sleep(2)
        robotic_arm_ctrl.moveto(160, 80, wait_for_complete=True)
        time.sleep(2)
    else:
        if variable_dropcount == 1:
            chassis_ctrl.rotate_with_time(rm_define.clockwise, 9)
            robotic_arm_ctrl.moveto(175, -30, wait_for_complete=True)
            time.sleep(2)
            gripper_ctrl.open()
            time.sleep(2)
            robotic_arm_ctrl.moveto(160, 80, wait_for_complete=True)
            time.sleep(2)
            chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 9)
        else:
            if variable_dropcount == 2:
                chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 9)
                robotic_arm_ctrl.moveto(175, -30, wait_for_complete=True)
                time.sleep(2)
                gripper_ctrl.open()
                time.sleep(2)
                robotic_arm_ctrl.moveto(160, 80, wait_for_complete=True)
                time.sleep(2)
                chassis_ctrl.rotate_with_time(rm_define.clockwise, 9)
            else:
                if variable_dropcount == 3:
                    chassis_ctrl.rotate_with_time(rm_define.clockwise, 18)
                    robotic_arm_ctrl.moveto(175, -30, wait_for_complete=True)
                    time.sleep(2)
                    gripper_ctrl.open()
                    time.sleep(2)
                    robotic_arm_ctrl.moveto(160, 80, wait_for_complete=True)
                    time.sleep(2)
                    chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 18)
    variable_dropcount = variable_dropcount + 1
def chassis_impact_detection(msg):
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    chassis_ctrl.stop()
def start():
    global variable_distance
    global variable_marker1check
    global variable_marker1seen
    global variable_arm_pos
    global variable_mark2xvalue
    global variable_avg
    global variable_gauge1
    global variable_gauge2
    global variable_wallrecursion_ct
    global variable_exit
    global variable_center_xvar
    global variable_accum_distance
    global variable_orientation
    global variable_orientationvariation
    global variable_overflow
    global variable_dropcount
    global variable_drop_direction
    global list_MarkerList
    global list_SightList
    global list_arm_pos
    user_defined_startup_condition()

    user_defined_center_marker1()

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    user_defined_distance_avg()

    variable_distance = variable_avg
    user_defined_grab1()

    user_defined_drop_heart_circle()

    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,5)
    user_defined_center_marker2()

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 193, 0, rm_define.effect_always_on)
    user_defined_distance_avg()

    variable_distance = variable_avg
    user_defined_grab2()

    user_defined_drop_heart_circle()

    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four)):
        chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,5)
    user_defined_center_marker4()

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 36, 103, 255, rm_define.effect_always_on)
    user_defined_distance_avg()

    variable_distance = variable_avg
    user_defined_grab4()

    user_defined_drop_heart_circle()

    while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three)):
        chassis_ctrl.rotate_with_speed(rm_define.clockwise,5)
    user_defined_center_marker3()

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 127, 70, rm_define.effect_always_on)
    user_defined_distance_avg()

    variable_distance = variable_avg
    user_defined_grab3()

    user_defined_drop_heart_circle()
