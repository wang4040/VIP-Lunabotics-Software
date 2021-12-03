cd ~
mkdir -p rplidar_ws/src
sudo git clone https://github.com/Slamtec/rplidar_ros.git
cd rplidar_ros
sudo mv * ~/rplidar_ws/src
cd ~/rplidar_ws/
catkin_make