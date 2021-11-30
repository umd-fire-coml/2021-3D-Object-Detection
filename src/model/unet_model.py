from tensorflow.keras.layers import MaxPooling3D, Dropout
from tensorflow.python.keras.engine.training import Model
from tensorflow.python.keras.layers.convolutional import Conv3D

from .conv_blocks import DownConvBlock, TransConvBlock

from tensorflow.keras.models import Sequential


def get_unet(x, n_blocks, n_filters=16, dropout=0.1):
    # Contracting Path
    C = [DownConvBlock(n_filters, 3)(x)]
    P = []

    for i in range(1, n_blocks + 2):
        P.append(Dropout(dropout)(MaxPooling3D()(C[-1])))
        C.append(DownConvBlock((n_filters * i ** 2), 3)(P[-1]))

    U = []
    for i in range(n_blocks, 0, -1):
        print(i, flush=True)
        U.append(
            Dropout(dropout)(TransConvBlock(C[i], n_filters * i ** 2, 3)(C[-1]))
        )
        C.append(DownConvBlock((n_filters * i ** 2), 3)(U[-1]))

    outputs = Conv3D(1, (1, 1, 1))(C[-1])

    return Model(inputs=[x], outputs=[outputs])
