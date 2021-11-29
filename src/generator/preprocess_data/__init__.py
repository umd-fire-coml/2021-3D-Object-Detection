import numpy as np

def build_voxel_grids(pcd, labels, grid_dim, voxel_resolution):
    x_grid = np.zeros((grid_dim, grid_dim, grid_dim))
    y_grid = np.zeros((grid_dim, grid_dim, grid_dim))

    octant_dim = grid_dim // 2
    
    pcd = np.round(pcd / voxel_resolution).astype(int)
    valid_indices = (np.min(pcd, axis=1) > -octant_dim) & (np.max(pcd, axis=1) < octant_dim)

    pcd, labels = pcd[valid_indices], labels[valid_indices]
    pcd += octant_dim
    print(len({tuple(row) for row in pcd}))

    for coord, label in zip(pcd, labels):
        x_grid[tuple(coord)] = 1
        y_grid[tuple(coord)] = label
    
    return x_grid, y_grid