# VIP Lunabotics Software code repository
This is my Repository for all my code for VIP Lunabotics


The master branch contains the 3D Pybullet Implementation of the sampling-based motion planning algorithms


The 2D-motion-planner branch contains the 3D Pybullet Implementation of the sampling-based motion planning algorithms


The mosse-tracking branch contains camera tracking software from my team last semester


The rplidar branch contains code for setting up point-cloud map data from RPLidar


# Notes on how to run the 2D and 3D simulations:


To run the 2D simulation: Go to the 2d-motion-planner branch, use command `python -m motion_planners.tkinter.run`. Use args '-a' to specify the specific algorithm to run ('prm', 'lazy_prm', 'lazy_prm_star', 'rrt', 'rrt_star', 'birrt', 'rrt_connect'. Use args '-i' to specify the number of iterations. To enable the graph, comment out the statement 'draw=False'  in the main() function in tkinter\run.py


To run the 3D simulation: Go to the master branch, use command `python -m examples.test_turtlebot_motion`. Use args '-a' to specify the specific algorithm to run ('prm', 'lazy_prm', 'lazy_prm_star', 'rrt', 'rrt_star', 'birrt', 'rrt_connect'. Use args '-i' to specify the number of iterations. To disable the PyBullet GUI interface, uncomment the statement 'use_gui=False' in the connect() function in pybullet_tools\utils.py


Jerry Wang
