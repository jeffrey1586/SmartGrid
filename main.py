import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# reading the csv file for 'wijk1'
df=pd.read_csv('data/wijk1_huizen.csv', sep = ',')
print(df.head(150))

# Load in batteries
Batteries = [
            (38, 12),
            (43, 13),
            (42, 3),
            (49, 23),
            (3, 45),
]

# setting the x and y coordinates from the houses in the plot
fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, color='blue')

# adding the batteries to the plot
xBat = list(map(lambda x: x[0], Batteries))
yBat = list(map(lambda x: x[1], Batteries))
ax.plot(xBat, yBat, 's', color='red')

# turn on the grid
ax.grid()

# Establish gridlines and show plot
plt.xticks(np.arange(0, 51, 1))
plt.yticks(np.arange(0, 51, 1))
plt.show()
