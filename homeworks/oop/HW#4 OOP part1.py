# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    vehicle_type = "all vehicle"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_max_speed(self):
        print(f'Your vehicle can accelerate up to {self.max_speed} km/hour.')

    def print_mileage(self):
        print(f'Your vehicle drove {self.mileage} km.')


bicycle = Vehicle(max_speed="40", mileage="120")
porshe = Vehicle(max_speed=300, mileage=100000)

bicycle.print_mileage()
bicycle.print_max_speed()
porshe.print_mileage()
porshe.print_max_speed()


# 2. Create a child class Bus that will inherit all the variables and methods of the Vehicle class
# and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, seating_capacity, max_speed, mileage):
        Vehicle.__init__(self, max_speed, mileage)
        self.seating_capacity = seating_capacity

    def print_seating_capacity(self):
        print(f'You can take {self.seating_capacity} passengers')


Neoplan = Bus("53", "110", "1 000 000")
School_bus = Bus("44", "70", "600 000")

Neoplan.print_seating_capacity()
Neoplan.print_mileage()
School_bus.print_mileage()

# 3. Determine which class a given Bus object belongs to (Check type of an object)

print(type(Neoplan))

# 4. Determine if School_bus is also an instance of the Vehicle class

print(isinstance(School_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own
# - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, bus_school_color, get_school_id, number_of_students, seating_capacity, max_speed, mileage):
        Bus.__init__(self, seating_capacity, max_speed, mileage)
        School.__init__(self, get_school_id, number_of_students)
        self.bus_school_color = bus_school_color

    def bus_school_color(self):
        print(f'School bus is {self.bus_school_color}')



# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def print_make_sound(self):
        print(f'I will song {self.make_sound}')


Brown = Bear(make_sound="Queen")


class Wolf:
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def print_make_sound(self):
        print(f'I will play {self.make_sound}')


Grey_wolf = Wolf(make_sound="Metallika")

animals = (Grey_wolf, Brown)

for animal in animals:
    animal.print_make_sound()


# # Magic methods:
# # 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# # otherwise return message: "Your city is too small".



