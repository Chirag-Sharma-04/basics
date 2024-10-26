#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class String_pub(Node):

    def __init__(self):
        super().__init__("string_pub")
        self.string_pub_= self.create_publisher(String, "/string_pub/data",10)
        self.timer_= self.create_timer(1 ,self.String_pub)
        self.get_logger().info("String_pub has started ")

    def String_pub(self):
        msg=String()
        msg.data=" Hellloooooo "
        self.string_pub_.publish(msg)
            



def main(args=None):
    rclpy.init(args=args)
    node=String_pub()
    rclpy.spin(node)
    rclpy.shutdown()