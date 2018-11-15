

class House(object):

    """Defines the house class."""
    def __init__(self, xvalue, yvalue, output):
            self.xvalue = xvalue
            self.yvalue = yvalue
            self.output = output

    # calculating which battery
    def calculate(self, x, y, list_batteries):
        batteries = list_batteries

        check = []
        for i in batteries:
            x_value = i.get_xval()
            y_value = i.get_yval()
            checkx = abs(int(x)-int(x_value))
            checky = abs(int(y)-int(y_value))
            disty = checkx + checky
            check.append(disty)
            shortest_length = min(check)
        battery_index = check.index(shortest_length)
        return (shortest_length, battery_index)

    def __str__(self):
        return f"{self.xvalue}, {self.yvalue}, {self.output}"

        #super(, self).__init__()
