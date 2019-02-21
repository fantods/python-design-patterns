# decouples creation of a complex object and its representation
# helpful for abstractions

# Pros:
# code is more maintainable
# object creation is less error-prone
# increases robustness of application

# Cons:
# verbose and requires a lot of code duplication


# Abstract Building
class Building(object):
    def __init__(self):
        self.build_floor()
        self.build_size()
    
    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError
    
    def __repr__(self):
        return 'Floor: {0.floor}, Size: {0.size}'.format(self)
    
# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'


class Flat(Building):
    def build_floor(self):
        self.floor = 'More than One'

    def build_size(self):
        self.size = 'Small'

def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building

house = House()
print(house)
# Floor: One, Size: Big

flat = Flat()
print(flat)
# Floor: More than One, Size: Small

# use external constructor
complex_house = construct_building(House)
print(complex_house)
# Floor: One, Size: Big