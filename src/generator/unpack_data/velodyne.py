import numpy as np
import open3d as o3d
import struct

def read_from_bin(source_path):
    size_float = 4
    list_pcd = []

    with open(source_path, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, _ = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)

    return list_pcd

def unpack_velodyne(source_path):
    """
    Converts binary velodyne data (supplied as .bin) into PCD format.
    """
    np_pcd = np.asarray(read_from_bin(source_path))
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np_pcd)

    return pcd