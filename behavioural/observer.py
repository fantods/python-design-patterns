# maintains a list of dependent items and notifies of changes
# used in the Signal abstraction in Django/Flask

# Pros:
# supports loosely coupled design between objects and interactions
# allows for efficient data transfer between objects
# no modifications needed to add new observers
# can add/remove observers at any time

# Cons:
# must subclass observers
# can add unnecessary complexity
# order of observer notifications can be tricky

class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def deatch(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self, modifier=None):
        for obs in self._observers:
            if modifier != obs:
                obs.update(self)

class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class HexViewer:
    def update(self, subject):
        print(u'HexViewer: Subject %s has data 0x%x' % (subject.name, subject.data))

class DecimalViewer:
    def update(self, subject):
        print(u'DecimalViewer: Subject %s has data %d' % (subject.name, subject.data))


# create example data
data1 = Data("Data Element 1")
data2 = Data("Data Element 2")

# create data viewers
viewer1 = DecimalViewer()
viewer2 = HexViewer()

# attach data to viewers
data1.attach(viewer1)
data1.attach(viewer2)

data2.attach(viewer1)
data2.attach(viewer2)

# update data:
data1.data = 10
# DecimalViewer: Subject Data Element 1 has data 10
# HexViewer: Subject Data Element 1 has data 0xa

data2.data = 15
# DecimalViewer: Subject Data Element 2 has data 15
# HexViewer: Subject Data Element 2 has data 0xf

# detach observer from HexViewer
data1.deatch(viewer2)
data2.deatch(viewer2)

data1.data = 20
# DecimalViewer: Subject Data Element 1 has data 20
data2.data = 50
# DecimalViewer: Subject Data Element 2 has data 50