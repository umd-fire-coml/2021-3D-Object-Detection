from tensorflow.keras.layers import concatenate, Layer
from tensorflow.python.keras.layers.convolutional import Conv3DTranspose


class TransConvBlock(Layer):
    def __init__(self, downconv_block, n_filters, kernel_size, **kwargs):
        super(TransConvBlock, self).__init__(**kwargs)

        self.n_filters = n_filters
        self.kernel_size = kernel_size
        self.downconv_block = downconv_block

    def call(self, x):
        x = Conv3DTranspose(
            self.n_filters,
            (self.kernel_size, self.kernel_size, self.kernel_size),
            strides=(2, 2, 2),
            padding="same",
        )(x)
        return concatenate([x, self.downconv_block])
