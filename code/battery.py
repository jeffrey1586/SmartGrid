class Battery(object):

    """Defines the battery class."""
    def __init__(self, xvalue, yvalue, capacity):
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.capacity = capacity

    """ """
    def get_xval(self):
        return self.xvalue

    """ """
    def get_yval(self):
        return self.yvalue

    """ """
    def get_capacity(self):
        return self.capacity

    """ """
    def set_capacity(self, output):
        self.capacity = float(self.capacity) - float(output)
        return self.capacity

        #super(, self).__init__()
