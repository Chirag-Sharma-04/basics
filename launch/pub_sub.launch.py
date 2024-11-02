from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    pub_sub=Node(
        package="basics",
        executable="pub_sub"
    )


    return LaunchDescription([
        pub_sub,
        
    ])