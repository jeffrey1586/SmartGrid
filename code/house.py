class House(object):

    """Defines the house class."""
    def __init__(self, xvalue, yvalue, output):
            self.xvalue = xvalue
            self.yvalue = yvalue
            self.output = output


    def calculate(self, x, y):
        batteries = [(38, 12),(43, 13),(42, 3),(49, 23),(3, 45)]
        check = []
        for i in batteries:
            x_value = i[0]
            y_value = i[1]
            checkx = abs(int(x)-int(x_value))
            checky = abs(int(y)-int(y_value))
            disty = checkx + checky
            check.append(disty)
            smallest = min(check)
            index = check.index(smallest)
            print(index)

        return smallest

    def __str__(self):
        return f"{self.xvalue}, {self.yvalue}, {self.output}"

        #super(, self).__init__()
