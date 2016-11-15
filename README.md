# PygameRobot
Use Pygame to control a robot with your RaspberryPi.

I initially wrote this script to control a two-wheeled robot with realtime commands. Though using raw_input() is useful for many applications, it does not facilitate capturing realtime keyup and keydown events – this is where Pygame comes in handy. There are more advanced ways to do this without Pygame but they require knowledge of more advanced features like curses or getch(). 

This example is for a two-wheeled robot using a L298N motor driver.

Dependencies: Pygame
sudo apt-get install python-pygame
