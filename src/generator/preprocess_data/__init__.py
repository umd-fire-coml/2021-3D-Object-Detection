import numpy as np
from sklearn.preprocessing import OneHotEncoder

def label_to_class_index(label):
    return {
        0: 1,
        1: 2,
        10: 3,
        11: 4,
        13: 5,
        15: 6,
        16: 7,
        18: 8,
        20: 9,
        30: 10,
        31: 11,
        32: 12,
        40: 13,
        44: 14,
        48: 15,
        49: 16,
        50: 17,
        51: 18,
        52: 19,
        60: 20,
        70: 21,
        71: 22,
        72: 23,
        80: 24,
        81: 25,
        99: 26,
        252: 27,
        253: 28,
        254: 29,
        255: 30,
        256: 31,
        257: 32,
        258: 33,
        259: 34
    }[label]

def build_voxel_grids(pcd, labels, grid_dim, voxel_resolution):
    x_grid = np.zeros((grid_dim, grid_dim, grid_dim))
    y_grid = np.zeros((grid_dim, grid_dim, grid_dim))

    octant_dim = grid_dim // 2
    
    pcd = np.round(pcd / voxel_resolution).astype(int)
    valid_indices = (np.min(pcd, axis=1) > -octant_dim) & (np.max(pcd, axis=1) < octant_dim)

    pcd, labels = pcd[valid_indices], labels[valid_indices]
    pcd += octant_dim

    for coord, label in zip(pcd, labels):
        x_grid[tuple(coord)] = 1
        y_grid[tuple(coord)] = label_to_class_index(label)
    
    return x_grid.reshape((grid_dim, grid_dim, grid_dim, 1)), y_grid.reshape((grid_dim, grid_dim, grid_dim, 1))