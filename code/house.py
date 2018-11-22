class House(object):

    """Defines the house class."""
    def __init__(self, id, xvalue, yvalue, output):
        self.id = id
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.output = output

    # calculating battery capacity and cable lengths
    def calculate_all(self, house, list_batteries):
        batteries = list_batteries
        distances = []
        x = house.get_xval()
        y = house.get_yval()
        output = house.get_output()

        # get smallest distance out of array distances
        for battery in batteries:
            x_value = battery.get_xval()
            y_value = battery.get_yval()
            checkx = abs(int(x)-int(x_value))
            checky = abs(int(y)-int(y_value))

            # calculating distance and appending
            distTotal = checkx + checky
            distances.append(distTotal)
        return (distances, output)

    #
    def calculate_min(self, distances):

        # shortest distance from house to battery
        shortest_length = min(distances)
        return(shortest_length)

    #
    def check_capacity(self, distances, shortest_length, output, list_batteries):
        
        # getting battery closest to house
        battery_index = distances.index(shortest_length)

        # adjusting battery capacity
        batteries = list_batteries
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


    # get method that returns the x coordinate from the house
    def get_xval(self):
        return self.xvalue

    # get method that returns the y coordinate from the house
    def get_yval(self):
        return self.yvalue

    # get method that returns the output from the house
    def get_output(self):
        return self.output

    # get method that returns the id from the house
    def get_id(self):
        return self.id

    # methods that returns the values when printing house object
    def __str__(self):
        return f"{self.xvalue}, {self.yvalue}, {self.output}"
