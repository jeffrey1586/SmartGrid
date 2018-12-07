class Battery(object):

    """Defines the battery class."""
    def __init__(self, xvalue, yvalue, capacity):
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.capacity = capacity

    # get method that returns the x coordinate from the battery
    def get_xval(self):
        return self.xvalue

    def set_xval(self, xval):
        self.xvalue = xval
        return self.xvalue

    # get method that returns the y coordinate from the battery
    def get_yval(self):
        return self.yvalue

    def set_yval(self, yval):
        self.yvalue = yval
        return self.yvalue

    # get method that returns capacity the battery
    def get_capacity(self):
        return self.capacity

    # method that adjust the capacity from the battery
    def set_capacity(self, output):
        self.capacity = float(self.capacity) - float(output)
        return self.capacity

        #super(, self).__init__()
