import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from code.house import House
from code.battery import Battery
from random import shuffle

"""
initialising variables, filling when better smartgrid is found
optimal for best sequence in list_houses, optimallength for best cabledistance
"""
optimal = []
optimallength = 0

# initialising counters for comparing
count = 0

class SmartGrid():

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

    # load method for houses
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

    # connecting batteries to houses
    def connecting(self):


        global count
        global optimal
        global optimallength
        if count == 0:

            # change order of array list_houses
            #shuffle(self.houses)
            total_length = 0
            for house in self.houses:

                # calculate length to closest battery
                all_distances = house.calculate_all(house, self.batteries)

                # calculate length to closest battery
                min_distance = house.calculate_min(all_distances[0])

                # adjusting battery capacity and checking for overload
                index_battery = house.check_capacity(all_distances[0], min_distance, all_distances[1], self.batteries)

                # add the batterynumber to houseobject
                house.set_batteryId(index_battery[0])

                total_length += index_battery[1]


        else:
            # shuffle(optimal)
            total_length = 0
            for house in optimal:
                # calculate length to closest battery
                all_distances = house.calculate_all(house, self.batteries)

                # calculate length to closest battery
                min_distance = house.calculate_min(all_distances[0])

                # adjusting battery capacity and checking for overload
                index_battery = house.check_capacity(all_distances[0], min_distance, all_distances[1], self.batteries)

                # add the batterynumber to houseobject
                house.set_batteryId(index_battery[0])
                total_length += index_battery[1]


        if count == 0:
            optimal = self.houses
            optimallength = total_length
            count = 1

        else:
            if optimallength > total_length:
                optimallength = total_length
                optimal = self.houses
                print(optimallength)

        return total_length

    # method for visualizing grid
    def visualize_grid(self):

        # reading the house file
        housefile = pd.read_csv("data/wijk1_huizen.csv")

        # setting the x and y coordinates from the houses in the plot
        fig, ax = plt.subplots()
        housefile.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, color='grey')

        #load in battery coordinates
        Batteries = []
        for i in range(5):
            battery_nmr = self.batteries[i]
            x_battery = int(battery_nmr.get_xval())
            y_battery = int(battery_nmr.get_yval())
            Batteries.append((x_battery, y_battery))

        # adding the batteries to the plot
        xBat = list(map(lambda x: x[0], Batteries))
        yBat = list(map(lambda x: x[1], Batteries))
        ax.plot(xBat, yBat, 's', color='red')

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
        plt.show()

if __name__ == "__main__":

    for i in range(5):
        smartgrid = SmartGrid()
