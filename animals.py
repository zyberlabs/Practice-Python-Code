#!/usr/bin/python

# Class definition
class Animal(object):
    """ Makes cute animals """
    # For initializing our instance objects
    is_alive = True
    health = "good"
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
    def description(self):
        print self.name
        print self.age

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
panda.is_alive = False
hippo = Animal("Bert", 12, True)
sloth = Animal("Pokey", 2, False)
ocelot = Animal("Swookie", 5, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry
panda.description()
print
print hippo.health
print sloth.health
print ocelot.health

