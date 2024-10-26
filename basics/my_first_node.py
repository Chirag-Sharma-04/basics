#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(Self):
        super().__init__("first_node")
        Self.counter_ = 0
        Self.create_timer(1.0, Self.timer_callback)
       

    def timer_callback(Self):
         Self.get_logger().info("Hellloooo from rosss " + str(Self.counter_))
         Self.counter_ +=1


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()