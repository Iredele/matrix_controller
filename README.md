# NeoPixel ROS 2 Package for scrap robot

## Overview

**NeoPixel ROS 2 Package** includes two nodes:

- **neo_pixel_node**: Controls a NeoPixel LED matrix by subscribing to the `led_cmd` topic.
- **led_control_node**: Publishes commands to the `led_cmd` topic to toggle LED colors.

## Installation

1. **Clone the Repository**

   Navigate to your ROS 2 workspace and clone the repository:

   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/Iredele/matrix_controller.git
   
   # Navigate back to the workspace root
   cd ~/ros2_ws

   # Build the package
   colcon build --packages-select neo_pixel_ros2_package

   # Source the workspace
   source install/setup.bash

2. **Usage**
Run both nodes in separate terminals after sourcing the workspace:
   ```bash
   # Terminal 1: Start the neo_pixel_node
   ros2 run neo_pixel_ros2_package neo_pixel_node

   # Terminal 2: Start the led_control_node
   ros2 run neo_pixel_ros2_package led_control_node

3. **Optional: Manual Control**
Alternatively, you can control the LEDs manually by publishing commands to the `led_cmd` topic:
   ```bash
    # Turn LEDs Red
    ros2 topic pub /led_cmd std_msgs/msg/Int8 "{data: 1}"

    # Turn LEDs Green
    ros2 topic pub /led_cmd std_msgs/msg/Int8 "{data: 0}"

    # Turn LEDs Off
    ros2 topic pub /led_cmd std_msgs/msg/Int8 "{data: 2}"
   
Developed by Dayo Iredele.

