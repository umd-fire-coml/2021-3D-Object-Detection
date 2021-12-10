from io import BufferedReader

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
    return [value[1] for value in list]

def unpack_labels(label_file_path):
    return return_lower_labels(convert_all_kitti(label_file_path))