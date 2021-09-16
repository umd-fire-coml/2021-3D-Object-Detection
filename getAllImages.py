import os


def getAllImages(imageFolder):
    images = []
    for file in os.listdir(imageFolder):
        if file.endswith(".jpg"): # might need to change depending on format of images
            images.append(os.path.join(imageFolder,file))

    return images