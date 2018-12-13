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

class Visualize(object):

    def __init__(self, list_houses, list_batteries):
        self.houses = list_houses
        self.batteries = list_batteries

    def visualize_all(self, list_houses, list_batteries, optimallength):

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
        plt.title("Greedy algorithm, kabellengte: %s" % (optimallength))
        plt.show()
