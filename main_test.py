# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from house import House
#
# class SmartGrid():
#
#     """Smartgrid."""
#     def __init__(self, file):
#         self.houses = self.load_houses(f"{file}_huizen.csv")
#
#
#     def load_houses(self):
#
#         # reading the csv file for 'wijk1'
#         #housefile= pd.read_csv('data/wijk1_huizen.csv', sep = ',')
#         housefile= open("wijk1_huizen.csv", "r")
#
#         self.list_houses = []
#
#         counter = 0
#
#         for line in housefile:
#             if counter != 0:
#                 values = line.split(",")
#                 x_value = values[0]
#                 y_value = values[1]
#                 output = values[2]
#                 list_houses.append(House(x_value, y_value, output))
#             counter = 1
#         print(list_houses)
#
# if __name__ == "__main__":
#     smartgrid = SmartGrid("wijk1")
#     smartgrid.load_houses()
#
#
#
#
# # load in batteries (hardcoded)
# # Batteries = [
# #             (38, 12),
# #             (43, 13),
# #             (42, 3),
# #             (49, 23),
# #             (3, 45),
# # ]
#
# # # setting the x and y coordinates from the houses in the plot
# # fig, ax = plt.subplots()
# # housefile.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, color='blue')
# #
# # # adding the batteries to the plot
# # xBat = list(map(lambda x: x[0], Batteries))
# # yBat = list(map(lambda x: x[1], Batteries))
# # ax.plot(xBat, yBat, 's', color='red')
# #
# # # turn on the grid
# # ax.grid()
# #
# # # establish gridlines and show plot
# # plt.xticks(np.arange(0, 51, 1))
# # plt.yticks(np.arange(0, 51, 1))
# # plt.show()
