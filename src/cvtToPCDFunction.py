import sys
print(sys.version)

import numpy as np
import struct
from open3d import *

def convert_kitti_bin_to_pcd(binFilePath):
    size_float = 4
    list_pcd = []
    with open(binFilePath, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)
    pcd = open3d.geometry.PointCloud()
    pcd.points = open3d.utility.Vector3dVector(np_pcd)

    return pcd

pcd = convert_kitti_bin_to_pcd("C:\\Users\\fpras\\FIRE298\\2021-3D-Object-Detection\\notebooks\\data\\velodyne\\000000.bin")


#open3d.io.write_point_cloud("copy_of_fragment.pcd", pcd)


print(pcd)