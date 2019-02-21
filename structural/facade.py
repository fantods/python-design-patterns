# Provides simple unified interface to a complex system

# Pros:
# allows you to isolate code from complexity of a subsystem

# Cons:
# can become a god object, coupled to all classes in an application

import time

SLEEP = 0.1

# Complex Parts:
# Complex Parts
class TC1:
    def run(self):
        print(u"###### In Test 1 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")

class TC2:
    def run(self):
        print(u"###### In Test 2 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")

class TC3:
    def run(self):
        print(u"###### In Test 3 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")

class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def run_all(self):
        [i.run() for i in self.tests]

runner = TestRunner()
runner.run_all()

# output:
# ###### In Test 1 ######
# Setting up
# Running test
# Tearing down
# Test Finished

# ###### In Test 2 ######
# Setting up
# Running test
# Tearing down
# Test Finished

# ###### In Test 3 ######
# Setting up
# Running test
# Tearing down
# Test Finished