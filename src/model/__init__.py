from .unet_model import get_unet
from tensorflow.keras import Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from pathlib import Path

class SemSegModelWrapper:
    def __init__(self):
        self.model = get_unet(Input(shape=(512, 512, 512, 1), batch_size=8, name="X_voxel_grid"), 5)

    def train_model(self, train_gen, val_gen, checkpoints_dir, epochs):
        self.model.compile(optimizer=Adam(), loss="binary_crossentropy")

        checkpoints_path = Path(checkpoints_dir)
        checkpoints_callback = ModelCheckpoint(
            filepath = checkpoints_dir,
            save_weights_only=True,
            save_best_only=True,
        )
        
        if checkpoints_path.exists():
            files_list = list(checkpoints_path.glob())
            if len(files_list) != 0:
                self.model.load_weights(str(checkpoints_path / files_list[0]))

        self.model.fit(
            train_gen,
            callbacks=[checkpoints_callback],
            epochs=epochs,
            validation_data=val_gen
        )