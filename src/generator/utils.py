from pathlib import Path

def filter_by_ext(data_folder, ext):
    return list(map(str, filter(lambda file: len(file.suffixes) > 0 and file.suffixes[0] == ext, Path(data_folder).rglob('*'))))

def filter_many_by_ext(data_folder, exts):
    return (filter_by_ext(data_folder, ext) for ext in exts)