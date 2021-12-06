from .generator.data_generator import DataGenerator
from .model import SemSegModelWrapper

model = SemSegModelWrapper()
generator = DataGenerator()
model.train_model(generator)