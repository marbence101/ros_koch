from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_course',  # Csomag neve
            executable='hello',  # Futtatható fájl neve (általában a .py fájl neve, kiterjesztés nélkül)
            name='koch_curve'  # Node neve
        )
    ])
