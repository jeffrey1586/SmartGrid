import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from code.house import House
from code.battery import Battery
from random import shuffle

for i in range(50000):
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


    housefile= open("data/wijk1_huizen.csv", "r")

    list_houses = []
    # making house instances and adding to list
    connected_battery = []
    counter = 0
    total_length = 0
    id = 1
    for line in housefile:
        if counter != 0:
            values = line.split(",")
            x_value = values[0]
            y_value = values[1]
            output = values[2]
            new_house = House(id, x_value, y_value, output)
            list_houses.append(new_house)
            id += 1
        counter = 1

    # volgorde list_houses veranderen
    shuffle(list_houses)

    total_length = 0
    for house in list_houses:
        # calculate length to closest battery
        battery_index = house.calculate(house.get_xval(), house.get_yval(), house.get_output(), list_batteries)
        connected_battery.append(battery_index[0])
        total_length += battery_index[1]

    if total_length < 3700:
        # # print id volgorde
        # for house in list_houses:
        #     print(house.get_id())
        print("total: ", total_length)

        # # reading the house file
        # housefile = pd.read_csv("data/wijk1_huizen.csv")
        #
        # # setting the x and y coordinates from the houses in the plot
        # fig, ax = plt.subplots()
        # housefile.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, color='grey')
        #
        # #load in battery coordinates
        # Batteries = []
        # for i in range(5):
        #     battery_nmr = list_batteries[i]
        #     x_battery = int(battery_nmr.get_xval())
        #     y_battery = int(battery_nmr.get_yval())
        #     Batteries.append((x_battery, y_battery))
        #
        # # adding the batteries to the plot
        # xBat = list(map(lambda x: x[0], Batteries))
        # yBat = list(map(lambda x: x[1], Batteries))
        # ax.plot(xBat, yBat, 's', color='red')
        #
        # # appending cables lines to lineCollection
        # segs = []
        # for i in range(150):
        #     house = list_houses[i]
        #     index = connected_battery[i]
        #     battery_nmr = Batteries[index]
        #     x1 = house.get_xval()
        #     y1 = house.get_yval()
        #     x2 = battery_nmr[0]
        #     y2 = battery_nmr[1]
        #     segs.append(((x1, y1), (x1, y2)))
        #     segs.append(((x1, y2), (x2, y2)))
        # # adding the entire collection to the grid
        # ln_coll = LineCollection(segs)
        # ax.add_collection(ln_coll)
        #
        # # turn on the grid
        # ax.grid()
        #
        # # establish gridlines and show plot
        # plt.xticks(np.arange(0, 51, 1))
        # plt.yticks(np.arange(0, 51, 1))
        # plt.show()
