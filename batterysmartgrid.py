import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from code.classes.houseTwo import House
from code.classes.batteryTwo import Battery
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
                new_house = House(id, x_value, y_value, output, 10)
                list_houses.append(new_house)
                id += 1
            counter = 1
        return list_houses

    # method that connects houses with batteries
    def connecting(self):

        global count
        global optimal
        global optimallength
        if count == 0:

            # change order of array list_houses
            #shuffle(self.houses)
            total_length = 0
            battery_index = 0
            counter = 0
            i = 0

            for battery in self.batteries:
                if counter == 0:
                    # calculate length to closest battery
                    all_distances = battery.calculate_all(battery, self.houses)
                    distances = all_distances
                    counter = 1

                new_capacity = battery.get_capacity()

                # connect houses until capacity is full
                while (float(new_capacity) > 0 and i < 150):
                    i += 1
                    # calculate length to closest battery
                    min_distance = battery.calculate_min(distances)

                    # adjusting battery capacity and checking for overload
                    capacity = battery.check_capacity(distances, min_distance, new_capacity, self.houses, battery_index, battery)
                    new_capacity = capacity[0]
                    house_output = capacity[1]
                    new_house = capacity[2]
                    distances = capacity[3]
                    house_index = capacity[4]
                    total_length += min_distance


                    if new_capacity < 0:

                        # add output back to negative battery
                        new_capacity = battery.set_capacity(-1 * float(house_output))
                        all_capacities = []
                        for cap_battery in self.batteries:
                            all_capacities.append(float(cap_battery.get_capacity()))

                        # get new battery
                        temp_cap = max(all_capacities)
                        new_index = all_capacities.index(temp_cap)
                        new_battery = self.batteries[new_index]

                        # substract output from other closest battery
                        new_capacity = new_battery.set_capacity(house_output)
                        new_house.set_batteryId(new_index)
                        distances[house_index] = 10000

                battery_index += 1
            print(total_length)
        return total_length

    # method that visualizes the grids
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

    for i in range(1):
        smartgrid = SmartGrid()