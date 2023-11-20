#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class KochSnowflake(Node):

    def __init__(self):
        super().__init__('koch_snowflake')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.length = 4.0  # A vonal kezdeti hossza
        self.angle = 60.0  # A fordulási szög fokban

    def draw_koch_segment(self, length, level):
        if level == 0:
            move_cmd = Twist()
            move_cmd.linear.x = length
            self.publisher_.publish(move_cmd)
            time.sleep(1)  # Adjon időt a turtlesimnek a mozgásra
        else:
            length /= 3.0
            self.draw_koch_segment(length, level - 1)
            self.rotate_turtle(-self.angle)
            self.draw_koch_segment(length, level - 1)
            self.rotate_turtle(2 * self.angle)
            self.draw_koch_segment(length, level - 1)
            self.rotate_turtle(-self.angle)
            self.draw_koch_segment(length, level - 1)

    def rotate_turtle(self, angle):
        turn_cmd = Twist()
        turn_cmd.angular.z = math.radians(angle)
        self.publisher_.publish(turn_cmd)
        time.sleep(1)  # Adjon időt a turtlesimnek a fordulásra

    def draw_snowflake(self):
        # Először elforgatjuk a teknőst, hogy a kezdővonal a hópehely egyik csúcsától induljon
        self.rotate_turtle(-90)  # Elforgatás felfelé
        # A hópehely minden oldalának megrajzolása
        for _ in range(3):
            self.draw_koch_segment(self.length, 3)  # A rekurzió mélységét itt állítjuk be
            self.rotate_turtle(120)

def main(args=None):
    rclpy.init(args=args)
    koch_snowflake = KochSnowflake()
    koch_snowflake.draw_snowflake()
    koch_snowflake.publisher_.publish(Twist())  # Megállítjuk a teknőst
    koch_snowflake.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

