import numpy as np
import open3d as o3d

from open3d import*


def cvtToPCD(myList):
    customPoints = o3d.geometry.PointCloud()
    customPoints.points = open3d.utility.Vector3dVector(myList)

    return customPoints
    


def getSegments(pcd, bounds):
    #bounds will be array of x min, x max, y min, y max
    result_segments = []

    originalArray = np.asarray(pcd.points)

    inboundsArray = []

    index = 0
    while index < originalArray.shape[0]:
        x = originalArray[index][0]
        y = originalArray[index][1]
        if(x >bounds[0] and x<bounds[1] and y> bounds[2] and y< bounds[3] ) :

            
            inboundsArray.append(originalArray[index])

        index= index +1


    return inboundsArray

def shrinkArray(array, factor):
    result_array = []

    index = 0
    while index < len(array):
        if(index % factor == 0) :
            result_array.append(array[index])
        index = index +1

    return result_array



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