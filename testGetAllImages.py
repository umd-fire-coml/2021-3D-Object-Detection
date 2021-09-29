from src.getAllImagesFunction import *
import os


imageFolder = "\data_test_getAllImages" #folder with all the images

imageFolderPath = os.getcwd()+ imageFolder
imageFolderPath.encode('unicode_escape')

#print (imageFolderPath)

images = getAllImages(imageFolderPath)

imagesRel = []

for image in images:
    image = os.path.relpath(image, imageFolderPath)
    imagesRel.append(image)

    


print(imagesRel)
