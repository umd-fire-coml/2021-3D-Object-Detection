import os
import pathlib
import sys
sys.path.insert(0, './src')

from  src.getAllImagesFunction import getAllImages


imageFolder = r"\getAllImagesFolder" #folder with all the images

imageFolderPath = os.getcwd()+ imageFolder
imageFolderPath.encode('unicode_escape')

print (imageFolderPath)

images = getAllImages(imageFolderPath)

imagesRel = []

for image in images:
    image = os.path.relpath(image, imageFolderPath)
    imagesRel.append(image)

    
print(len(imagesRel))
assert len(imagesRel) == 0
assert True

