import os


def getAllImages(imageFolder):
    images = []

    for path, subdirs, files in os.walk(imageFolder):
        for name in files:

            if name.endswith(".jpg") or name.endswith(".png") or name.endswith('.jpeg'): # might need to change depending on format of images
                images.append(os.path.join(path,name))
            #print(os.path.join(path, name))
            #print(os.path.relpath(path, imageFolderPath))

    
    



    return images