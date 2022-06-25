# Wall Follower Robot
Robotics project for 2nd semester of 2022 @SBU 

# Description
This project is a practice for ***image processing*** and ***wall following*** techniques using Webots with python controllers
The scenario is that we have two rooms in map and two portraits in them. robot should walk to nearest wall and follow the wall until catch a painting, take pictures of it and detect if the painting is our target, if it was'nt target countinue.

<br/>
<br/>

### Wall Following
Robot has a sonar sensor and 2 Infrared sensors in each side, using them detect the distance and change motor speeds

### Shape Detection
After camera of robot takes pictures in specific positions, the picture processed using OpenCV 

<br/>

### State machine of robot for wall following
![state_machine](https://s6.uupload.ir/files/statemachine_koeu.png)
