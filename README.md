# 3D Object Detection




# Directory Guide



data_generator.py
  - loads file paths of data into memory, when you call __getItem__(index) it reads the binary point cloud data and converts it to a voxel grid, and outputs the labels 
  
index_data.py
  - process the file paths for the data generator
  
Velodyne.py
  - converts the binary lidar file to a list of 3D points

Labels.py
  - Reads labels from the .label files

