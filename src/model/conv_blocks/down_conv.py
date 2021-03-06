from tensorflow.keras.layers import Activation, Conv3D, BatchNormalization, Layer
from tensorflow.python.keras.layers.normalization.batch_normalization import BatchNormalization

import numpy as np

class DownConvBlock(Layer):
    def __init__(self, num_filters, kernel_size, **kwargs):
        super(DownConvBlock, self).__init__(**kwargs)

        self.num_filters = num_filters
        self.kernel_size = kernel_size

    def call(self, x):
        for i in range(0, 2):
            x = Conv3D(
                self.num_filters, 
                kernel_size=(
                    self.kernel_size, self.kernel_size, self.kernel_size
                ),
                padding="same",
                kernel_initializer="he_normal",
                data_format="channels_last"
            )(x)
            x = BatchNormalization()(x)
            x = Activation('relu')(x)

        return x