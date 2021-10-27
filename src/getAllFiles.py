import os


    
def getAllFiles(Folder, extension):
    files = []

    for path, subdirs, files in os.walk(Folder):
        for name in files:
            if(name.endswith(extension)):
                files.append(os.path.join(path,name))

    return files
