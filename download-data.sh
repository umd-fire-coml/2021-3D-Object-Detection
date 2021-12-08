#!/bin/bash
if [ ! -d "data/sequences" ]; then
    wget -c "https://s3.eu-central-1.amazonaws.com/avg-kitti/data_odometry_velodyne.zip"
    unzip data_odometry_velodyne.zip -d data
    wget -c "https://s3.eu-central-1.amazonaws.com/avg-kitti/data_odometry_calib.zip"
    unzip data_odometry_calib.zip -d data
    wget -c "http://www.semantic-kitti.org/assets/data_odometry_labels.zip"
    unzip data_odometry_labels.zip -d data

else
    echo "Directory data/sequences already exists, so there is no need to download anything else."
fi