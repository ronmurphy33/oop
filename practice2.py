class Vehicle:
    def __init__(self,manufacturer,doors):
        self.manufacturer = manufacturer
        self.doors = doors

    def turn_right(self):
        print("Turning right")

    def carrying_capacity(self):
        print("Vehicle can carry 20 boxes of goods")


class Truck(Vehicle):
    def __init__(self, manufacturer, doors, bed_size, gear_count):
        super(). __init__(manufacturer, doors)
        self.bed_size = bed_size
        self.gear_count = gear_count

    def count_doors(self):
        return self.doors

    def carrying_capacity(self):
        print("Truck can carry 100 boxes of goods")


my_vehicle = Vehicle("Chevrolet",4)
my_truck = Truck("Dodge",4,100, 8)


print(my_vehicle.manufacturer)

my_vehicle.carrying_capacity()
my_truck.carrying_capacity()
my_truck.turn_right()



