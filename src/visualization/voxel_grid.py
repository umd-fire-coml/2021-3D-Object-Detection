import open3d as o3d
import numpy as np

from itertools import combinations, combinations_with_replacement

index_to_color = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 255],
    [245, 150, 100],
    [245, 230, 100],
    [250, 80, 100],
    [150, 60, 30],
    [255, 0, 0],
    [180, 30, 80],
    [255, 0, 0],
    [30, 30, 255],
    [200, 40, 255],
    [90, 30, 150],
    [255, 0, 255],
    [255, 150, 255],
    [75, 0, 75],
    [75, 0, 175],
    [0, 200, 255],
    [50, 120, 255],
    [0, 150, 255],
    [170, 255, 150],
    [0, 175, 0],
    [0, 60, 135],
    [80, 240, 150],
    [150, 240, 255],
    [0, 0, 255],
    [255, 255, 50],
    [245, 150, 100],
    [255, 0, 0],
    [200, 40, 255],
    [30, 30, 255],
    [90, 30, 150],
    [250, 80, 100],
    [180, 30, 80],
    [255, 0, ]
]

def display_voxel_grid(input_grid, output_grid: np.ndarray):
    X, Y = np.squeeze(input_grid), np.squeeze(output_grid)
    points = []
    colors = []

    for x, y, z in combinations_with_replacement(range(len(X)), 3):
        if X[x, y, z] != 0:
            points.append([x, y, z])
            colors.append(index_to_color[Y[x, y, z]])

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.asarray(points))
    pcd.colors = o3d.utility.Vector3dVector(np.asarray(colors))

    o3d.visualization.draw_geometries([pcd])