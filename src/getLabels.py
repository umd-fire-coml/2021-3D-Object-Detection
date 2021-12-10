import os

def getLabelsForOneImage(fileName, labelTextFile):
    cars, pedestrians, cyclists,  vans, trucks, miscs, dontCare, labels = [],[],[],[],[],[],[],[]

    dataPath = os.path.join(fileName, labelTextFile)


    with open(dataPath, "r") as a_file:
        for line in a_file:
            data = (line.strip()).split()
            if(data[0] == "Pedestrian"):
                pedestrians.append(tuple(data[1:]))
            if(data[0] == "Car"):
                cars.append(tuple(data[1:]))
            if(data[0] == "Cyclist"):
                cyclists.append(tuple(data[1:]))
            if(data[0] == "Van"):
                vans.append(tuple(data[1:]))
            if(data[0] == "Truck"):
                trucks.append(tuple(data[1:]))
            if(data[0] == "Misc"):
                miscs.append(tuple(data[1:]))
            if(data[0] == "DontCare"):
                dontCare.append(tuple(data[1:]))
    
    labels.append(cars)
    labels.append(pedestrians)
    labels.append(cyclists)
    labels.append(vans)
    labels.append(trucks)
    labels.append(miscs)
    labels.append(dontCare)

    return labels
    
            