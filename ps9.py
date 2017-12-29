# 6.00 Problem Set 9
#
# Name: Anusika Nijher
# Collaborators: None


from string import *
from operator import attrgetter
class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        self.side = float(h)
    def area(self):
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)
    def area(self):
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
# Time: 15 min

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
    def area(self):
        return ((self.base * self.height)/2)
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        return type(other) == Triangle and self.height == other.height and self.base == other.base


# Problem 2: Create the ShapeSet class
# Time: 20 min
class ShapeSet:
    def __init__(self):
        self.names = []
        self.start = 0
    def addShape(self, sh):
        if sh not in self.names:
            self.names.append(sh)
    def __iter__(self):
        self.start = 0
        return self
    def __str__(self):
        strings = ""
        self.names = sorted(self.names)
        for names in self.names:
            strings = strings + str(self.names[self.start]) + "\n"
            if self.start <= len(self.names):
                self.start +=1
            else:
                raise StopIteration
        return strings

    

#
# Problem 3: Find the largest shapes in a ShapeSet
# Time: 45 min
def findLargest(shapes):
    largest = ()
    pretty = ()
    max_area = max(shape.area() for shape in shapes.names)
    for shape in shapes.names:
        if shape.area() == max_area:
            largest = largest + (shape, )
            pretty = pretty + (str(shape), )
    print pretty
    return largest

            

##a = Triangle(1,72)
##b = Circle(1)
##c = Square(2)
##d = Square(6)
##s = ShapeSet()
##s.addShape(d)
##s.addShape(c)
##s.addShape(a)
##s.addShape(b)
##
##print str(s)
##print findLargest(s)


# Problem 4: Read shapes from a file into a ShapeSet
# Time: 20 min
def readShapesFromFile(filename):
    new_set = ShapeSet()
    inputFile = open(filename)
    for line in inputFile:
        line = line.strip()
        parts = line.split(',')
        if parts[0] == 'circle':
            new_set.addShape(Circle(parts[1]))
        elif parts[0] == 'square':
            new_set.addShape(Square(parts[1]))
        elif parts[0] == 'triangle':
            new_set.addShape(Triangle(parts[1],parts[2]))
    return new_set



SHAPES= "shapes.txt"


print readShapesFromFile(SHAPES)
