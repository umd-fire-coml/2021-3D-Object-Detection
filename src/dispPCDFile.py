import open3d as o3d
from open3d import *
import struct
import numpy as np
from cvtToPCDFunction import convert_kitti_bin_to_pcd
from random import*

from segmentPoints import*

pcd = convert_kitti_bin_to_pcd('data\\example_dataset\\sequences\\03\\velodyne\\000000.bin')
#open3d.io.write_point_cloud("temp.pcd", temp)
#pcd = o3d.io.read_point_cloud("temp.pcd")
#print(pcd)



test = convert_kitti_bin_to_pcd('data\\example_dataset\\sequences\\00\\labels\\000000.label')

#print(np.asarray(test).shape)


print(np.asarray(pcd.points).shape)

curArray = np.asarray(pcd.points)

print(curArray[0])
print(curArray[0][0])




#[0,0,0] = The position of the camera, Center of the point cloud

minRandom = -5
maxRandom = 5


x =  minRandom + (random() * (maxRandom - minRandom))
y =  minRandom + (random() * (maxRandom - minRandom))
z =  minRandom + (random() * (maxRandom - minRandom))
origin = [x, y,z]


boxLength = 10
bounds = [-boxLength/2+x, boxLength/2+x, -boxLength/2+y, boxLength/2+y, -boxLength/2+z, boxLength/2+z]




filtered = get_filtered_lidar(curArray, bounds)

print(len(filtered))



pcdPoints = cvtToPCD(filtered)

o3d.visualization.draw_geometries([pcdPoints])

#o3d.visualization.draw_geometries([pcd])
