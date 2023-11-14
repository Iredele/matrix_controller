import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

class LedControlNode(Node):
    def __init__(self):
        super().__init__('led_control_node')

        # Create a publisher for the "led_cmd" topic
        self.led_cmd_publisher = self.create_publisher(Int8, 'led_cmd', 10)

        # Timer to publish 1 or 0 every second (adjust as needed)
        self.timer = self.create_timer(1.0, self.publish_led_cmd)

        # Initialize LED state
        self.led_state = 0

    def publish_led_cmd(self):
        # Toggle LED state (1 or 0)
        self.led_state = 1 - self.led_state

        # Create and publish the message
        msg = Int8()
        msg.data = self.led_state
        self.led_cmd_publisher.publish(msg)
        self.get_logger().info(f'Published LED command: {self.led_state}')

def main(args=None):
    rclpy.init(args=args)

    led_control_node = LedControlNode()

    try:
        rclpy.spin(led_control_node)
    except KeyboardInterrupt:
        pass

    led_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
