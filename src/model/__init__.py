from .unet_model import get_unet
from tensorflow.keras import Input
from tensorflow.keras.optimizers import Adam

class SemSegModelWrapper:
    def __init__(self):
        self.model = get_unet(Input(shape=(512, 512, 512, 1), batch_size=8, name="X_voxel_grid"), 5)

    def train_model(self, generator):
        self.model.compile(optimizer=Adam(), loss="binary_crossentropy")
        self.model.fit(generator)