# Allows for encapsulation of individual factories
# provides interface for related objects without specifying their actual class

# Pros:
# objects created are always compatible
# avoids tight coupling
# uses the Single Responsibility Principle
# can introduce new variants without breaking existing code

# Cons:
# code can be overly complicated
# lot of extra code for interfaces and classes

import random

class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print(f"We have a: {pet}")
        print(f"It says: {pet.speak()}")

class Dog(object):
    def speak(self):
        return "Woof!"
    
    def __str__(self):
        return "Dog"

class Cat(object):
    def speak(self):
        return "Meow!"
    
    def __str__(self):
        return "Cat"

class Parrot(object):
    def speak(self):
        return "Squak!"
    
    def __str__(self):
        return "Parrot"

def random_animal():
    return random.choice([Dog, Cat, Parrot])()


shop = PetShop(random_animal)
for i in range(5):
    shop.show_pet()
    print("-" * 20)

# We have a: Cat
# It says: Meow!
# --------------------
# We have a: Cat
# It says: Meow!
# --------------------
# We have a: Parrot
# It says: Squak!
# --------------------
# We have a: Parrot
# It says: Squak!
# --------------------
# We have a: Dog
# It says: Woof!
# --------------------