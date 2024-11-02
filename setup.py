from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros-humble',
    maintainer_email='chiragcs2004@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "first_node = basics.my_first_node:main",
            "draw_circle = basics.draw_circle:main",
            "string_pub = basics.string_pub:main",
            "pose_sub = basics.pose_sub:main",
            "string_sub = basics.string_sub:main",
            "pub_sub = basics.pub_sub:main",
            
        ],
    },
)
