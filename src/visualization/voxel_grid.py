import open3d as o3d
import numpy as np

from itertools import combinations, combinations_with_replacement

def display_voxel_grid(grid: np.ndarray):
    unpacked_data = [((x, y, z), grid[x, y, z]) for (x, y, z) in combinations_with_replacement(range(len(grid)), 3) if grid[x, y, z] != 0]
