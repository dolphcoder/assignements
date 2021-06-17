#6
from math import pi
class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(pi*self.radius**2) 

c = Circle(7)
c.area()