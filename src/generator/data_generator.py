from numpy.core.numeric import indices
from tensorflow.keras.utils import Sequence

from .unpack_data import unpack_labels, unpack_velodyne
from .index_data import build_xy_filenames
from .preprocess_data import build_voxel_grids

import numpy as np

class DataGenerator(Sequence):
    def create_train_val_generators(data_source, validation_split=0.2, batch_size=8, voxel_grid_dim=512, voxel_resolution=0.088):
        x_filenames, y_filenames = build_xy_filenames(data_source)

        val_X, train_X = x_filenames[:(validation_split * len(x_filenames))], x_filenames[(validation_split * len(x_filenames)):]
        val_Y, train_Y = y_filenames[:(validation_split * len(y_filenames))], y_filenames[(validation_split * len(y_filenames)):]

        return (DataGenerator(train_X, train_Y, batch_size, voxel_grid_dim, voxel_resolution), 
                DataGenerator(val_X, val_Y, batch_size, voxel_grid_dim, voxel_resolution))
        
    def __init__(self, x_filenames, y_filenames, batch_size, voxel_grid_dim, voxel_resolution):
        self.batch_size = batch_size

        self.x_filenames, self.y_filenames = x_filenames, y_filenames

        self.voxel_grid_dim = voxel_grid_dim
        self.voxel_resolution = voxel_resolution

        self.indexes = np.arange(len(self.x_filenames))
        
        self.on_epoch_end()

    def __len__(self):
        """
        Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return len(self.x_filenames) // self.batch_size

    def __getitem__(self, index):
        """
        Generate one batch of data
        :param index: index of the batch
        :return: x_batch and y_batch
        """
        # Initialization
        x_batch = np.empty((self.batch_size, self.voxel_grid_dim, self.voxel_grid_dim, self.voxel_grid_dim, 1))
        y_batch = np.empty((self.batch_size, self.voxel_grid_dim, self.voxel_grid_dim, self.voxel_grid_dim, 1))

        # Generate indexes of the batch
        indexes = self.indexes[index * self.batch_size : (index + 1) * self.batch_size]

        # Generate data
        for i in range(self.batch_size):
            x_file_path, y_file_path = self.x_filenames[indexes[i]], self.y_filenames[indexes[i]]

            # loads converts file into pcd data point
            pcd = unpack_velodyne(x_file_path)
            pcd_list = np.asarray(pcd.points)
            lower_labels = np.asarray(unpack_labels(y_file_path))

            pcd_len = len(pcd_list)
            labels_len = len(lower_labels)
            assert pcd_len == labels_len, f"Got different labels and pcd len: {pcd_len}, {labels_len} for filenames {x_file_path}, {y_file_path}"
            print(f"PCD Length: {len(pcd_list)}, Lower Labels Length: {len(lower_labels)}")

            x_batch[i, ], y_batch[i, ] = build_voxel_grids(pcd_list, lower_labels, self.voxel_grid_dim, self.voxel_resolution)

        # Return batch data
        return x_batch, y_batch

    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        np.random.shuffle(self.indexes)