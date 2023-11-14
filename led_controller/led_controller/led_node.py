import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

class NeoPixelNode(Node):
    def __init__(self):
        super().__init__('neo_pixel_node')

        # NeoPixel configuration
        pixel_pin = board.D18
        pixel_width = 32
        pixel_height = 32

        self.pixels = neopixel.NeoPixel(
            pixel_pin,
            pixel_width * pixel_height,
            brightness=0.1,
            auto_write=False,
        )

        self.pixel_framebuf = PixelFramebuffer(
            self.pixels,
            32,
            32,
            reverse_x=True,
        )

        # Subscribe to the "led_cmd" topic
        self.subscription = self.create_subscription(
            Int8,
            'led_cmd',
            self.led_cmd_callback,
            10  # QoS profile depth
        )

    def led_cmd_callback(self, msg):
        # Change LED color based on the received message
        if msg.data == 1:
            # Turn LEDs red
            self.pixel_framebuf.fill(0xFF0000)
        elif msg.data == 0:
            # Turn LEDs green
            self.pixel_framebuf.fill(0x00FF00)
        else:
            # Invalid command, turn LEDs off
            self.pixel_framebuf.fill(0x000000)

        # Display the new LED color
        self.pixel_framebuf.display()

    def destroy_node(self):
        self.pixels.deinit()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    neo_pixel_node = NeoPixelNode()

    try:
        rclpy.spin(neo_pixel_node)
    except KeyboardInterrupt:
        pass

    neo_pixel_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
