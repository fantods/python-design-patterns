# Describes a group of objects that are treated as a single instance

# Pros:
# works with complex tree structures more efficiently
    # uses polymorphism and recursion to your advantage
# open/closed principle

# Cons:
# might be difficult to provide a common interface for classes with differing functionality

class Graphic:
    def render(self):
        raise NotImplementedError

class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()
    
    def add(self, graphic):
        self.graphics.append(graphic)
    
    def remove(self, graphic):
        self.graphics.remove(graphic)

class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Ellipse: {self.name}")


ellipse1 = Ellipse("1")
ellipse2 = Ellipse("2")
ellipse3 = Ellipse("3")
ellipse4 = Ellipse("4")

graphic1 = CompositeGraphic()
graphic2 = CompositeGraphic()

graphic1.add(ellipse1)
graphic1.add(ellipse2)
graphic1.add(ellipse3)
graphic2.add(ellipse4)

graphic = CompositeGraphic()

graphic.add(graphic1)
graphic.add(graphic2)

graphic.render()

# output:
# Ellipse: 1
# Ellipse: 2
# Ellipse: 3
# Ellipse: 4