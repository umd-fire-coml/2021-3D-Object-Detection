from pathlib import Path
import re

def filter_by_ext(data_folder, ext):
    return list(map(str, filter(lambda file: len(file.suffixes) > 0 and file.suffixes[0] == ext, Path(data_folder).rglob('*'))))

def filter_many_by_ext(data_folder, exts):
    return (filter_by_ext(data_folder, ext) for ext in exts)

file_matcher_re = re.compile('.+sequences/(\d+)/(?:velodyne|labels)/(\d+)\.(?:bin|label)')
def tuple_rep(filename):
    return file_matcher_re.findall(filename)[0]

def tuple_reps(velodyne_files, label_files):
    vel_tups = set([tuple_rep(filename) for filename in velodyne_files])
    label_tups = set([tuple_rep(filename) for filename in label_files])

    return vel_tups.intersection(label_tups)

def path_fmt_string(file_path):
    """
    Given a label or velodyne file's full path, returns a format string that 
    can be used to rebuild the paths from the tuple representations.
    """
    return re.sub('(\d+)|(labels|velodyne)|(\.bin|\.label)', "{}", file_path)

def build_xy_filenames(data_folder):
    """
    Puts all of these functions together to build a filtered and 
    aligned list of x and y filenames.
    """
    init_x, init_y = filter_many_by_ext(data_folder, ('.bin', '.label'))
    fmt_string = path_fmt_string(init_x[0])

    data_tups = tuple_reps(init_x, init_y)

    x_filenames = [fmt_string.format(tup[0], 'velodyne', tup[1], '.bin') for tup in data_tups]
    y_filenames = [fmt_string.format(tup[0], 'labels', tup[1], '.label') for tup in data_tups]

    return x_filenames, y_filenames
