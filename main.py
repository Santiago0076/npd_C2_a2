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

class Square(object):
    shape_type = 'square'

    def __init__(self, edge_length, allies, enemies):
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

if __name__ == '__main__':
    square_marty = Square(5, "marty", [], [])
    print(square_marty.area())
    print(square_marty.update_edge_length(10))
    print(square_marty.area())

class Triangle(object):
    shape_type = 'equilateral'
    def __init__(self, edge_length, allies, enemies):
         self.edge_length = edge_length
         self.name = name
         self.allies = allies
         self.enemies = enemies

     def area(self):
         formula_triangle = (self.base * self.heigth) / 2
         return area

    def perimeter(self):

        return self.edge = (self_edge_a + self_edge_b + self_edge_c)

     def update_edge_length(self, new_length):
         self.edge = new_length

     def add_ally(self, shape_object):
         self.allies.append(shape_object)

     def add_enemy(self, shape_object):
         self.enemies.append(shape_object)
  if __name__ == '__main__':
     square_marty = Square(5, "marty", [], [])
     print(triangle.area())
     print(triangle.update_edge_length(10))
     print(triangle.area())

class Circle(object):
    shape_type = 'circle'
    def __init__(self, edge_length, allies, enemies):
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        formula_circle = pi * radius**2
        return area

    def add_ally





