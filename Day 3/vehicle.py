
class Vehicle:

    def __init__(self, year_made, top_speed, num_wheels, seating_capacity):
        self.year_made = year_made
        self.top_speed = top_speed
        self.num_wheels = num_wheels
        self.seating_capacity = seating_capacity
        self.current_speed = 0

    def accelerate(self, increase_by):
        self.current_speed += increase_by
        return "You are going {} MPH".format(self.current_speed)

    def brake(self, decrease_by):
        self.current_speed -= decrease_by
        return "You are going {} MPH".format(self.current_speed)

    def stop(self):
        self.current_speed = 0
        return "You have stopped. You are now going {} MPH".format(self.current_speed)

    # Setters and Getters
    def set_year_made(self, year_made):
        self.year_made = year_made

    def set_top_speed(self, top_speed):
        self.top_speed = top_speed

    def set_num_wheels(self, num_wheels):
        self.num_wheels = num_wheels

    def set_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def get_year_made(self):
        return self.year_made

    def get_top_speed(self):
        return self.top_speed()

    def get_num_wheels(self):
        return self.num_wheels

    def get_seating_capacity(self):
        return self.seating_capacity()


my_vehicle = Vehicle(2006, 100, 4, 5)

print(my_vehicle.accelerate(50))
print(my_vehicle.accelerate(20))
print(my_vehicle.brake(25))
