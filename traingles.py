from . import base
from base import Vector, Point, Angle
import math
import numpy as np

class Triangle:
    
    point_a = Point(0, 0)
    point_b = Point(0, 0)
    point_c = Point(0, 0)

    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

        # проверить существует ли такой треугольник
    
    def is_isosceles(a, b, c):
        vector1 = Vector(x = a.x - b.x, y = a.y - b.y)
        vector2 = Vector(x = b.x - c.x, y = b.y - c.y)
        vector3 = Vector(x = a.x - c.x, y = a.y - c.x)

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()

        if vector1_value == vector2_value or vector2 == vector3_value or vector3_value==vector1_value:
            return True
        else:
            return False

        # проверить равны ли длины каких-то двух сторон

    def is_rectangular(a, b, c):
        # проверить равен ли угол 90 градусов между какими-то векторами 
        #vector1 = np.array([[a.x, b.x], [a.y, b.y]])
        #vector2 = np.array([[a.x, c.x], [a.y], c.y])
        #vector3 = np.array([[b.x, c.x], [b.y, c.y]])

        ab_vector = Vector(x = a.x - b.x, y = a.y - b.y)
        ac_vector = Vector(x = a.x - c.x, y = a.y - c.x)
        bc_vector = Vector(x = b.x - c.x, y = b.y - c.y)
        
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




        

    def is_equilateral(a, b, c):
        # проверить рав-во всех векторов
        vector1 = Vector(x = (a.x - b.x), y = (a.y-b.y))
        vector2 = Vector(x = (b.x-c.x), y = (b.y-c.y))
        vector3 = Vector(x = (a.x-c.x), y = (a.y - c.y))

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()

        if vector1_value == vector2_value == vector3_value:
            return True
        else:
            return False

    def perimeter(a, b, c):
        # side1 + side2 + side3
        vector1 = Vector(x = (a.x - b.x), y = (a.y-b.y))
        vector2 = Vector(x = (b.x-c.x), y = (b.y-c.y))
        vector3 = Vector(x = (a.x-c.x), y = (a.y - c.y))

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()

        P = vector3_value + vector2_value + vector1_value

        return P
        

    def area(a, b, c):
        # count half of perimeter as p
        # area = math.sqrt((p*(p-side1)*(p-side2)*(p-side3)))
        vector1 = Vector(x = (a.x - b.x), y = (a.y-b.y))
        vector2 = Vector(x = (b.x-c.x), y = (b.y-c.y))
        vector3 = Vector(x = (a.x-c.x), y = (a.y - c.y))

        vector1_value = vector1.get_value()
        vector2_value = vector2.get_value()
        vector3_value = vector3.get_value()
        P = vector3_value + vector2_value + vector1_value
        p = P/2
        area = math.sqrt((p*(p-vector1_value)*(p-vector2_value)*(p-vector3_value)))

        return area




