class Battery(object):

    """Defines the battery class."""
    def __init__(self, xvalue, yvalue, capacity):
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.capacity = capacity

    # calculating battery capacity and cable lengths
    def calculate_all(self, battery, connecting_houses):
        distances = []
        x = battery.get_xval()
        y = battery.get_yval()
        i = 0

        # calculating distances from battery to all houses
        for house in connecting_houses:
            # only calculate distance if house is not yet connected
            if (house.get_batteryId() == 10):
                x_value = house.get_xval()
                y_value = house.get_yval()
                checkx = abs(int(x)-int(x_value))
                checky = abs(int(y)-int(y_value))
                distTotal = checkx + checky
            else:
                distTotal = 10000

            # calculating distance and appending
            distances.append(distTotal)

        return distances

    # search to closest houses for the batteries
    def calculate_min(self, distances):

        # searching house closest to battery
        length = min(distances)
        house_index = distances.index(length)

        return(house_index, length)

    # adjusting battery capacity and connecting house
    def check_capacity(self, connecting_houses, house_index, battery, distances, battery_nmr, total_length, length):

        # adjusting battery capacity
        new_house = connecting_houses[house_index]
        house_output = new_house.get_output()
        new_capacity = battery.set_capacity(house_output)

        # connecting house to battery
        if (new_capacity > 0):
            new_house.set_batteryId(battery_nmr)
            distances[house_index] = 10000
            total_length += length

        return (new_capacity, house_output, total_length, new_house)

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
