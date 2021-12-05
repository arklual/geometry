from . import base
from base import Vector, Point, Angle
import math

class Triangle:
    a = Point(0, 0)
    b = Point(0, 0)
    c = Point(0, 0)

    def __init__(self, point_a, point_b, point_c):
        self.a = point_a
        self.b = point_b
        self.c = point_c
    
    def is_isosceles(self):
        vector1 = Vector(start = self.a, end = self.b)
        vector2 = Vector(start = self.b, end = self.c)
        vector3 = Vector(start = self.c, end = self.a)

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()

        if vector1_value == vector2_value or vector2 == vector3_value or vector3_value==vector1_value:
            return True
        else:
            return False

    def is_rectangular(self):
        ab_vector = Vector(start = self.a, end = self.b)
        ac_vector = Vector(start = self.c, end = self.a)
        bc_vector = Vector(start = self.b, end = self.c)
        
        ang = Angle(ab_vector, ac_vector)
        ang1 = Angle(ab_vector, bc_vector)
        ang2 = Angle(ac_vector, bc_vector)

        angle1 = ang.get_value_in_degrees()
        angle2 = ang1.get_value_in_degrees()
        angle3 = ang2.get_value_in_degrees()

        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            return True
        else:
            return False

    def is_equilateral(self):
        vector1 = Vector(start = self.a, end = self.b)
        vector2 = Vector(start = self.b, end = self.c)
        vector3 = Vector(start = self.c, end = self.a)

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()

        if vector1_value == vector2_value == vector3_value:
            return True
        else:
            return False

    def perimeter(self):
        vector1 = Vector(start = self.a, end = self.b)
        vector2 = Vector(start = self.b, end = self.c)
        vector3 = Vector(start = self.c, end = self.a)

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()

        P = vector3_value + vector2_value + vector1_value

        return P

    def area(self):
        vector1 = Vector(start = self.a, end = self.b)
        vector2 = Vector(start = self.b, end = self.c)
        vector3 = Vector(start = self.c, end = self.a)
        
        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()
        P = vector3_value + vector2_value + vector1_value
        p = P/2
        area = math.sqrt((p*(p-vector1_value)*(p-vector2_value)*(p-vector3_value)))
        
        return area




