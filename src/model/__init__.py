from .unet_model import get_unet
from tensorflow.keras import Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from pathlib import Path
from tensorflow.keras.losses import SparseCategoricalCrossentropy
import numpy as np

class SemSegModelWrapper:
    def __init__(self, batch_size, voxel_dim):
        print("Constructing UNet")
        self.model = get_unet(Input(shape=(voxel_dim, voxel_dim, voxel_dim, 1), batch_size=batch_size, name="X_voxel_grid"), 5)
        print("Done constructing UNet")

    def train_model(self, train_gen, val_gen, checkpoints_file, epochs):
        print("Compiling model")
        self.model.compile(
            loss=SparseCategoricalCrossentropy(from_logits=False),
            metrics=['sparse_categorical_accuracy']
        )

        checkpoints_callback = ModelCheckpoint(
            filepath = checkpoints_file,
            save_weights_only=True,
            save_best_only=True,
        )
        
        checkpoints_path = Path(checkpoints_file)
        if checkpoints_path.exists():
            print(f"Found existing checkpoints file at {checkpoints_file}")
            self.model.load_weights(str(checkpoints_path))

        self.model.fit(
            train_gen,
            callbacks=[checkpoints_callback],
            epochs=epochs,
            validation_data=val_gen,
            steps_per_epoch=10
        )

    def predict(self, data_point, checkpoint):
        print("Compiling model.")
        self.model.compile(optimizer=Adam(), loss="categorical_crossentropy")

        print("Loading weights from the checkpoint file.")
        assert Path(checkpoint).exists(), f"The checkpoint file {checkpoint} was not found."
        self.model.load_weights(checkpoint)

        return np.argmax(self.model.predict(data_point).squeeze(), axis=3)