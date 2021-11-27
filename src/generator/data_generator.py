from tensorflow.keras.utils import Sequence

from .unpack_data import unpack_labels, unpack_velodyne
from .utils import filter_many_by_ext

import numpy as np

class DataGenerator(Sequence):
    def __init__(self, batch_size=8, x_shape=(130000, 3), y_shape=(130000,), n_dataset_items=233):
        self.batch_size = batch_size
        self.x_shape = x_shape
        self.y_shape = y_shape

        self.X, self.y = filter_many_by_ext('data/example_dataset', ('.bin', '.label'))
        assert len(self.X) == len(self.y), "X and y are of different sizes."
        
        self.indexes = np.arange(len(self.X))
        
        self.on_epoch_end()

    def __len__(self):
        """
        Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return len(self.X) // self.batch_size

    def __getitem__(self, index):
        """
        Generate one batch of data
        :param index: index of the batch
        :return: x_batch and y_batch
        """
        # Initialization
        x_batch = np.empty((self.batch_size, *self.x_shape))
        y_batch = np.empty((self.batch_size, *self.y_shape))

        # Generate indexes of the batch
        indexes = self.indexes[index * self.batch_size : (index + 1) * self.batch_size]

        x =  0 #minRandom + (random() * (maxRandom - minRandom))
        y =  0 #minRandom + (random() * (maxRandom - minRandom))
        z =  0 #minRandom + (random() * (maxRandom - minRandom))
        origin = [x, y,z]


        boxLength = 70
        bounds = [-boxLength/2+x, boxLength/2+x, -boxLength/2+y, boxLength/2+y, -boxLength/2+z, boxLength/2+z]

        # Generate data
        for i in range(self.batch_size):
            # loads converts file into pcd data point
            pcd = unpack_velodyne(self.X[indexes[i]])
            lower_labels = unpack_labels(self.y[indexes[i]])

            pcd_list = np.asarray(pcd.points).tolist()


            #print("diff is")
            #print(self.x_shape[0] - len(pcdList))

            for x in range(self.x_shape[0] - len(pcd_list)):
                pcd_list.append([0,0,0])
                lower_labels.append(0)

            #converts to array and filters to 70, 70, 70
            #x_batch[i,], y_batch[i,]= get_filtered_lidar(np.asarray(pcdList), bounds, np.asarray(lowerLabels))

            x_batch[i, ] = np.asarray(pcd_list)
            y_batch[i, ] = np.asarray(lower_labels)

            #y_batch[i,] = self.Y_DATASET[indexes[i]]

        # Return batch data
        return x_batch, y_batch

    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        np.random.shuffle(self.indexes)