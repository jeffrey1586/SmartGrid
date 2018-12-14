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
This class generates smartgrids with a steepest ascent hill climber.
"""
optimalorder= []
optimallength = 0
lengths = []
total_length = 0
optimal = []
besttotal = 0

# initialising counter for comparing
count = 0

class SmartGridSteepest():

    def __init__(self):
        self.batteries = self.load_batteries()
        self.houses = self.load_houses()
        self.connecting = self.connecting()
        self.visualize = self.visualize_grid()

    # load method for Batteries
    def load_batteries(self):

        # reading the battery file
        batteryfile= open("data/wijk1_batterijen.txt", "r")
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
        housefile= open("data/wijk1_huizen.csv", "r")
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
        global optimal
        global besttotal

        # change order of array list_houses
        shuffle(self.houses)
        # total_length = 0
        for house in self.houses:

            # calculate length to closest battery
            all_distances = house.calculate_all(house, self.batteries)

            # calculate length to closest battery
            min_distance = house.calculate_min(all_distances[0])

            # adjusting battery capacity and checking for overload
            index_battery = house.check_capacity(all_distances[0], min_distance, all_distances[1], self.batteries)

            # add the batterynumber to houseobject
            house.set_batteryId(index_battery[0])

        # # This can be used if shuffle needs to be itterated more than once
        # # saving initial list order and optimal length
        # if count == 0:
        #     optimalorder = self.houses
        #     optimallength = total_length
        #     print(optimallength)
        #
        # # saving the better list order and optimal length
        # elif count > 0 and count < 1000:
        #     if optimallength < total_length:
        #         optimallength = total_length
        #         optimalorder = self.houses
        #         print(optimallength)
        # count += 1

        if count == 0:
            # Steepest-ascent hill climber implementation
            # optimal = optimalorder
            optimal = self.houses
            house = optimal[0]
            besttotal = house.total(optimal, self.batteries)
            for i in range(100):
                j = random.randint(0,149)
                house_one = optimal[j]
                index_one = int(house_one.get_batteryId())
                battery_one = self.batteries[index_one]
                swap_distances = {}

                for house_two in optimal:
                    index_two = int(house_two.get_batteryId())
                    battery_two = self.batteries[index_two]

                    # check if houses are connected to same battery
                    if (index_two != index_two):
                        capacities = battery_one.change_capacity(battery_one,
                         battery_two, house_one, house_two)
                        cap_one = capacities[0]
                        cap_two = capacities[1]

                        # checking if capacities are exceeded
                        if (cap_one < 0 or cap_two < 0):
                            capacities = battery_one.change_capacity(
                            battery_one, battery_two, house_two, house_one)

                        # swap the connections
                        else:
                            battery_one.change_batteryId(house_one, house_two,
                            index_two, index_one)
                            newtotal = house.total(optimal, self.batteries)

                            # check for better result and append to list
                            if (besttotal > newtotal):
                                key_id = house_sec.get_id()
                                swap_distances[key_id] = newtotal
                                besttotal = newtotal

                            # set all changes back to initial state
                            battery_one.change_batteryId(house_one, house_two,
                             index_one, index_two)
                            capacities = battery_one.change_capacity(
                             battery_one, battery_two, house_two, house_one)

                # get best swap option
                if swap_distances != {}:
                    house_id = max(swap_distances, key=swap_distances.get)
                    house_sec = list_houses[house_id]
                    index_sec = int(house_sec.get_batteryId())
                    battery_sec = self.batteries[index_sec]

                    # make the swap between the two connections
                    battery_one.change_batteryId(house_one, house_two,
                    index_two, index_one)
                    battery_first.set_capacity(house_sec.get_output())
                    battery_sec.set_capacity(house_first.get_output())
                    print("total: ", house.total(optimal, self.batteries))

        lengths.append(besttotal)
        return besttotal

    # method that visualizes the grids
    def visualize_grid(self):

        # get list of houses and batteries, and visualize the grid
        list_houses = self.houses
        list_batteries = self.batteries
        visualize_grid = Visualize(list_houses, list_batteries)
        visualize_grid.visualize_all(list_houses, list_batteries, besttotal)

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
        plt.title('Steepest ascent algorithm (iteraties: 500 000)')
        plt.xlabel('Score')
        plt.ylabel('Aantal per score')
        plt.show()
