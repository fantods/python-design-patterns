# Reduces t he number of classes required by an application
# easier to derive new kinds of objects, especially with instantiation is expensive

# creates new object instances by cloning a prototype

# Pros
# clone objects without coupling to concrete classes
# removes repeated initialization code
# convenient way to produce complex objects

# Cons:
# tricky to clone complex objects with circular references

class Prototype(object):
    value = 'default'

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj

class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister_object(self, name):
        del self._objects[name]


dispatcher = PrototypeDispatcher()
prototype = Prototype()

first = prototype.clone()
second = prototype.clone(value='second', category='2')
third = prototype.clone(value='third', is_checked=True)

dispatcher.register_object('first_obj', first)
dispatcher.register_object('second_obj', second)
dispatcher.register_object('third_obj', third)

print([
    { n: p.value } for n, p in dispatcher.get_objects().items()
])
# [{'first_obj': 'default'}, {'second_obj': 'second'}, {'third_obj': 'third'}]
