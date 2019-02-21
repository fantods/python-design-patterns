# Provides an interface to a resource that is expensive to duplicate

# Pros: 
# controls a service object without client knowing about it
# manage lifecycle of a service object when clients don't care
# proxy works even if service object isn't ready or unavailable
# open/closed principle

# Cons:
# more complicated code
# service object response might become delayed


import time

class SalesManager:
    def talk(self):
        print("Sales Manager is ready to talk")

class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None
    
    def talk(self):
        print("Proxy checking Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print("Sales Manager is busy")

class NoTalkProxy(Proxy):
    def talk(self):
        print("Proxy checking Sales Manager availability")
        time.sleep(0.1)
        print("This Sales Manager will not talk to you, whether they are busy or not")
        

p = Proxy()
p.talk()
p.busy = 'Yes'
p.talk()
# Proxy checking Sales Manager availability
# Sales Manager is ready to talk
# Proxy checking Sales Manager availability
# Sales Manager is busy

p = NoTalkProxy()
p.talk()
p.busy = 'Yes'
p.talk()
# Proxy checking Sales Manager availability
# This Sales Manager will not talk to you, whether they are busy or not
# Proxy checking Sales Manager availability
# This Sales Manager will not talk to you, whether they are busy or not