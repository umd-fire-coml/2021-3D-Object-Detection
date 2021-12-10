import numpy as np
from tensorflow.keras.utils import Sequence
from cvtToPCDFunction import convert_kitti_bin_to_pcd
from open3d import *
from segmentPoints import*
from getAllFiles import*
from readLabels import return_lower_labels
from readLabels import convert_all_kitti

class DataGenerator(Sequence):
    '''this is a random data generator, edit this data generator to read data from dataset folder and return a batch with __getitem__'''

    def __init__(self, batch_size=8, x_shape=(130000, 3), y_shape=(130000,), n_dataset_items=233):
        self.batch_size = batch_size
        self.x_shape = x_shape
        self.y_shape = y_shape
        self.n_dataset_items = n_dataset_items
        self.indexes = np.arange(self.n_dataset_items)
        self.on_epoch_end()

        # Use getAllImages function to get all images that are type .bin
        self.x_filepaths = getAllFiles('data/example_dataset/sequences', '.bin')

        #use getAllImages function to get all labels that are type .label
        self.y_labels = getAllFiles('data/example_dataset/sequences', '.label')

        self.X_DATASET = self.x_filepaths
        self.Y_DATASET = self.y_labels

    def __len__(self):
        """Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return int(np.floor(self.n_dataset_items / self.batch_size))

    def __getitem__(self, index):
        """Generate one batch of data
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
            pcd = convert_kitti_bin_to_pcd(self.X_DATASET[indexes[i]])

            pcdList = np.asarray(pcd.points).tolist()
            
            map = convert_all_kitti(self.Y_DATASET[indexes[i]])
            lowerLabels = (return_lower_labels(map))

            #print("diff is")
            #print(self.x_shape[0] - len(pcdList))
            
            for x in range(self.x_shape[0] - len(pcdList)):
                pcdList.append([0,0,0])
                lowerLabels.append(0)

            #converts to array and filters to 70, 70, 70
            #x_batch[i,], y_batch[i,]= get_filtered_lidar(np.asarray(pcdList), bounds, np.asarray(lowerLabels))

            x_batch[i, ] = np.asarray(pcdList)
            y_batch[i, ] = np.asarray(lowerLabels)

            
            


            #y_batch[i,] = self.Y_DATASET[indexes[i]]

        # Return batch data
        return x_batch, y_batch



    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        np.random.shuffle(self.indexes)

