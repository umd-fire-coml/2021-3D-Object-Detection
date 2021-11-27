from tensorflow.keras.layers import Activation, concatenate, Layer
from tensorflow.python.keras.layers.convolutional import Conv3DTranspose
from .down_conv import DownConvBlock


class TransConvBlock(Layer):
    def __init__(self, downconv_block, n_filters, kernel_size, **kwargs):
        super(TransConvBlock, self).__init__(kwargs)

        self.n_filters = n_filters
        self.kernel_size = kernel_size
        self.downconv_block = downconv_block

    def call(self, x):
        tconv = Conv3DTranspose(
            self.n_filters,
            (self.kernel_size, self.kernel_size, self.kernel_size),
            strides=(2, 2, 2),
            padding="same",
        )(x)

        return concatenate([tconv, self.downconv_block])
