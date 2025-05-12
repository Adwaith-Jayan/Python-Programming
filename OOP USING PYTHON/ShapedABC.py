from abc import ABC,abstractmethod
import math

class Shapes(ABC):
    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Circumference(self):
        pass

class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
    
    def Area(self):
        return math.pi * self.radius**2

    def Circumference(self):
        return 2 * math.pi * self.radius


class Rectangle(Shapes):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def Area(self):
        return self.length * self.breadth
    
    def Circumference(self):
        return 2*(self.length+ self.breadth)


r=Rectangle(10,20)
c=Circle(10)
print(r.Area())
print(r.Circumference())
print(c.Area())
print(c.Circumference())
