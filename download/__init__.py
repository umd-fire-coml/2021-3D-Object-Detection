from download.accelerator import DownloadAccelerator

def download_all_datasets():
    datasets = {
        "data/temp_storage/lsvm_baseline.zip": "https://s3.eu-central-1.amazonaws.com/avg-kitti/models_lsvm.zip",
        "data/temp_storage/training_labels.zip": "https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_label_2.zip",
        "data/temp_storage/object_development_kit.zip": "https://s3.eu-central-1.amazonaws.com/avg-kitti/devkit_object.zip",
        "data/temp_storage/velodyne.zip": "https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_velodyne.zip"
    }

    for output, link in datasets.items():
        accelerator = DownloadAccelerator(link, output)
        accelerator.start()
