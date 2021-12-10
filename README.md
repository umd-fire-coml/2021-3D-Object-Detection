# 3D Object Detection
# Product Description

This product identifies and labels 3D Objects in images of every day settings, such as cars, trees, bikes, pedestrians, etc. 

This product makes use of a UNet, which is a Convolutional Neural Network, to identify objects, given voxel data. Our product first takes point cloud data from the SemanticKITTI dataset, and converts it to voxels. For the sake of simplicity, a voxel can be described as a 3d pixel. We visualize these voxels as cubes, each cube containing spatial information in 3 dimensions.

# Model Visualizer

Link to Colab Notebook that trains the model, tests the model, and then visualizes the output of the model - https://colab.research.google.com/drive/1N3HXZgfRkDfz55EOIG3y0QOh7ADUBjaO?usp=sharing#scrollTo=pNvlnPUrTqyi

## File Directory
- `src/visualization/voxel_grid.py`: displays results as a voxel grid generated by the model.
- `src/cvtToPCDFunction.py`: converting raw data to point clouds
- `src/dataGenerator.py`: data generator
- `src/readLabels.py`: processes labels from SemanticKITTI dataset
- `src/dispPCDFile.py`: visualizes color-coded point cloud data
- `src/test_datagen.py`: tests data generator 
- `src/getLabels.py`: fetches object labels from SemanticKITTI dataset 
- `src/generator/__init__.py`: importing DataGenerator
- `src/generator/index_data.py`: indexes data by reformatting paths from the velodyne file
- `src/generator/unpack_data/labels.py`: processing raw data from SemanticKITTI
- `src/generator/unpack_data/__init__.py`: imports for labels.py
- `src/generator/unpack_data/velodyne.py`: converts raw velodyne data to point clouds
- `src/generator/data_generator.py`: creates usable voxel dataset from original SemanticKITTI and Velodyne data.
- `src/generator/preprocess_data/__init__.py`: builds voxel grid based on object labels
- `src/getAllFiles.py`: shows all files in directory
- `src/model/__init__.py`: initializing and printing information about model status.
- `src/model/unet_model.py`: UNet Convolutional Neural Network.
- `src/model/conv_blocks/down_conv.py`: Down Convolutional Layer 
- `src/model/conv_blocks/__init__.py`: importing down_conv and trans_conv layers
- `src/model/conv_blocks/trans_conv.py`: Transposed Convolutional Layer
- `src/__main__.py`: master script - handles model training+demo, also data download and environment setup.
- `src/visualization/__init__.py`: Registers `visualization` as a module.
- `src/visualization/voxel_grid.py`: Displays model predictions from voxel grid.
- 
# Downloading the Dataset
```
#!/bin/bash
if [ ! -d "data/sequences" ]; then
    wget -c "https://s3.eu-central-1.amazonaws.com/avg-kitti/data_odometry_velodyne.zip"
    unzip data_odometry_velodyne.zip -d data
    wget -c "https://s3.eu-central-1.amazonaws.com/avg-kitti/data_odometry_calib.zip"
    unzip data_odometry_calib.zip -d data
    wget -c "http://www.semantic-kitti.org/assets/data_odometry_labels.zip"
    unzip data_odometry_labels.zip -d data

else
    echo "Directory data/sequences already exists, so there is no need to download anything else."
fi
```

# Setting Up The Environment
```
#!/bin/bash
echo "Setting up environment"
echo "Getting rid of any existing venv folder"
rm -rf venv
echo "Creating a new virtual environment"
python3 -m venv venv
echo "Activating that virtual environment"
. venv/bin/activate
echo "Installing all dependencies"
pip3 install -r requirements.txt
echo "Done! Note that you still have to activate the virtualenv before using it. Use 'source venv/bin/activate'."
```

# Citations
J. Behley, A. Milioto, C. Stachniss, M. Garbade, J. Gall, J. Quenzel, and S. Behnke, “Semantic Kitti Dataset Overview,” Semantickitti - A dataset for LIDAR-based Semantic Scene Understanding, 2020. [Online]. Available: http://www.semantic-kitti.org/dataset.html. [Accessed: 08-Dec-2021].
