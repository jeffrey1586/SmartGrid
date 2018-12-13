from code.algorithms.smartgridBattery import SmartGridBattery
from code.algorithms.smartgridHillclimber import SmartGridHillclimber
from code.algorithms.smartgridHouse import SmartGridHouse
from code.algorithms.smartgridRelocation import SmartGridRelocation
from code.algorithms.smartgridSteepest import SmartGridSteepest
from code.algorithms.smartgridStochastic import SmartGridStochastic
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.visualize import Visualize
from datetime import datetime
from itertools import zip_longest
from matplotlib.collections import LineCollection
from random import shuffle
import csv
import itertools
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

def main():
    start_time = datetime.now()

    for i in range(500000):
        SmartGridHouse()
        if i == 499998:
            end_time = datetime.now()
            print('Duration: {}'.format(end_time - start_time))


if __name__ == "__main__":
    main()
