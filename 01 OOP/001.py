import numpy as np
class circ:
  def __init__(self,radius):
      self.radius = radius
  def area(self):
    print(np.pi*self.radius*self.radius)
  def peri(self):
    print(2*np.pi*self.radius)
circle1 = circ(6)
circle2 =circ(5)
circle1.area()
circle1.peri()