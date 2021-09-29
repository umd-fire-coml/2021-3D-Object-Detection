import os
import pytest
from src.getLabels import  getLabelsForOneImage

def test_label_amount():
    fileName = os.getcwd()
    fileName = os.path.join(fileName, "notebooks/data/label_2")
    count = 0
    labels = getLabelsForOneImage(fileName, "000043.txt")
    
    for label in labels:
        count = count + 1
    assert(count == 7)

#Note this is just a very basic test, I will add more
#extensive tests in the next couple of days
