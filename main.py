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
         a = (self.edge_base * self.edge_heigth) / 2
         return area

    def perimeter(self):
        p = (self_edge_a + self_edge_b + self_edge_c)
        return perimeter

     def update_edge_length(self, new_length):
         self.edge_length = new_length

     def add_ally(self, shape_object):
         self.allies.append(shape_object)

     def add_enemy(self, shape_object):
         self.enemies.append(shape_object)

if __name__ == '__main__':
    triangle_equi = Triangle(3, "equi", [], [])
    print(triangle_equi.area())
    print(triangle_equi.update_edge_length(6))
    print(triangle_equi.area())

class Circle(object):
    shape_type = 'circle'
    def __init__(radius, edge_length, allies, enemies):
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(radius):
        a = math.pi * radius**2
        return a

    def diameter(double_radius)
        d = radius + radius
        return d

    def update_edge_length(radius, new_length):
        radius_length = new_length

    def add_ally(radius, shape_object):
        radius.allies.append(shape_object)

    def add_enemy(radius, shape_object):
        radius.enemies.append(shape_object)

if __name__ == '__main__':
    circle_red = Circle(5, "red", [], [])
    print(circle_red.area())
    print(circle_red.update_edge_length(8))
    print(circle_red.area())





