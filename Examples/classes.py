class Vehicle: # parent (super) class
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed

    def __str__(self):
        return f"{self.make} {self.model}"

    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.top_speed < other.top_speed


class ElectricCar(Vehicle): # child (sub) class, Inheritance is shwon by putting the super class in parentheses

    def __init__(self, make, model, top_speed, battery_size): # Pass in all super class data and any specialized data
        super().__init__(make, model, top_speed) # call the super class constructor first with required arguments
        self.battery_size = battery_size # initialize our subclass variables

    def __str__(self):
        return f"{super.__str__(self)} (EV, {self.battery_size}kWh)"
