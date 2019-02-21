# provides a different interface for a class
# allows for integration of classes that couldn't be normally integrated to incompatibilities

# Pros:
# implements single responsibility principle
    # separate interface from primary business logic
# implements open/closed principle
    # introduce new adapters without breaking existing client code
    # as long as they work through the client interface

# Cons:
# increases overall complexity

class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)

class Adapter(object):
    """
    Adapts an object by replacing methods
    e.g.:
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj, **methods):
        self.obj = obj
        self.__dict__.update(methods)
    
    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__

objects = []
dog = Dog()
cat = Cat()
human = Human()
car = Car()

objects.append(Adapter(dog, make_noise=dog.bark))
objects.append(Adapter(cat, make_noise=cat.meow))
objects.append(Adapter(human, make_noise=human.speak))
objects.append(Adapter(car, make_noise=lambda: car.make_noise(9)))

for obj in objects:
    print(f"a {obj.name} goes {obj.make_noise()}")

# output:
# a Dog goes woof!
# a Cat goes meow!
# a Human goes 'hello'
# a Car goes vroom!!!!!!!!!
