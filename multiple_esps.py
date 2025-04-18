from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='micro_ros_agent_1',
            output='screen',
            arguments=['serial', '--dev', '/dev/ttyUSB0']
        ),
        Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='micro_ros_agent_2',
            output='screen',
            arguments=['serial', '--dev', '/dev/ttyUSB1']
        )
    ])
