from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    esp32_1_device_arg = DeclareLaunchArgument(
        'esp32_1_device',
        default_value='/dev/ttyUSB0',
        description='ESP32 #1 USB device path'
    )
    
    esp32_2_device_arg = DeclareLaunchArgument(
        'esp32_2_device',
        default_value='/dev/ttyUSB1',
        description='ESP32 #2 USB device path'
    )
    
    micro_ros_agent1 = ExecuteProcess(
        cmd=['ros2', 'run', 'micro_ros_agent', 'micro_ros_agent', 'serial', '--dev', 
             LaunchConfiguration('esp32_1_device')],
        name='micro_ros_agent_1',
        output='screen'
    )
    
    micro_ros_agent2 = ExecuteProcess(
        cmd=['ros2', 'run', 'micro_ros_agent', 'micro_ros_agent', 'serial', '--dev', 
             LaunchConfiguration('esp32_2_device')],
        name='micro_ros_agent_2',
        output='screen'
    )
    
    return LaunchDescription([
        esp32_1_device_arg,
        esp32_2_device_arg,
        micro_ros_agent1,
        micro_ros_agent2
    ])
