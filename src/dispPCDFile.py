import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("copy_of_fragment.pcd")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])