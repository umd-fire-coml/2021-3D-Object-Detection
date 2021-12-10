from tensorflow.keras.layers import MaxPooling3D, Dropout, BatchNormalization, Activation
from tensorflow.keras.layers import Conv3D
from tensorflow.keras.models import Model

from tensorflow.python.keras.layers.convolutional import Conv3DTranspose
from tensorflow.python.keras.layers.merge import concatenate

# tf.compat.v1.disable_eager_execution()


def conv3d_block(input_tensor, n_filters, kernel_size = 3, batchnorm = True):
    """Function to add 2 convolutional layers with the parameters passed to it"""
    # first layer
    x = Conv3D(filters = n_filters, kernel_size = (kernel_size, kernel_size, kernel_size),\
              kernel_initializer = 'he_normal', padding = 'same')(input_tensor)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    """Function to add 2 convolutional layers with the parameters passed to it"""
    # first layer
    x = Conv3D(filters = n_filters, kernel_size = (kernel_size, kernel_size, kernel_size),\
              kernel_initializer = 'he_normal', padding = 'same')(input_tensor)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    
    return x
  
def get_unet(input_img, n_filters = 16, dropout = 0.1, batchnorm = True):
    # Contracting Path
    c1 = conv3d_block(input_img, n_filters * 1, kernel_size = 3, batchnorm = batchnorm)
    p1 = MaxPooling3D()(c1)
    p1 = Dropout(dropout)(p1)

    c2 = conv3d_block(p1, n_filters * 2, kernel_size = 3, batchnorm = batchnorm)
    p2 = MaxPooling3D()(c2)
    p2 = Dropout(dropout)(p2)
    
    c3 = conv3d_block(p2, n_filters * 4, kernel_size = 3, batchnorm = batchnorm)
    p3 = MaxPooling3D()(c3)
    p3 = Dropout(dropout)(p3)
    
    c4 = conv3d_block(p3, n_filters * 8, kernel_size = 3, batchnorm = batchnorm)
    p4 = MaxPooling3D()(c4)
    p4 = Dropout(dropout)(p4)
    
    c5 = conv3d_block(p4, n_filters = n_filters * 16, kernel_size = 3, batchnorm = batchnorm)
    
    # Expansive Path
    u6 = Conv3DTranspose(n_filters * 8, (3, 3, 3), strides = (2, 2, 2), padding = 'same')(c5)
    u6 = concatenate([u6, c4])
    u6 = Dropout(dropout)(u6)
    c6 = conv3d_block(u6, n_filters * 8, kernel_size = 3, batchnorm = batchnorm)
    
    u7 = Conv3DTranspose(n_filters * 4, (3, 3, 3), strides = (2, 2, 2), padding = 'same')(c6)
    u7 = concatenate([u7, c3])
    u7 = Dropout(dropout)(u7)
    c7 = conv3d_block(u7, n_filters * 4, kernel_size = 3, batchnorm = batchnorm)
    
    u8 = Conv3DTranspose(n_filters * 2, (3, 3, 3), strides = (2, 2, 2), padding = 'same')(c7)
    u8 = concatenate([u8, c2])
    u8 = Dropout(dropout)(u8)
    c8 = conv3d_block(u8, n_filters * 2, kernel_size = 3, batchnorm = batchnorm)
    
    u9 = Conv3DTranspose(n_filters * 1, (3, 3, 3), strides = (2, 2, 2), padding = 'same')(c8)
    u9 = concatenate([u9, c1])
    u9 = Dropout(dropout)(u9)
    c9 = conv3d_block(u9, n_filters * 1, kernel_size = 3, batchnorm = batchnorm)
    
    outputs = Conv3D(34, (1, 1, 1), activation="sigmoid")(c9)
    model = Model(inputs=[input_img], outputs=[outputs])
    return model

# def get_unet(x, n_blocks, n_filters=16, dropout=0.1):
#     # Contracting Path
#     C = []
#     curr_f = x

#     for i in range(0, n_blocks):
#         curr_f = DownConvBlock((n_filters * (2**i)), 3)(curr_f)
#         C.append(curr_f)
#         curr_f = Dropout(dropout)(MaxPooling3D()(curr_f))

#     curr_f = DownConvBlock((n_filters * (2**(n_blocks + 1))), 3)(curr_f)

#     for i in range(n_blocks - 1, -1, -1):
#         curr_f = Dropout(dropout)(
#             TransConvBlock(C[i], n_filters * (2**i), 3)(curr_f)
#         )
#         curr_f = DownConvBlock(n_filters * (2**i), 3)(curr_f)

#     outputs = Conv3D(1, (1, 1, 1))(curr_f)

#     return Model(inputs=[x], outputs=[outputs])
