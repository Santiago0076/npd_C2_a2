'''Contains shape classes and does fun things with them

Shapes:
Triangle
Square
Circle

Data Attributes:
shape_type
edge_length
name
allies
enemies

Methods:
area
perimeter
update_edge_lenght
add_ally
add_enemy
'''
import math

class Square(object):
    shape_type = 'square'

    def __init__(self, name, edge_length, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.edge_length**2

    def perimeter(self):
        return self.edge_length * 4

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

class Triangle(object):
    shape_type = 'triangle'
    def __init__(self, edge_length, edge_height, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.edge_height = edge_height
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return 0.5 *(self.edge_length * self.edge_height)

    def perimeter(self):
        return self.edge_length * 3

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

class Circle(object):
    shape_type = 'circle'
    def __init__(self, name, radius, allies, enemies):
        self.name = name
        self.radius= radius
        self.allies = allies
        self.enemies = enemies

    def area(radius):
        return math.pi * self.radius**2

    def diameter(double_radius):
        return self.radius + self.radius

    def update_edge_length(radius, new_length):
        self.radius = new_length

    def add_ally(radius, shape_object):
        self.allies.append(shape_object)

    def add_enemy(radius, shape_object):
        self.enemies.append(shape_object)

if __name__ == '__main__':
    square_marty = Square(5, "marty", [], [])
    print(square_marty.area())
    print(square_marty.update_edge_length(10))
    print(square_marty.area())


if __name__ == '__main__':
    triangle_equi = Triangle(3,  "equi", [], [])
    print(triangle_equi.area())
    print(triangle_equi.update_edge_length(6))
    print(triangle_equi.area())


if __name__ == '__main__':
    circle_red = Circle(5, pi, "red", [], [])
    print(circle_red.area())
    print(circle_red.update_radius_length(8))
    print(circle_red.area())

