# from .generator.data_generator import DataGenerator
# from .model import SemSegModelWrapper
import sys
import os

def parse_setup_environment():
    assert len(sys.argv) == 0, "Did not expect any arguments after setup-env"
    os.system('. scripts/setup-environment.sh')

def parse_download_data():
    assert len(sys.argv) == 0, "Did not expect any arguments after dl-data"
    os.system('./scripts/download-data.sh')

def parse_train_model():
    assert len(sys.argv) >= 2, "Expected a dataset directory and a checkpoints directory, in that order."
    dataset_dir, checkpoints_dir = sys.argv.pop(0), sys.argv.pop(0)

    try:
        epochs = int(sys.argv.pop(0))
    except Exception as e:
        epochs = 10

    print(f'Using dataset directory {dataset_dir} and checkpoints directory {checkpoints_dir}')
    print(f"Going to run for {epochs} epochs.")

    from .generator.data_generator import DataGenerator
    from .model import SemSegModelWrapper

    train_gen, val_gen = DataGenerator(dataset_dir)
    model_wrapper = SemSegModelWrapper()
    model_wrapper.train_model(train_gen, val_gen, checkpoints_dir, epochs)

def parse_arguments():
    sys.argv.pop(0)
    assert len(sys.argv) > 0, "Expected arguments. Read the documentation."

    next_argument = sys.argv.pop(0)
    if next_argument == "setup-env":
        parse_setup_environment()
    elif next_argument == "dl-data":
        parse_download_data()
    elif next_argument == "train-model":
        parse_train_model()
    else:
        print("Expected the first argument to be one of (setup-env|dl-data|).")

parse_arguments()

# model = SemSegModelWrapper()
# generator = DataGenerator()
# model.train_model(generator)