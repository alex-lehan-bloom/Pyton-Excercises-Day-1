from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make, model, year_made, is_electric, top_speed, seating_capacity):
        self.make = make
        self.model = model
        self.is_electric = is_electric
        self.is_car_on = False
        super().__init__("Car", year_made, top_speed, 4, seating_capacity)

    # Class functions
    def turn_car_on(self):
        self.is_car_on = True

    def turn_car_off(self):
        self.is_car_on = False

    def accelerate(self, increase_by):
        if self.is_car_on == False:
            return "Cannot accelerate. You need to turn on your car first."
        else:
            self.current_speed += increase_by
            return "Your {} going {} MPH".format(self.type, self.current_speed)

    # Setters
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_is_electric(self, is_electric):
        self.is_electric = is_electric

    # Getters
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_is_electric(self):
        return self.is_electric


car_of_alex = Car("Toyota", "Camry", 2006, False, 95, 5)
print(vars(car_of_alex))
car_of_alex.turn_car_on()
print(car_of_alex.accelerate(10))