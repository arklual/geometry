from . import base
from base import Vector, Point, Angle
import math
import numpy as np

class Triangle:
    
    a = Point(0, 0)
    b = Point(0, 0)
    c = Point(0, 0)

    def __init__(self, point_a, point_b, point_c):
        self.a = point_a
        self.b = point_b
        self.c = point_c

        # проверить существует ли такой треугольник
    
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

        # проверить равны ли длины каких-то двух сторон

    def is_rectangular(self):
        # проверить равен ли угол 90 градусов между какими-то векторами 
        #vector1 = np.array([[a.x, b.x], [a.y, b.y]])
        #vector2 = np.array([[a.x, c.x], [a.y], c.y])
        #vector3 = np.array([[b.x, c.x], [b.y, c.y]])

        ab_vector = Vector(start = self.a, end = self.b)
        ac_vector = Vector(start = self.c, end = self.a)
        bc_vector = Vector(start = self.b, end = self.c)
        
        # between v1 and v2
        ang = Angle(ab_vector, ac_vector)
        ang1 = Angle(ab_vector, bc_vector)
        ang2 = Angle(ac_vector, bc_vector)


        angle1 = ang.get_value_in_degrees()
        angle2 = ang1.get_value_in_degrees()
        angle3 = ang2.get_value_in_degrees()


        #sc_multiplication_of_v1_and_v2 = float(np.dot(vector1, vector2))
        # vector1_length = Vector.get_value(x = (a.x - b.x), y = (a.y-b.y))
        # vector2_length = Vector.get_value(x = (a.x-c.x), y = (a.y - c.y))
        # magnitude_of_v1_and_v2 = vector1_length * vector2_length
        # cosine_of_angle_1 = sc_multiplication_of_v1_and_v2/magnitude_of_v1_and_v2


        # between v2 and v3
        # sc_multiplication_of_v2_and_v3 = float(np.dot(vector1, vector2))
        # vector3_length = Vector.get_value(x = (b.x-c.x), y = (b.y-c.y))
        # vector2_length = Vector.get_value(x = (a.x-c.x), y = (a.y - c.y))
        # magnitude_of_v3_and_v2 = vector3_length * vector2_length
        # cosine_of_angle_2 = sc_multiplication_of_v2_and_v3/magnitude_of_v3_and_v2

        # between v1 and v3
        # sc_multiplication_of_v1_and_v3 = float(np.dot(vector1, vector3))
        # magnitude_of_v1_and_v2 = vector1_length * vector3_length
        # cosine_of_angle_3 = sc_multiplication_of_v1_and_v3/magnitude_of_v1_and_v2


        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            return True
        else:
            return False




        

    def is_equilateral(self):
        # проверить рав-во всех векторов
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
        # side1 + side2 + side3
        vector1 = Vector(start = self.a, end = self.b)
        vector2 = Vector(start = self.b, end = self.c)
        vector3 = Vector(start = self.c, end = self.a)

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()

        P = vector3_value + vector2_value + vector1_value

        return P
        

    def area(self):
        # count half of perimeter as p
        # area = math.sqrt((p*(p-side1)*(p-side2)*(p-side3)))
        # vector1 = Vector(x = (self.a.x - self.b.x), y = (self.a.y-self.b.y))
        # vector2 = Vector(x = (self.b.x-self.c.x), y = (self.b.y-self.c.y))
        # vector3 = Vector(x = (self.a.x-self.c.x), y = (self.a.y - self.c.y))
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




