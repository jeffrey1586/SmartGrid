class House(object):

    """Defines the house class."""
    def __init__(self, id, xvalue, yvalue, output, batteryId):
        self.id = id
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.output = output
        self.batteryId = batteryId

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

    # get the shortest battery distance
    def calculate_min(self, distances):

        # shortest distance from house to battery
        shortest_length = min(distances)
        return(shortest_length)

    #   search battery to connect to
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

    # calculate total length of grid
    def total(self, list_houses, list_batteries):

        total = 0
        for house in list_houses:
            index = house.get_batteryId()
            battery = list_batteries[index]

            x_diff = abs(int(house.get_xval()) - int(battery.get_xval()))
            y_diff = abs(int(house.get_yval()) - int(battery.get_yval()))
            tot = x_diff + y_diff
            total += tot
        return total

    # calculate length of two cables
    def local_length(self, house_first, house_sec, list_batteries):
         index_first = house_first.get_batteryId()
         index_sec = house_sec.get_batteryId()
         battery_first = list_batteries[index_first]
         battery_sec = list_batteries[index_sec]

         x_first = abs(int(house_first.get_xval()) - int(battery_first.get_xval()))
         y_first = abs(int(house_first.get_yval()) - int(battery_first.get_yval()))
         x_sec = abs(int(house_sec.get_xval()) - int(battery_sec.get_xval()))
         y_sec = abs(int(house_sec.get_yval()) - int(battery_sec.get_yval()))

         tot_first = x_first + y_first
         tot_sec = x_sec + y_sec
         total = tot_first + tot_sec
         return total

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

    def get_batteryId(self):
        return self.batteryId

    #
    def set_batteryId(self, index):
        self.batteryId = index
        return self.batteryId


    # methods that returns the values when printing house object
    def __str__(self):
        return f"{self.id}, {self.xvalue}, {self.yvalue}, {self.output}, {self.batteryId}"
