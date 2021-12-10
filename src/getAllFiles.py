import os


    
def getAllFiles(Folder, extension):
    result = []

    for path, subdirs, files in os.walk(Folder):
        
        for name in files:
            if(name.endswith(extension)):
                result.append(os.path.join(path,name))
                print(name)

    return result
