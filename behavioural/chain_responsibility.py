# its like a chained if/elif/elif/else statement that can be reassigned at runtime
# decouples sender of a request from its receivers

# allows for a request to pass down a chain of receivers until it is handled

# Pros:
# decouples senders and receivers
# simplifies objects and removes direct references to members
# allows for dynamic add/removal of responsibilites

# Cons:
# hard to debug and observe runtime characteristics

# abstract base class
import abc

class Handler(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        # handles request and stop
        # calls next handler in chain if it cannot handle request
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abc.abstractmethod
    def check_range(self, request):
        """Compare passed value to predefined interval"""

class ConcreteHandler1(Handler):
    """simple static handler"""

    @staticmethod
    def check_range(request):
        if 0 <= request < 10:
            print(f"request {request} handled by handler 1")
            return True

class ConcreteHandler2(Handler):
    """handler with internal state"""

    start, end = 10, 20

    def check_range(self, request):
        if self.start <= request < self.end:
            print(f"request {request} handled by handler 2")
            return True

class ConcreteHandler3(Handler):
    """handler with helper methods"""

    def check_range(self, request):
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print(f"request {request} handled by handler 3")
            return True

    @staticmethod
    def get_interval_from_db():
        return (20, 30)

def FallbackHandler(Handler):
    @staticmethod
    def check_range(request):
        print(f"End of chain, no handler for {request}")
        return False
    
h1 = ConcreteHandler1()
h2 = ConcreteHandler2()
h3 = ConcreteHandler3()

h1.successor = h2
h2.successor = h3

requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
for request in requests:
    h1.handle(request)

# request 2 handled by handler 1
# request 5 handled by handler 1
# request 14 handled by handler 2
# request 22 handled by handler 3
# request 18 handled by handler 2
# request 3 handled by handler 1
# request 27 handled by handler 3
# request 20 handled by handler 3