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
This class relocates the batteries to find a shorter total length.
"""
optimalorder= []
optimallength = 0
lengths = []
total_length = 0
relocation_length = 0
diax = 0
diay = 0

# initialising counter for comparing
count = 0

class SmartGridRelocation():

    def __init__(self):
        self.batteries = self.load_batteries()
        self.houses = self.load_houses()
        self.connecting = self.connecting()
        self.visualize = self.visualize_grid()


    # load method for Batteries
    def load_batteries(self):
        global diax
        global diay

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
        battery_change = list_batteries[0]

        battery_change.set_xval(diay)
        battery_change.set_yval(diax)
        dia += 1

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

        # change order of array list_houses
        # shuffle(self.houses)
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
            optimal = self.houses
            optimallength = total_length
            count = 1

        # saving the better list order and optimal length
        else:
            if optimallength > total_length:
                optimallength = total_length
                optimal = self.houses

        #writing total_length value to csv
        pickle.dump(total_length, open( "realtest.p", "wb" ))
        pickle_total_length = pickle.load( open ( "realtest.p", "rb" ))

        return total_length

    # method that visualizes the grids
    def visualize_grid(self):

        # get list of houses and batteries, and visualize the grid
        list_houses = self.houses
        list_batteries = self.batteries
        visualize_grid = Visualize(list_houses, list_batteries)
        visualize_grid.visualize_all(list_houses, list_batteries)
