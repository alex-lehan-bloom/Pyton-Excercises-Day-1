from vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, year_made, top_speed, type_of_handlebars, number_of_gears=21, seating_capacity=1):
        self.type_of_handlebars = type_of_handlebars
        self.number_of_gears = number_of_gears
        super().__init__("Bike", year_made, top_speed, 2, seating_capacity)

    # Setters
    def set_type_of_handlebars(self, type_of_handlebars):
        self.type_of_handlebars = type_of_handlebars

    def set_number_of_gears(self, number_of_gears):
        self.number_of_gears = number_of_gears

    # Getters
    def get_type_of_handelbars(self):
        return self.type_of_handlebars

    def get_number_of_gears(self):
        return self.number_of_gears


my_bike = Bike(2019, 25, "drop down")
print(vars(my_bike))
