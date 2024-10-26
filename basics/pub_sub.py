#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Pub_sub(Node):

    def __init__(self):
        super().__init__("pub_sub")
        self.pub_=self.create_publisher(String, "/command" ,10)
        self.sub_=self.create_subscription(Twist, "/cmd_vel", self.pub_sub_callback , 10)
        self.get_logger().info("Pub_sub has started ")

    def pub_sub_callback(self, twist:Twist):
        msg=String()
        if twist.linear.x == 0.5 and twist.angular.z == 0:
            msg.data="Forward"
        elif twist.linear.x == -0.5 and twist.angular.z == 0:
            msg.data="Backward"
        elif twist.linear.x == 0.0 and twist.angular.z == -1.0:
            msg.data="Right"
        elif twist.linear.x == 0.0 and twist.angular.z == 1.0:
            msg.data="Left"
        elif twist.linear.x == 0.0 and twist.angular.z == 0.0:
            msg.data="Stop"
        self.pub_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node= Pub_sub()
    rclpy.spin(node)
    rclpy.shutdown()