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

def extract_labels(input_integer):
    input_integer = input_integer[0]

    high_mask = 4294901760
    low_mask = 65535

    high_data = (input_integer & high_mask) >> 16
    low_data = input_integer & low_mask

    return high_data, low_data

def convert_all_kitti(labelFilePath):
    integers = []
    with open(labelFilePath, "rb") as f:
        next_integer = read_integer(f)
        while next_integer:
            integers.append(next_integer)
            next_integer = read_integer(f)

    return map(extract_labels, integers)

def return_lower_labels(list):
    lower = []
    for value in list:
        high, low = value
        lower.append(low)

    return lower


# def convert_kitti_label(labelFilePath):
#     list = []
#     with open(labelFilePath, "rb") as f:
#         next_integer = read_integer(f)
#         while next_integer:
#             print(next_integer[0])
#             list.append(next_integer)
#             next_integer = read_integer(f)
#     return list

# if __name__ == "__main__":
#     list = []
#     filename = "data\\example_dataset\\sequences\\00\\labels\\"
#     list_of_unique_ids = [] 
#     list_of_lower = []

#     for x in range(0,24):
#         newFileName = filename + f'{x:06d}' + ".label"
#         print("Processing: {}".format(newFileName))
#         list = convert_all_kitti(newFileName)
#         for value in list:
#             high, low = value
#             if high > 0:
#                 if not high in list_of_unique_ids:
#                     list_of_unique_ids.append(high)
#             if low > 0:
#                 if not low in list_of_lower:
#                     list_of_lower.append(low)
#     print("Higher values:")
#     list_of_unique_ids.sort()
#     list_of_lower.sort
#     for value in list_of_unique_ids:
#         print(value)
#     list = convert_all_kitti("data\\example_dataset\\sequences\\00\\labels\\000000.label")
#     print("\nLower values:")
#     for value in list_of_lower:
#         print(value)

#   0 : "unlabeled"
#   1 : "outlier"
#   10: "car"
#   11: "bicycle"
#   13: "bus"
#   15: "motorcycle"
#   16: "on-rails"
#   18: "truck"
#   20: "other-vehicle"
#   30: "person"
#   31: "bicyclist"
#   32: "motorcyclist"
#   40: "road"
#   44: "parking"
#   48: "sidewalk"
#   49: "other-ground"
#   50: "building"
#   51: "fence"
#   52: "other-structure"
#   60: "lane-marking"
#   70: "vegetation"
#   71: "trunk"
#   72: "terrain"
#   80: "pole"
#   81: "traffic-sign"
#   99: "other-object"
#   252: "moving-car"
#   253: "moving-bicyclist"
#   254: "moving-person"
#   255: "moving-motorcyclist"
#   256: "moving-on-rails"
#   257: "moving-bus"
#   258: "moving-truck"
#   259: "moving-other-vehicle"