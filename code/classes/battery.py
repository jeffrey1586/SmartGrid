"""This class represents a battery object and is used by multiple algorithms."""
class Battery(object):

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

    # method that changes the battery capacities when swap is made
    def change_capacity(self, batt_one, batt_two, house_one, house_two):
        batt_one.set_capacity(-1 * float(house_one.get_output()))
        batt_two.set_capacity(-1 * float(house_two.get_output()))
        cap_one = batt_one.set_capacity(house_two.get_output())
        cap_two = batt_two.set_capacity(house_one.get_output())
        return (cap_one, cap_two)

    # method that changes the batteryId of a house houseobject
    def change_batteryId(self, house_one, house_two, index_one, index_two):
        house_one.set_batteryId(int(index_one))
        house_two.set_batteryId(int(index_two))
        return
