class ParkingLot:
    def __init__(self, location, sq_feet, num_spaces, cost_per_hour):
        self.location = location
        self.sq_feet = sq_feet
        self.num_spaces = num_spaces
        self.cost_per_hour = cost_per_hour
        self.open_spots = num_spaces

    def take_spots(self, number_of_spots=1):
        self.open_spots -= number_of_spots
        return self.open_spots

    def leave_parking_lot(self, number_of_spots=1):
        self.open_spots += number_of_spots
        return self.open_spots

    def get_location(self):
        print("Your parking lot is located in {}".format(self.location))
        return self.location

    def set_location(self, location):
        self.location = location
        print("Your parking lot is located in {}".format(self.location))

    def get_sq_feet(self):
        return self.sq_feet

    def set_sq_feet(self, sq_feet):
        self.sq_feet = sq_feet

    def get_num_spaces(self):
        return self.num_spaces

    def set_num_spaces(self, num_spaces):
        self.num_spaces = num_spaces

    def get_cost_per_hour(self):
        return self.cost_per_hour

    def set_cost_per_hour(self, cost_per_hour):
        self.cost_per_hour = cost_per_hour


new_parking_lot = ParkingLot("Massachusetts", 10000, 1000, 10)
new_parking_lot.get_location()
new_parking_lot.take_spots(15)
print(new_parking_lot.open_spots)
print(vars(new_parking_lot))
