# POO !!

# Class definition
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry
  def description(self):
    print self.name,
    print self.age,
    print self.is_hungry,
    print self.is_alive

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

zebra.description()
giraffe.description()
panda.description()