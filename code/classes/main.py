import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from house import House
from battery import Battery

# reading the house file for 'wijk1'
housefile= open("wijk1_huizen.csv", "r")

# making house instances and adding to list
list_houses = []
counter = 0
for line in housefile:
    if counter != 0:
        values = line.split(",")
        x_value = values[0]
        y_value = values[1]
        output = values[2]
        list_houses.append(House(x_value, y_value, output))
    counter = 1


# reading the battery file for 'wijk1'
batteryfile= open("wijk1_batterijen.txt", "r")

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


# readinng from house file
housefile= pd.read_csv('wijk1_huizen.csv', sep = ',')

#load in batteries (hardcoded)
Batteries = [
            (38, 12),
            (43, 13),
            (42, 3),
            (49, 23),
            (3, 45),
]

# setting the x and y coordinates from the houses in the plot
fig, ax = plt.subplots()
housefile.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, color='blue')

# adding the batteries to the plot
xBat = list(map(lambda x: x[0], Batteries))
yBat = list(map(lambda x: x[1], Batteries))
ax.plot(xBat, yBat, 's', color='red')

# turn on the grid
ax.grid()

# establish gridlines and show plot
plt.xticks(np.arange(0, 51, 1))
plt.yticks(np.arange(0, 51, 1))
plt.show()
