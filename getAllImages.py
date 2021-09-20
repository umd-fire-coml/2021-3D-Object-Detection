import os


def getAllImages(imageFolder):
    images = []

    for path, subdirs, files in os.walk(imageFolder):
        for name in files:
            images.append(os.path.join(path,name))

    
    



    return images