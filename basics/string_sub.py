#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class String_sub(Node):

    def __init__(self):
        super().__init__("string_sub")
        self.string_sub_=self.create_subscription(String, "/string_pub/data" , self.string_callback , 10)


    def string_callback(self, msg:String):
        self.get_logger().info(str(msg.data))


def main (args=None):
    rclpy.init(args=args)
    node=String_sub()
    rclpy.spin(node)
    rclpy.shutdown()