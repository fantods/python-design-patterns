# Decouples an abstraction from its implementation

# Pros:
# creates platform-independent classes and applications
# client code works with high-level abstractions, not exposed to platform details
# open/closed principle
# single responsibility principle

# Cons:
# might make code more complicated by applying the pattern to a highly cohesive class

# Concrete 1
class DrawingAPIv1(object):
    def draw_circle(self, x, y, radius):
        print(f"APIv1.circle at: {x}:{y}, radius: {radius}")

# Concrete 2
class DrawingAPIv2(object):
    def draw_circle(self, x, y, radius):
        print(f"APIv2.circle at: {x}:{y}, radius: {radius}")
    

# Abstraction
class CircleShape(object):
    def __init__(self, x, y, radius, api):
        self._x = x
        self._y = y
        self._radius = radius
        self._api = api
    
    # Low level Implementation specific method
    def draw(self):
        self._api.draw_circle(self._x, self._y, self._radius)

    # High level Abstraction specific method
    def scale(self, pct):
        self._radius *= pct

shapes = (
    CircleShape(1, 2, 3, DrawingAPIv1()),
    CircleShape(5, 7, 11, DrawingAPIv2())
)

for shape in shapes:
    shape.scale(2.5)
    shape.draw()

# output:
# APIv1.circle at: 1:2, radius: 7.5
# APIv2.circle at: 5:7, radius: 27.5