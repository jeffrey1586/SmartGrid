import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from code.house import House
from code.battery import Battery

# reading the battery file for 'wijk1'
batteryfile= open("data/wijk3_batterijen.txt", "r")

# making battery instances and adding to list
list_batteries = []
counter = 0
for line in batteryfile:
    if counter != 0:
        check = line.split()
        x_value = check[0].strip('[').strip(',')
        y_value = check[1].strip(']')
        capacity = check[2]
        list_batteries.append(Battery(x_value, y_value, capacity))
    counter = 1

# reading the house file for 'wijk1'
housefile= open("data/wijk3_huizen.csv", "r")

# making house instances and adding to list
list_houses = []
counter = 0
total_length = 0
for line in housefile:
    if counter != 0:
        values = line.split(",")
        x_value = values[0]
        y_value = values[1]
        output = values[2]
        new_house = House(x_value, y_value, output)
        list_houses.append(new_house)

        # calculate length to closest battery
        shortest_length = new_house.calculate(x_value, y_value, output, list_batteries)
        total_length += shortest_length
    counter = 1
print("total", total_length)

#print("bat1", list_batteries[0].get_capacity())



## visualising the smartgrid
# readinng from house file
housefile= pd.read_csv('data/wijk3_huizen.csv', sep = ',')

#load in batteries (hardcoded)
Batteries = [
            (18, 34),
            (32, 11),
            (41, 1),
            (3, 35),
            (39, 41),
]

# setting the x and y coordinates from the houses in the plot
fig, ax = plt.subplots()
housefile.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, color='blue')

# adding the batteries to the plot
xBat = list(map(lambda x: x[0], Batteries))
yBat = list(map(lambda x: x[1], Batteries))
ax.plot(xBat, yBat, 's', color='red')

# plotting cables

# turn on the grid
ax.grid()

# establish gridlines and show plot
plt.xticks(np.arange(0, 51, 1))
plt.yticks(np.arange(0, 51, 1))
plt.show()
