from base import *


class Polygon:
    num_of_vertex = int(0)
    sides = []
    angles = []

    def __init__(self, num_of_vertex, sides, angles):
        if not len(list(sides)) == num_of_vertex or not len(list(angles)) == num_of_vertex:
            raise Exception("Entered data isn't correct")
        self.num_of_vertex = int(num_of_vertex)
        self.sides = list(sides)
        self.angles = list(angles)


class Quadrangle(Polygon):
    def __init__(self, sides, angles):
        Polygon.__init__(self=self, num_of_vertex=4, sides=sides, angles=angles)


class Parallelogram(Quadrangle):
    def __init__(self, sides, angle_alpha, angle_beta):
        angles = [Angle(value=angle_alpha), Angle(value=angle_beta), Angle(value=angle_alpha), Angle(value=angle_beta)]
        Quadrangle.__init__(self=self, sides=sides, angles=angles)
        sides_sorted = list(sides).sort()
        if not sides_sorted[0].get_value() == sides_sorted[1].get_value() or \
                not sides_sorted[2].get_value() == sides_sorted[3].get_value():
            raise Exception("It isn't a parallelogram")


class Rectangle(Parallelogram):
    def __init__(self, sides):
        Parallelogram.__init__(self=self, sides=sides, angle_alpha=Angle(value=90), angle_beta=Angle(value=90))


class Rhombus(Parallelogram):
    def __init__(self, sides, angle_alpha, angle_beta):
        Parallelogram.__init__(self=self, sides=sides, angle_alpha=angle_alpha, angle_beta=angle_beta)
        sides_sorted = list(sides).sort()
        if not sides_sorted[0] == sides_sorted[1] == sides_sorted[2] == sides_sorted[3]:
            raise Exception("It isn't a rhombus")


class Square(Rhombus, Rectangle):
    def __init__(self, sides):
        Rhombus.__init__(self=self, sides=sides, angle_alpha=Angle(value=90), angle_beta=Angle(value=90))
