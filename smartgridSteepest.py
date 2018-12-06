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
import random

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

        # change order of array list_houses
        # shuffle(self.houses)
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

            # add distance to total_length
            total_length += index_battery[1]

        # Stochastic hill climber implementation
        house = self.houses[0]
        besttotal = house.total(self.houses, self.batteries)
        for i in range(10000):
            j = random.randint(0,149)
            house_first = self.houses[j]
            index_first = int(house_first.get_batteryId())
            battery_first = self.batteries[index_first]
            swap_distances = {}

            for house_sec in self.houses:
                index_sec = int(house_sec.get_batteryId())
                battery_sec = self.batteries[index_sec]

                # check if houses are connected to same battery
                if (index_first != index_sec):
                    battery_first.set_capacity(-1 * float(house_first.get_output()))
                    battery_sec.set_capacity(-1 * float(house_sec.get_output()))
                    cap_one = battery_first.set_capacity(house_sec.get_output())
                    cap_two = battery_sec.set_capacity(house_first.get_output())

                    # checking if capacities are exceeded
                    if (cap_one < 0 or cap_two < 0):
                        battery_first.set_capacity(-1 * float(house_sec.get_output()))
                        battery_sec.set_capacity(-1 * float(house_first.get_output()))
                        battery_first.set_capacity(house_first.get_output())
                        battery_sec.set_capacity(house_sec.get_output())

                    # swap connections
                    else:
                        house_first.set_batteryId(int(index_sec))
                        house_sec.set_batteryId(int(index_first))
                        newtotal = house.total(self.houses, self.batteries)

                        # check for better result and append to list
                        if (besttotal > newtotal or besttotal == newtotal):
                            print("old: ", besttotal)
                            besttotal = newtotal
                            print("new: ", newtotal)
                            swap_distances[house_sec] = newtotal

                        house_first.set_batteryId(int(index_first))
                        house_sec.set_batteryId(int(index_sec))
                        battery_first.set_capacity(-1 * float(house_sec.get_output()))
                        battery_sec.set_capacity(-1 * float(house_first.get_output()))
                        battery_first.set_capacity(house_first.get_output())
                        battery_sec.set_capacity(house_sec.get_output())

            # get best swap option
            if swap_distances != {}:
                house_sec = min(swap_distances, key=swap_distances.get)
                index_sec = int(house_sec.get_batteryId())
                battery_sec = self.batteries[index_sec]

                house_first.set_batteryId(int(index_sec))
                house_sec.set_batteryId(int(index_first))
                battery_first.set_capacity(house_sec.get_output())
                battery_sec.set_capacity(house_first.get_output())

                print(house.total(self.houses, self.batteries))


        # writing total_length value to csv
        # with open('resultaten/testresults.csv', mode='a') as results_file:
        #     results_writer = csv.writer(results_file)
        #     export_data = [total_length]
        #     results_writer.writerow(export_data)

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
                ax.plot(xHouse, yHouse, '*', color='lightgreen')

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

        # adding the batteries to the plot
        xBat = list(map(lambda x: x[0], Batteries))
        yBat = list(map(lambda x: x[1], Batteries))
        ax.plot(xBat, yBat, 's', color='red')

        # appending cables lines to lineCollection
        cables = []
        for i in range(150):
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
    start_time = datetime.now()

    for i in range(1):
        smartgrid = SmartGrid()

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
