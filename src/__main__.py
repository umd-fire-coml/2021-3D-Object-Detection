# from .generator.data_generator import DataGenerator
# from .model import SemSegModelWrapper
import sys
import os

def parse_setup_environment(args):
    assert len(args) == 0, "Did not expect any arguments after setup-env"
    os.system('. scripts/setup-environment.sh')

def parse_download_data(args):
    assert len(args) == 0, "Did not expect any arguments after dl-data"
    os.system('./scripts/download-data.sh')

def parse_train_model(args):
    assert len(args) >= 2, "Expected a dataset directory and a checkpoints file, in that order."
    dataset_dir, checkpoints_dir = args.pop(0), args.pop(0)

    try:
        epochs = int(args.pop(0))
    except Exception as e:
        epochs = 10

    try:
        dim = int(args.pop(0))
    except Exception as e:
        dim = 256

    print(f'Using dataset directory {dataset_dir} and checkpoints file {checkpoints_dir}')
    print(f"Going to run for {epochs} epochs.")
    print(f"Using voxel grid dimension {dim}")

    print("Now importing the generator and model code. This could take a while if it's the first time, as it needs to byte-compile.")
    from .generator.data_generator import DataGenerator
    from .model import SemSegModelWrapper

    train_gen, val_gen = DataGenerator.create_train_val_generators(dataset_dir, voxel_grid_dim=dim, batch_size=1)
    model_wrapper = SemSegModelWrapper(voxel_dim=dim, batch_size=1)
    model_wrapper.train_model(train_gen, val_gen, checkpoints_dir, epochs)

def parse_demo_model(args):
    assert len(args) == 3, "Expected dataset directory, checkpoint file, and voxel grid dimension, in that order."
    
    dataset, checkpoint, voxel_grid_dim  = args.pop(0), args.pop(0), int(args.pop(0))
    print(f"Using dataset directory {dataset} and checkpoint file {checkpoint}.")

    print("Now importing the generator and model code. This could take a while if it's the first time, as it needs to byte-compile.")
    from .generator.data_generator import DataGenerator
    from .model import SemSegModelWrapper

    train_gen, val_gen = DataGenerator.create_train_val_generators(dataset, voxel_grid_dim=voxel_grid_dim)
    model_wrapper = SemSegModelWrapper(voxel_dim=voxel_grid_dim)
    model_wrapper.demo_model(val_gen, checkpoint)

def parse_arguments(args):
    args.pop(0)
    
    assert len(args) > 0, "Expected arguments. Read the documentation."
    next_argument = args.pop(0)

    if next_argument == "setup-env":
        parse_setup_environment(args)
    elif next_argument == "dl-data":
        parse_download_data(args)
    elif next_argument == "train-model":
        parse_train_model(args)
    elif next_argument == "demo-model":
        parse_demo_model(args)
    else:
        print(f"Expected the first argument to be one of (setup-env|dl-data|train-model). Instead, got {next_argument}")

parse_arguments(sys.argv.copy())

# model = SemSegModelWrapper()
# generator = DataGenerator()
# model.train_model(generator)