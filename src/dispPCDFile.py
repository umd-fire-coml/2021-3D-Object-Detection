import open3d as o3d
from open3d import *
import struct
import numpy as np
from cvtToPCDFunction import convert_kitti_bin_to_pcd

temp = convert_kitti_bin_to_pcd('C:\\Users\\fpras\\FIRE298\\2021-3D-Object-Detection\\data\\example_dataset\\sequences\\00\\velodyne\\000001.bin')
open3d.io.write_point_cloud("temp.pcd", temp)
pcd = o3d.io.read_point_cloud("temp.pcd")
#print(pcd)
print(np.asarray(pcd.points).shape)
#print(np.shape(pcd))
o3d.visualization.draw_geometries([pcd])