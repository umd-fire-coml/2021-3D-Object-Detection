import os
from getAllFiles import getAllFiles

from dataGenerator import DataGenerator



mydatagen = DataGenerator()
newlist = []
newlist = getAllFiles('C:\\Users\\fpras\\FIRE298\\2021-3D-Object-Detection\\data\\example_dataset\\sequences\\00\\velodyne', ".bin")
print(len(newlist))
print("initialized")


print(len(mydatagen.x_filepaths))

x = []
y = []
x, y = mydatagen.__getitem__(1)


for i in mydatagen.x_filepaths:
    print(i)

print(x.shape)
print(y.shape)
