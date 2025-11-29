# Parent class
class Shape:
    def area(self):
        raise NotImplementedError("Area method not implemented")

    def perimeter(self):
        raise NotImplementedError("Perimeter method not implemented")


# =============================================
# Child Class: Circle
# =============================================
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# =============================================
# Child Class: Square
# =============================================
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# =============================================
# Child Class: Triangle
# =============================================
class Triangle(Shape):
    def __init__(self, a, b, c, base, height):
        self.a = a
        self.b = b
        self.c = c
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.a + self.b + self.c


# ==================================================
# Example Usage
# ==================================================

# Circle Example
c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

# Square Example
s = Square(4)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())

# Triangle Example
t = Triangle(3, 4, 5, base=4, height=3)
print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())
