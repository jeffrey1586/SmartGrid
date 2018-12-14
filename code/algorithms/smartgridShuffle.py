# add the current structure with path
import os, sys
directory = os.path.dirname(os.path.realpath("algorithms"))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))

from battery import Battery
from datetime import datetime
from house import House
from itertools import zip_longest
from matplotlib.collections import LineCollection
from random import shuffle
from visualize import Visualize
import csv
import itertools
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle


"""
This class generates smartgrids with a shuffle algorithm.
"""
count = 0
optimalorder= []
lengths = []
optimallength = 0
total_length = 0

class SmartGridShuffle():

    def __init__(self):
        self.batteries = self.load_batteries()
        self.houses = self.load_houses()
        self.connecting = self.connecting()
        if count == 500000:
            self.visualize = self.visualize_grid()


    # load method for Batteries
    def load_batteries(self):

        # reading the battery file
        batteryfile= open("data/wijk2_batterijen.txt", "r")
        list_batteries = []

        # making battery instances and adding to list
        counter = 0
        for line in batteryfile:
            if counter != 0:
                check = line.split()
                x_value = check[0].strip('[').strip(',')
                y_value = check[1].strip(']')
                capacity = check[2]
                list_batteries.append(Battery(x_value, y_value, capacity))
            counter = 1
        return list_batteries

    # load method for Houses
    def load_houses(self):

        # reading the house file
        housefile= open("data/wijk2_huizen.csv", "r")
        list_houses = []
        counter = 0
        id = 1

        # making house instances and adding to list
        for line in housefile:
            if counter != 0:
                values = line.split(",")
                x_value = values[0]
                y_value = values[1]
                output = values[2]
                new_house = House(id, x_value, y_value, output, 0)
                list_houses.append(new_house)
                id += 1
            counter = 1
        return list_houses

    # method that connects houses with batteries
    def connecting(self):

        global count
        global optimalorder
        global optimallength
        global total_length

        # shuffle order of array list_houses
        shuffle(self.houses)
        for house in self.houses:

            # calculate length to closest battery
            all_distances = house.calculate_all(house, self.batteries)

            # calculate length to closest battery
            min_distance = house.calculate_min(all_distances[0])

            # adjusting battery capacity and checking for overload
            index_battery = house.check_capacity(all_distances[0], min_distance, all_distances[1], self.batteries)

            # add the batterynumber to houseobject
            house.set_batteryId(index_battery[0])

        # calculate total length
        total_length = house.total(self.houses, self.batteries)

        # saving initial list order and optimal length
        if count == 0:
            optimalorder = self.houses
            optimallength = total_length

        # saving the better list order and optimal length
        else:
            if optimallength > total_length:
                optimallength = total_length
                optimalorder = self.houses
        count += 1

        #writing total_length value to csv
        pickle.dump(total_length, open( "resultaten/pickledata.p", "wb" ))
        pickle_total_length = pickle.load( open ( "resultaten/pickledata.p", "rb" ))
        lengths.append(total_length)

        return total_length

    # method that visualizes the grids
    def visualize_grid(self):

        # get list of houses and batteries, and visualize the grid
        list_houses = optimalorder
        list_batteries = self.batteries
        visualize_grid = Visualize(list_houses, list_batteries)
        visualize_grid.visualize_all(list_houses, list_batteries, optimallength)

        # print the best and worst score, standard deviation and mean
        print("best: ", min(lengths))
        print("worst: ", max(lengths))
        print("sd: ", np.std(lengths))
        print("mean: ", np.mean(lengths))

        # plot a histogram with the score (x-axis) and count (y-axis)
        unique_lengths = set(lengths)
        count_unique = len(unique_lengths)
        bins = np.linspace(math.ceil(min(lengths)),
                       math.floor(max(lengths)), count_unique)
        plt.xlim([min(lengths), max(lengths)])
        plt.hist(lengths, bins=bins, alpha=1)
        plt.title('Shuffle algorithm (iteraties: 500 000)')
        plt.xlabel('Score')
        plt.ylabel('Aantal per score')
        plt.show()
