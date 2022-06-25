# important points:
# use <robot_position> to get current position of robot in <x,y,theta> format.
# use <robot_omega> to get current values for the wheels in <w1,w2,w3> format.

# import numpy as np
from initialization import *
from image_detection import *


if __name__ == "__main__":
    TIME_STEP = 32
    camera,robot = init_robot(time_step=TIME_STEP)
    init_robot_state(in_pos=[0, 0, 0], in_omega=[0, 0, 0])
    update_motor_speed(input_omega=[0, 0, 0])
    state = 0
    step_i = 0
    tmp1 = tmp2 = 0;
    tmp_v_state =0
    sleep_state =0 
    count_sleep = 0
    while robot.step(TIME_STEP) != -1:
        
        # image = np.frombuffer(a, np.uint8).reshape((camera.getHeight(), camera.getWidth(), 4))
        # print(type(image))
        # image_detection(image)
        # camera.getImage()
        if(sleep_state == 1):
            print("sleep state")
            count_sleep+=1
            if(count_sleep == 10):
                sleep_state = 0
                count_sleep = 0
        else:  
            if(step_i%5 == 0):
                step_i = 0
 
            gps_values, compass_val, sonar_value, encoder_value, ir_value = read_sensors_values()
            update_robot_state()

            if(state == 0):
                
                if(sonar_value[0]<5):
                    state = 1;
                    update_motor_speed(input_omega=[0, 0, 0])
                    sleep_state = 1
                
                if(sonar_value[0]>5):
                    update_motor_speed(input_omega=[10, 0, -10])
            
            
            elif(state == 1):
                print("1")
                if(step_i == 0):
                    tmp1 = ir_value[2]
                    tmp2 = ir_value[5]
                
                
                if(ir_value[4]<800):
                        state = 4
                        update_motor_speed(input_omega=[0, 0, 0])
                        sleep_state = 1
                else:
                    if(tmp_v_state == 1 or (tmp1 - ir_value[2]>2 )):
                        print("close error")
                        update_motor_speed(input_omega=[5.2, -10, 5.2])
                        tmp_v_state = 1
                    
                    
                    if(tmp_v_state == 2 or (tmp1 - ir_value[2]< -2 )):
                        print("far error")
                        update_motor_speed(input_omega=[4.8, -10, 4.8])
                        tmp_v_state = 2

                    if(ir_value[2] >= 1000 and ir_value[5] >= 1000 and sonar_value[0]>=1000):
                        state = 2
                        update_motor_speed(input_omega=[0, 0, 0])
                        sleep_state = 1

                
            elif(state == 2):   
                print("2")
                update_motor_speed(input_omega=[0, -10, -2])
                if(ir_value[2] < 850):
                    state = 3
                    update_motor_speed(input_omega=[0, 0, 0])
                    sleep_state = 1
                
            
            
            elif(state == 3):
                print("3")
                if(step_i == 0):
                    tmp1 = ir_value[2]
                    tmp2 = ir_value[5]
                
                if(gps_values[1] <2.4 and gps_values[1] >2.3):
                    state = 3 
                    a = camera.getImage()
                    #update_motor_speed(input_omega=[0, 0, 0])
                    #sleep_state = 1
                    image = np.frombuffer(a, np.uint8).reshape((camera.getHeight(), camera.getWidth(), 4))
                    print(type(image))
                    o = image_detection(image)
                    if (o ==  target_shape):
                        print("object founded")
                        break
                
                else:
                    

                    if(ir_value[4]<800):
                        state = 4
                        update_motor_speed(input_omega=[0, 0, 0])
                        sleep_state = 1
                    else:
                        if(tmp_v_state == 1 or (tmp1 - ir_value[2]>2 or tmp2 - ir_value[5]>2)):
                            print("close error")
                            update_motor_speed(input_omega=[5.2, -10, 5.2])
                            tmp_v_state = 1
                        
                        
                        if(tmp_v_state == 2 or (tmp1 - ir_value[2]< -2 or tmp2 - ir_value[5]< -2)):
                            print("far error")
                            update_motor_speed(input_omega=[4.6, -10, 4.6])
                            tmp_v_state = 2
                        
                        if(ir_value[2] >= 1000 and ir_value[5] >= 1000 and sonar_value[0]>=1000):
                            state = 2
                            update_motor_speed(input_omega=[0, 0, 0])
                            sleep_state = 1

                
            
            
            
            elif(state == 4):
                print("4")
                update_motor_speed(input_omega=[6, 3, 10])
                
                if(ir_value[2] < 800 and sonar_value[1]<200):
                    state = 3
                    update_motor_speed(input_omega=[0, 0, 0])
                    sleep_state = 1

            print(gps_values)    
            print(sonar_value)
            print(ir_value[2])
            print(ir_value[5])
            # print(ir_value[1])
            # print(ir_value[3])
            # print(ir_value[4])
            # print(ir_value[0])
            print("------------")
            
            
            step_i +=1
    
    update_motor_speed(input_omega=[0, 0, 0])
        
        