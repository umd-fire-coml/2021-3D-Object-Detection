import numpy as np
import os
from tensorflow.keras.utils import Sequence
from cvtToPCDFunction import convert_kitti_bin_to_pcd
import open3d as o3d
from open3d import *
from segmentPoints import*
from getAllFiles import*
from readLabels import*


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
        label_x = (labels[:, 1] >= minX) & (labels[:, 1] < maxX)
        label_y = (labels[:, 2] >= minY) & (labels[:, 2] < maxY)
        label_z = (labels[:, 3] >= minZ) & (labels[:, 3] < maxZ)
        mask_label = label_x & label_y & label_z
        labels = labels[mask_label]
        return lidar, labels
    else:
        return lidar

def testing_filter(lidar, boundary, labels=None):
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
        label_x = (labels[:, 1] >= minX) & (labels[:, 1] < maxX)
        label_y = (labels[:, 2] >= minY) & (labels[:, 2] < maxY)
        label_z = (labels[:, 3] >= minZ) & (labels[:, 3] < maxZ)
        mask_label = label_x & label_y & label_z
        labels = labels[mask_label]
        return lidar, labels
    else:
        return lidar

if __name__ == "__main__":

    list = []
    list2 = []
    print("Hello")

    x_shape=(70, 70, 70)
    y_shape=(1,)
    boxLength = 70
    bounds = [-boxLength/2, boxLength/2, -boxLength/2, boxLength/2, -boxLength/2, boxLength/2]

    x_batch = np.empty((8, *x_shape))

    map = convert_all_kitti('data\\example_dataset\\sequences\\00\\labels\\000000.label')

    for value in map:
        high, low = value
        list.append((high, low))
        list2.append(low)
    
    list3 = [1, 2, 3, 4, 5]
    print(np.shape(list3))
    

    
    #list = return_lower_labels(list)
    pcd = convert_kitti_bin_to_pcd('data\\example_dataset\\sequences\\00\\velodyne\\000000.bin')

    print(np.shape(list))
    print(np.shape(list2))

    print(np.shape(pcd.points))

    #filter = get_filtered_lidar(np.asarray(pcd.points), bounds, list)
    filter = get_filtered_lidar(np.asarray(pcd.points), bounds, list2)
