# ensures only one instance of the class exists in memory
class OneOnly:  
    singleton = None  
   
    def __new__(cls, *args, **kwargs):  
        if not cls.singleton:  
            cls.singleton = object.__new__(OneOnly)  
        return cls.singleton  
   
    def __init__(self, name):  
        self.name = name  
   
    def print_name(self):  
        print(self.name)  

test1 = OneOnly("Matt")

if OneOnly.singleton:
    test2 = OneOnly.singleton
else:
    test2 = OneOnly("something went wrong!")

assert test1 == test2
test1.print_name()
test2.print_name()
# Matt
# Matt