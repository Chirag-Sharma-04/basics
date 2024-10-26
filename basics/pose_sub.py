#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class Posesub(Node):
    
    def __init__(self):
        super().__init__("pose_sub")
        self.pose_sub_=self.create_subscription(Twist, "/cmd_vel", self.pose_callback, 10)
    
    def pose_callback(self, msg:Twist):
        self.get_logger().info("( x: " + str(msg.linear.x) + " , y: " + str(msg.angular.z) + " )")

def main(args=None):
    rclpy.init(args=args)
    node=Posesub()
    rclpy.spin(node)
    rclpy.shutdown()