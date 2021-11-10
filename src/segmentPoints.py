import numpy as np
import open3d as o3d

from open3d import*


def cvtToPCD(myList):
    customPoints = o3d.geometry.PointCloud()
    customPoints.points = open3d.utility.Vector3dVector(myList)

    return customPoints


def get_filtered_lidar(lidar, boundary, labels=None):
    minX = boundary[0]
    maxX = boundary[1]
    minY = boundary[2]
    maxY = boundary[3]
    minZ = boundary[4]
    maxZ = boundary[5]

    # Remove the point out of range x,y,z
    mask = np.where((lidar[:, 0] >= minX) & (lidar[:, 0] <= maxX) &
                    (lidar[:, 1] >= minY) & (lidar[:, 1] <= maxY) &
                    (lidar[:, 2] >= minZ) & (lidar[:, 2] <= maxZ))
    lidar = lidar[mask]
    lidar[:, 2] = lidar[:, 2] - minZ

    if labels is not None:
        labels = labels[mask]
        return lidar, labels
    else:
        return lidar
