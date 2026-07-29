import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(4, 6)

print(p1)
print(p1 == p2)
print(p1.distance(p3))

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2

print(v1)
print(v3)