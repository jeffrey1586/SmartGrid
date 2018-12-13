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
import pickle
import math

"""
initialising variables, filling when better smartgrid is found
optimalorder for best sequence in list_houses, optimallength for best cabledistance
"""
optimalorder= []
optimallength = 0
lengths = []
total_length = 0

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

        print(pickle_total_length)

        return total_length

    # method that visualizes the grids
    def visualize_grid(self):

        # setting up plots
        fig, ax = plt.subplots()

        # divide houses into lists, plot those with different colours
        aHouses = []
        bHouses = []
        cHouses = []
        dHouses = []
        eHouses = []

        for k in range(150):
            house_nmr = self.houses[k]
            x_house = int(house_nmr.get_xval())
            y_house = int(house_nmr.get_yval())
            batt = int(house_nmr.get_batteryId())

            if batt == 0:
                aHouses.append((x_house, y_house))
                xHouse = list(map(lambda x: x[0], aHouses))
                yHouse = list(map(lambda x: x[1], aHouses))
                ax.plot(xHouse, yHouse, '*', color='blue')

            elif batt == 1:
                bHouses.append((x_house, y_house))
                xHouse = list(map(lambda x: x[0], bHouses))
                yHouse = list(map(lambda x: x[1], bHouses))
                ax.plot(xHouse, yHouse, '*', color='red')

            elif batt == 2:
                cHouses.append((x_house, y_house))
                xHouse = list(map(lambda x: x[0], cHouses))
                yHouse = list(map(lambda x: x[1], cHouses))
                ax.plot(xHouse, yHouse, '*', color='purple')

            elif batt == 3:
                dHouses.append((x_house, y_house))
                xHouse = list(map(lambda x: x[0], dHouses))
                yHouse = list(map(lambda x: x[1], dHouses))
                ax.plot(xHouse, yHouse, '*', color='orange')

            elif batt == 4:
                eHouses.append((x_house, y_house))
                xHouse = list(map(lambda x: x[0], eHouses))
                yHouse = list(map(lambda x: x[1], eHouses))
                ax.plot(xHouse, yHouse, '*', color='black')

        #load in battery coordinates
        Batteries = []
        for i in range(5):
            battery_nmr = self.batteries[i]
            x_battery = int(battery_nmr.get_xval())
            y_battery = int(battery_nmr.get_yval())
            Batteries.append((x_battery, y_battery))

        # coloring batteries
        battcount = 0
        aBatteries = []
        bBatteries = []
        cBatteries = []
        dBatteries = []
        eBatteries = []

        for battery in Batteries:

            if battcount == 0:
                aBatteries.append(battery)
                # adding the batteries to the plot
                xBat = list(map(lambda x: x[0], aBatteries))
                yBat = list(map(lambda x: x[1], aBatteries))
                ax.plot(xBat, yBat, 's', color='blue', markersize=10)

            elif battcount == 1:
                bBatteries.append(battery)
                # adding the batteries to the plot
                xBat = list(map(lambda x: x[0], bBatteries))
                yBat = list(map(lambda x: x[1], bBatteries))
                ax.plot(xBat, yBat, 's', color='red', markersize=10)

            if battcount == 2:
                cBatteries.append(battery)
                # adding the batteries to the plot
                xBat = list(map(lambda x: x[0], cBatteries))
                yBat = list(map(lambda x: x[1], cBatteries))
                ax.plot(xBat, yBat, 's', color='purple', markersize=10)

            if battcount == 3:
                dBatteries.append(battery)
                # adding the batteries to the plot
                xBat = list(map(lambda x: x[0], dBatteries))
                yBat = list(map(lambda x: x[1], dBatteries))
                ax.plot(xBat, yBat, 's', color='orange', markersize=10)

            if battcount == 4:
                eBatteries.append(battery)
                # adding the batteries to the plot
                xBat = list(map(lambda x: x[0], eBatteries))
                yBat = list(map(lambda x: x[1], eBatteries))
                ax.plot(xBat, yBat, 's', color='black', markersize=10)

            battcount += 1

        # appending cables lines to lineCollection
        cables = []
        for i in range(149):
            house = self.houses[i]
            index = house.get_batteryId()
            battery_nmr = Batteries[index]
            x1 = house.get_xval()
            y1 = house.get_yval()
            x2 = battery_nmr[0]
            y2 = battery_nmr[1]
            cables.append(((x1, y1), (x1, y2)))
            cables.append(((x1, y2), (x2, y2)))

        # adding the entire collection to the grid
        ln_coll = LineCollection(cables)
        ax.add_collection(ln_coll)

        # turn on the grid
        ax.grid()

        # establish gridlines and show plot
        plt.xticks(np.arange(0, 51, 1))
        plt.yticks(np.arange(0, 51, 1))
        plt.title("Greedy algorithm, kabellengte: 3876")
        plt.show()

if __name__ == "__main__":
    start_time = datetime.now()

    for i in range(500000):
        smartgrid = SmartGrid()
        lengths.append(total_length)

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    # standard deviation and mean
    print("best: ", min(lengths))
    print("worst: ", max(lengths))
    print("sd: ", np.std(lengths))
    print("mean: ", np.mean(lengths))

    unique_lengths = set(lengths)
    #print(unique_lengths)
    count_unique = len(unique_lengths)
    #print(count_unique)

    bins = np.linspace(math.ceil(min(lengths)),
                   math.floor(max(lengths)),
                   count_unique)

    plt.xlim([min(lengths), max(lengths)])

    plt.hist(lengths, bins=bins, alpha=1)
    plt.title('Shuffle algorithm (iteraties: 500 000)')
    plt.xlabel('Score')
    plt.ylabel('Aantal per score')

    plt.show()
