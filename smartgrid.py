import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from code.house import House
from code.battery import Battery

class SmartGrid():

    def __init__(self):

        self.batteries = self.load_batteries()
        self.houses = self.load_houses()
        self.visualize = self.visualize_grid()

        self.connected_battery = self.connected_battery

    # load method for Batteries
    def load_batteries(self):

        # reading the battery file for 'wijk1'
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

    def load_houses(self):

        # reading the house file
        housefile= open("data/wijk1_huizen.csv", "r")

        list_houses = []
        # making house instances and adding to list
        self.connected_battery = []
        counter = 0
        for line in housefile:
            if counter != 0:
                values = line.split(",")
                x_value = values[0]
                y_value = values[1]
                output = values[2]
                new_house = House(x_value, y_value, output)
                list_houses.append(new_house)

                # calculate length to closest battery
                battery_index = new_house.calculate(x_value, y_value, output, self.batteries)
                self.connected_battery.append(battery_index)
            counter = 1
        return list_houses

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
        segs = []
        for i in range(149):
            house = self.houses[i]
            index = self.connected_battery[i]
            battery_nmr = Batteries[index]
            x1 = house.get_xval()
            y1 = house.get_yval()
            x2 = battery_nmr[0]
            y2 = battery_nmr[1]
            segs.append(((x1, y1), (x1, y2)))
            segs.append(((x1, y2), (x2, y2)))
        # adding the entire collection to the grid
        ln_coll = LineCollection(segs)
        ax.add_collection(ln_coll)

        # turn on the grid
        ax.grid()

        # establish gridlines and show plot
        plt.xticks(np.arange(0, 51, 1))
        plt.yticks(np.arange(0, 51, 1))
        plt.show()

if __name__ == "__main__":
    smartgrid = SmartGrid()
