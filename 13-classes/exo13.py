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


# Inheritance Syntax
class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

  def check_angles(self):
      return super(Equilateral, self).check_angles()


my_triangle = Triangle(30, 60, 90)
print my_triangle.number_of_sides
print "angles of my_triangle: ", my_triangle.check_angles()
my_equilateral_triangle = Equilateral()
print "angles of my_equilateral_triangle: ", my_equilateral_triangle.check_angles()