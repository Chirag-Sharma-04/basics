import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory


def generate_launch_description():

    pub_sub_launch=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory("basics"),
                "launch"
            ), "/pub_sub.launch.py"
        ]),
    )

    tur = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('basics'), 'launch'),
         '/pub_sub.launch.py'])
    )

    string_pub=Node(
        package="basics",
        executable="string_pub",
        output="screen"
    )


    return LaunchDescription([

        string_pub,
        #pub_sub_launch,
        tur
        
    ])

