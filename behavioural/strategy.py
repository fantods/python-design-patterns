# design a family of operations or algorithms
# that are interchangeable and encaspulated
# let the algorithm vary based on clients use-case
# decouples the client class from the class implementing the algorithm

# Pros:
# prevents conditional statements
# loose coupling with context entity
# easily extendable

# Cons:
# client must know of different strategies and how they differ
# increases number of objects in application (and memory!)

class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else: 
            discount = 0
        return self.price - discount
    
    def __repr__(self):
        fmt = "<Price: {}, price after discount: {}>"
        return fmt.format(self.price, self.price_after_discount())
    
def ten_percent(order):
    return order.price * 0.10

def on_sale(order):
    return order.price * 0.25 + 20


order1 = Order(100)
order2 = Order(100, discount_strategy=ten_percent)
order3 = Order(100, discount_strategy=on_sale)


print(order1)
# <Price: 100, price after discount: 100>
print(order2)
# <Price: 100, price after discount: 90.0>
print(order3)
# <Price: 100, price after discount: 55.0>
