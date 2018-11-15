

class House(object):

    """Defines the house class."""
    def __init__(self, xvalue, yvalue, output):
            self.xvalue = xvalue
            self.yvalue = yvalue
            self.output = output

    # calculating battery capacity and cable lengths
    def calculate(self, x, y, output, list_batteries):
        batteries = list_batteries
        distances = []

        #
        for battery in batteries:
            x_value = battery.get_xval()
            y_value = battery.get_yval()
            checkx = abs(int(x)-int(x_value))
            checky = abs(int(y)-int(y_value))

            distTotal = checkx + checky
            distances.append(distTotal)
            shortest_length = min(distances)

        #
        battery_index = distances.index(shortest_length)
        #
        new_capacity = batteries[battery_index].set_capacity(output)
        # if new_capacity < 0:
        #     # voeg output weer toe aan baterij
        #     zeroState = batteries[battery_index].set_capacity(-1 * float(output))
        #
        #     # trek output af van andere batterij
        #     new_capacity = batteries[1].set_capacity(output)
        # print(battery_index)
        # print(new_capacity)
        return (shortest_length, battery_index)

    def __str__(self):
        return f"{self.xvalue}, {self.yvalue}, {self.output}"

        #super(, self).__init__()
