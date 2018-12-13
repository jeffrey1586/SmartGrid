import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from code.classes.houseTwo import House
from code.classes.batteryTwo import Battery
from random import shuffle
from visualize import Visualize


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
        # self.visualize = self.visualize_grid()


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
            # shuffle(self.houses)
            connecting_houses = self.houses
            total_length = 0
            battery_nmr = 0
            i = 0

            for battery in self.batteries:

                # calculate length to closest battery
                all_distances = battery.calculate_all(battery, connecting_houses)
                distances = all_distances
                new_capacity = battery.get_capacity()

                # connect houses until capacity is full
                while (float(new_capacity) > 0):

                    # calculate length to closest battery
                    cable = battery.calculate_min(distances)
                    house_index = cable[0]
                    length = cable[1]

                    # adjusting battery capacity and checking for overload
                    capacity = battery.check_capacity(connecting_houses, house_index, battery, distances, battery_nmr, total_length, length)
                    new_capacity = capacity[0]
                    house_output = capacity[1]
                    total_length = capacity[2]
                    new_house = capacity[3]

                # if ouput does not fit in battery capacity
                if (new_capacity < 0):
                        new_capacity = battery.set_capacity(-1 * float(house_output))

                battery_nmr += 1

            all_id = []
            for house in self.houses:
                all_id.append(house.get_batteryId())
            print(all_id)

            all_capacities = []
            for cap_battery in self.batteries:
                all_capacities.append(float(cap_battery.get_capacity()))
            print(all_capacities)
            print(total_length)

        return total_length


    # method that visualizes the grids
    def visualize_grid(self):

        list_houses = self.houses
        list_batteries = self.batteries
        visualize_grid = Visualize(list_houses, list_batteries)

        visualize_grid.visualize_all(list_houses, list_batteries)

if __name__ == "__main__":

    for i in range(1):
        smartgrid = SmartGrid()
