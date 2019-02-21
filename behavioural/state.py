# implements state as a derived class of the state pattern interface
# allows for state transitions by invoking methods from superclass
# allows for changing of behavior at runtime

# Pros:
# reduces conditional complexity, no need for if/switch statements
# simplifies complex models

# Cons: 
# large amount of code needed
# adds to application complexity but reduces runtime complexity

class State(object):
    """Base State: shares functionality"""

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Scanning, current station is: {self.stations[self.pos]}, {self.name}")
            
class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1254", "1942", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Switching to FM Radio")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["99.9", "102.1", "104.1"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Switching to AM Radio")
        self.radio.state = self.radio.fmstate

class Radio(object):
    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate
    
    def toggle_amfm(self):
        self.state.toggle_amfm()
    
    def scan(self):
        self.state.scan()

radio = Radio()
actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
actions *= 2

for action in actions:
    action()

# output:
# Scanning, current station is: 1942, AM
# Scanning, current station is: 1510, AM
# Switching to FM Radio
# Scanning, current station is: 102.1, FM
# Scanning, current station is: 104.1, FM
# Scanning, current station is: 99.9, FM
# Scanning, current station is: 102.1, FM
# Switching to AM Radio
# Scanning, current station is: 104.1, FM
# Scanning, current station is: 99.9, FM