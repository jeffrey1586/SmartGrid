class House(object):

    """Defines the house class."""
    def __init__(self, id, xvalue, yvalue, output, batteryId):
        self.id = id
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.output = output
        self.batteryId = batteryId

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
        return f"{self.xvalue}, {self.yvalue}, {self.output}, {self.batteryId}"
