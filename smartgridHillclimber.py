import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from code.classes.house import House
from code.classes.battery import Battery
from random import shuffle
import itertools
from itertools import zip_longest
import csv
from datetime import datetime
from visualize import Visualize


"""
initialising variables, filling when better smartgrid is found
optimalorder for best sequence in list_houses, optimallength for best cabledistance
"""
optimalorder= []
optimallength = 0
lengths = []
besttotal = 0

# initialising counter for comparing
count = 0

class SmartGrid():

    def __init__(self):
        self.batteries = self.load_batteries()
        self.houses = self.load_houses()
        self.connecting = self.connecting()
        #self.visualize = self.visualize_grid()


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
        global besttotal

        # change order of array list_houses
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

        # hill climber implementation
        house = self.houses[0]
        besttotal = house.total(self.houses, self.batteries)
        for i in range(149):

            house_one = self.houses[i]
            house_two = self.houses[i + 1]
            index_one = int(house_one.get_batteryId())
            index_two = int(house_two.get_batteryId())
            battery_one = self.batteries[index_one]
            battery_two = self.batteries[index_two]

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
                    newtotal = house.total(self.houses, self.batteries)

                    # check for better result
                    if (besttotal > newtotal):
                        print("old: ", besttotal)
                        besttotal = newtotal
                        print("new: ", besttotal)
                    else:
                        battery_one.change_batteryId(house_one, house_two,
                         index_one, index_two)
                        capacities = battery_one.change_capacity(
                         battery_one, battery_two, house_two, house_one)

        return besttotal

    # method that visualizes the grids
    def visualize_grid(self):

        list_houses = self.houses
        list_batteries = self.batteries
        visualize_grid = Visualize(list_houses, list_batteries)

        visualize_grid.visualize_all(list_houses, list_batteries)

if __name__ == "__main__":
    start_time = datetime.now()

    for i in range(10):
        smartgrid = SmartGrid()
        lengths.append(besttotal)

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    print("best: ", min(lengths))
    print("sd: ", np.std(lengths))
    print("mean: ", np.mean(lengths))
