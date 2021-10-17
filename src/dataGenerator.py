import numpy as np
import os
from tensorflow.keras.utils import Sequence

class DataGenerator(Sequence):
    '''this is a random data generator, edit this data generator to read data from dataset folder and return a batch with __getitem__'''

    def __init__(self, batch_size=8, x_shape=(70, 70, 70), y_shape=(1,), n_dataset_items=233):
        self.batch_size = batch_size
        self.x_shape = x_shape
        self.y_shape = y_shape
        self.n_dataset_items = n_dataset_items
        self.indexes = np.arange(self.n_dataset_items)
        self.on_epoch_end()
        
        # DELETE THIS WHEN USING YOUR OWN DATASET, DO NOT STORE THE ACTUAL DATASET IN MEMEORY HERE
        #self.X_DATASET = [np.random.rand(*self.x_shape) for i in range(self.n_dataset_items)] 
        #self.Y_DATASET = [np.random.rand(*self.y_shape) for i in range(self.n_dataset_items)]


        # Use get all images function that are type of .bin
       # self.x_filepaths = os.listdir('./test/data/images')
       # self.y_labels = np.genfromtxt('./test/data/image_labels.txt', dtype = 'int')

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

        # Generate data
        for i in range(self.batch_size):
            x_batch[i,] = self.X_DATASET[indexes[i]]
            y_batch[i,] = self.Y_DATASET[indexes[i]]

        # Return batch data
        return x_batch, y_batch



    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        np.random.shuffle(self.indexes)

