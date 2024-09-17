import math
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def DisplayArea(self):
        print(f"The area of {self.name} is {self.area():.2f}")
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height 

def main():
    shapes = [Circle(10), Rectangle(3, 5), Triangle(10, 15)]
    for s in shapes:
        s.DisplayArea()
#    c = Circle(10)
#    r = Rectangle(3, 5)
#    t = Triangle(10, 15)
#    c.DisplayArea()
#    r.DisplayArea()
#    t.DisplayArea()
main()








