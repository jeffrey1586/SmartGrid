class House(object):

    """Defines the house class."""
    def __init__(self, xvalue, yvalue, output):
            self.xvalue = xvalue
            self.yvalue = yvalue
            self.output = output

    def __str__(self):
        return f"{self.xvalue}, {self.yvalue}, {self.output}" 

        #super(, self).__init__()
