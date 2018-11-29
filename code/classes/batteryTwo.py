class Battery(object):

    """Defines the battery class."""
    def __init__(self, xvalue, yvalue, capacity):
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.capacity = capacity

    # calculating battery capacity and cable lengths
    def calculate_all(self, battery, list_houses):
        houses = list_houses
        distances = []
        x = battery.get_xval()
        y = battery.get_yval()

        # get smallest distance out of array distances
        for house in houses:
            x_value = house.get_xval()
            y_value = house.get_yval()
            checkx = abs(int(x)-int(x_value))
            checky = abs(int(y)-int(y_value))

            # calculating distance and appending
            distTotal = checkx + checky
            distances.append(distTotal)

        return distances

    #
    def calculate_min(self, distances):

        # shortest distance from house to battery
        shortest_length = min(distances)
        return(shortest_length)

    #
    def check_capacity(self, distances, shortest_length, capacity, list_houses, battery_nmr, battery):

        # getting house closest to battery
        house_index = distances.index(shortest_length)

        # getting house information for connection
        new_house = list_houses[house_index]
        house_output = new_house.get_output()

        # adjusting capacity
        capacity = battery.set_capacity(house_output)

        if (capacity > 0):
            # adding the connected battery index to house object
            new_house.set_batteryId(battery_nmr)
            distances[house_index] = 10000

        return (capacity, house_output, new_house, distances, house_index)

    # get method that returns the x coordinate from the battery
    def get_xval(self):
        return self.xvalue

    # get method that returns the y coordinate from the battery
    def get_yval(self):
        return self.yvalue

    # get method that returns capacity the battery
    def get_capacity(self):
        return self.capacity

    # method that adjust the capacity from the battery
    def set_capacity(self, output):
        self.capacity = float(self.capacity) - float(output)
        return self.capacity

        #super(, self).__init__()
