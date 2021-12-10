# 3D Object Detection

# Product Description

This product identifies and labels 3D Objects in images of every day settings, such as cars, trees, bikes, pedestrians, etc. 

This product makes use of a UNet, which is a Convolutional Neural Network, to identify objects, given voxel data. Our product first takes point cloud data from the SemanticKITTI dataset, and converts it to voxels. For the sake of simplicity, a voxel can be described as a 3d pixel. We visualize these voxels as cubes, each cube containing spatial information in 3 dimensions.


# Directory Guide

data_generator.py
  - loads file paths of data into memory, when you call __getItem__(index) it reads the binary point cloud data and converts it to a voxel grid, and outputs the labels 
  
index_data.py
  - process the file paths for the data generator
  
Velodyne.py
  - converts the binary lidar file to a list of 3D points

Labels.py
  - Reads labels from the .label files

Citations
J. Behley, A. Milioto, C. Stachniss, M. Garbade, J. Gall, J. Quenzel, and S. Behnke, “Semantic Kitti Dataset Overview,” Semantickitti - A dataset for LIDAR-based Semantic Scene Understanding, 2020. [Online]. Available: http://www.semantic-kitti.org/dataset.html. [Accessed: 08-Dec-2021].
