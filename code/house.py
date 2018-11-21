class House(object):

    """Defines the house class."""
    def __init__(self, id, xvalue, yvalue, output):
        self.id = id
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.output = output

    # calculating battery capacity and cable lengths
    def calculate(self, x, y, output, list_batteries):
        batteries = list_batteries
        distances = []

        # get smallest distance out of array distances
        for battery in batteries:
            x_value = battery.get_xval()
            y_value = battery.get_yval()
            checkx = abs(int(x)-int(x_value))
            checky = abs(int(y)-int(y_value))

            # calculating distance and appending
            distTotal = checkx + checky
            distances.append(distTotal)

        # shortest distance from house to battery
        shortest_length = min(distances)
        # getting battery closest to house
        battery_index = distances.index(shortest_length)

        # adjusting battery capacity
        new_capacity = batteries[battery_index].set_capacity(output)

        #checking if capacity is negative
        for i in range(4):
            if new_capacity < 0:

                # add output back to negative battery
                new_capacity = batteries[battery_index].set_capacity(-1 * float(output))
                # block battery
                distances[battery_index] = 10000

                # get new battery
                shortest_length = min(distances)
                battery_index = distances.index(shortest_length)

                # substract output from other closest battery
                new_capacity = batteries[battery_index].set_capacity(output)
        return (battery_index, shortest_length)

    #
    def get_xval(self):
        return self.xvalue
    #
    def get_yval(self):
        return self.yvalue

    def get_output(self):
        return self.output

    def get_id(self):
        return self.id    

    #
    def __str__(self):
        return f"{self.xvalue}, {self.yvalue}, {self.output}"
