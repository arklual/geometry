from base import *


class Polygon:
    def __init__(self, num_of_vertex, sides, angles):
        if not len(list(sides)) == num_of_vertex or not len(list(angles)) == num_of_vertex:
            raise Exception("Entered data isn't correct")
        self.num_of_vertex = int(num_of_vertex)
        self.sides = list(sides)
        self.angles = list(angles)

    def __get_sorted_sides_value(self):
        value_sides = []
        for side in self.sides:
            value_sides.append(side.get_value())
        return sorted(value_sides)


class Quadrangle(Polygon):
    def __init__(self, sides, angles):
        Polygon.__init__(self=self, num_of_vertex=4, sides=sides, angles=angles)
        if not self.__is_quadrangle():
            raise Exception("It isn't a quadrangle")

    def __is_quadrangle(self):
        sum_of_angles = 0
        for angle in self.angles:
            sum_of_angles += angle.get_value_in_degrees()
        if not sum_of_angles == 360:
            return False
        return True


class Parallelogram(Quadrangle):
    def __init__(self, sides, angle_alpha, angle_beta):
        angles = [Angle(value=angle_alpha), Angle(value=angle_beta), Angle(value=angle_alpha), Angle(value=angle_beta)]
        Quadrangle.__init__(self=self, sides=sides, angles=angles)
        if not self.__is_parallelogram():
            raise Exception("It isn't a parallelogram")

    def __is_parallelogram(self):
        sides_sorted = self._Polygon__get_sorted_sides_value()
        if not sides_sorted[0] == sides_sorted[1] or \
                not sides_sorted[2] == sides_sorted[3]:
            return False
        elif not (self.angles[0].get_value_in_degrees() + self.angles[1].get_value_in_degrees() == 180):
            return False
        return True


class Rectangle(Parallelogram):
    def __init__(self, sides):
        Parallelogram.__init__(self=self, sides=sides, angle_alpha=Angle(value=90), angle_beta=Angle(value=90))


class Rhombus(Parallelogram):
    def __init__(self, sides, angle_alpha, angle_beta):
        Parallelogram.__init__(self=self, sides=sides, angle_alpha=angle_alpha, angle_beta=angle_beta)
        if not self.__is_rhombus():
            raise Exception("It isn't a rhombus")

    def __is_rhombus(self):
        sides_sorted = self._Polygon__get_sorted_sides_value()
        if not sides_sorted[0] == sides_sorted[1] == sides_sorted[2] == sides_sorted[3]:
            return False
        return True


class Square(Rhombus, Rectangle):
    def __init__(self, sides):
        Rhombus.__init__(self=self, sides=sides, angle_alpha=Angle(value=90), angle_beta=Angle(value=90))
