from io import BufferedReader
import sys
print(sys.version)

import numpy as np
import struct

def read_integer(file_pointer: BufferedReader):
    try:
        return struct.unpack('i', file_pointer.read(4))
    except Exception as e:
        return None

def convert_kitti_label(labelFilePath):
    list = []
    with open(labelFilePath, "rb") as f:
        next_integer = read_integer(f)
        while next_integer:
            #print(next_integer)
            list.append(next_integer)
            next_integer = read_integer(f)
    return list

if __name__ == "__main__":
    list = []
    list = convert_kitti_label("data\\example_dataset\\sequences\\00\\labels\\000000.label")
    print(np.asarray(list).shape)
    print(list[1000])