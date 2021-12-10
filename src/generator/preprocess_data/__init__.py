import numpy as np
from sklearn.preprocessing import OneHotEncoder

def label_to_class_index(label):
    return {
        0: 0,
        1: 1,
        10: 2,
        11: 3,
        13: 4,
        15: 5,
        16: 6,
        18: 7,
        20: 8,
        30: 9,
        31: 10,
        32: 11,
        40: 12,
        44: 13,
        48: 14,
        49: 15,
        50: 16,
        51: 17,
        52: 18,
        60: 19,
        70: 20,
        71: 21,
        72: 22,
        80: 23,
        81: 24,
        99: 25,
        252: 26,
        253: 27,
        254: 28,
        255: 29,
        256: 30,
        257: 31,
        258: 32,
        259: 32
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