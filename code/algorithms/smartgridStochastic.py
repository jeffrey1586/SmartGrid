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
import random

"""
initialising variables, filling when better smartgrid is found
optimalorder for best sequence in list_houses, optimallength for best cabledistance
"""

lengths = []
total = 0

class SmartGridStochastic():

    def __init__(self):
        self.batteries = self.load_batteries()
        self.houses = self.load_houses()
        self.connecting = self.connecting()
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

        global total

        # change order of array list_houses
        shuffle(self.houses)
        for house in self.houses:

            # calculate length to closest battery
            all_distances = house.calculate_all(house, self.batteries)

            # calculate length to closest battery
            min_distance = house.calculate_min(all_distances[0])

            # adjusting battery capacity and checking for overload
            index_battery = house.check_capacity(all_distances[0], min_distance,
             all_distances[1], self.batteries)

            # add the batterynumber to houseobject
            house.set_batteryId(index_battery[0])

        # Stochastic hill climber implementation
        house = self.houses[0]
        for i in range(1000):
            j = random.randint(0,149)
            k = random.randint(0,149)
            house_one = self.houses[j]
            house_two = self.houses[k]
            index_one = int(house_one.get_batteryId())
            index_two = int(house_two.get_batteryId())
            battery_one = self.batteries[index_one]
            battery_two = self.batteries[index_two]

            old_total = house.local_length(house_one, house_two,
             self.batteries)

            # check if houses are connected to same battery
            if (index_one != index_two):
                capacities = battery_one.change_capacity(battery_one,
                 battery_two, house_one, house_two)
                cap_one = capacities[0]
                cap_two = capacities[1]

                # checking if capacities are exceeded
                if (cap_one < 0 or cap_two < 0):
                    capacities = battery_one.change_capacity(battery_one,
                    battery_two, house_two, house_one)

                # swap connections
                else:
                    battery_one.change_batteryId(house_one, house_two,
                     index_two, index_one)
                    new_total = house.local_length(house_one,
                     house_two, self.batteries)

                    # check for better result
                    if (old_total < new_total):
                        battery_one.change_batteryId(house_one, house_two,
                         index_one, index_two)

                        capacities = battery_one.change_capacity(
                        battery_one, battery_two, house_two, house_one)

        total = house.total(self.houses, self.batteries)
        lengths.append(total)
        return total

    # method that visualizes the grids
    def visualize_grid(self):

        list_houses = self.houses
        list_batteries = self.batteries
        visualize_grid = Visualize(list_houses, list_batteries)

        visualize_grid.visualize_all(list_houses, list_batteries, total)

        # standard deviation and mean
        print("best: ", min(lengths))
        print("worst: ", max(lengths))
        print("sd: ", np.std(lengths))
        print("mean: ", np.mean(lengths))

        unique_lengths = set(lengths)
        count_unique = len(unique_lengths)

        bins = np.linspace(math.ceil(min(lengths)),
                       math.floor(max(lengths)),
                       count_unique)

        plt.xlim([min(lengths), max(lengths)])

        plt.hist(lengths, bins=bins, alpha=1)
        plt.title('Shuffle algorithm (iteraties: 500 000)')
        plt.xlabel('Score')
        plt.ylabel('Aantal per score')

        plt.show()
