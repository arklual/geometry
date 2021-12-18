from . import base
from base import Quadrangle, Angle

class Trapezoid(Quadrangle):
    def __init__(self, sides, angles):
        Quadrangle.__init__(self = self, sides = sides, angles = angles)
        if not self.__is_trapezoid():
            raise Exception('it is not trapezoid')
    
    def __is_trapezoid(self):
        # check if two base sides are parallel
        if (self.sides[1].get_x() / self.sides[3].get_x() == self.sides[1].get_y() / self.sides[3].get_y() and self.sides[0].get_x() / self.sides[2].get_x() != self.sides[0].get_y() / self.sides[2].get_y() / self.sides[3].get_x() != self.sides[1].get_y() / self.sides[3].get_y() and self.sides[0].get_x() / self.sides[2].get_x() == self.sides[0].get_y() / self.sides[2].get_y()):
            return True

    def is_isosceles(self):
        ab = self.sides[0].get_value()
        bc = self.sides[1].get_value()
        cd = self.sides[2].get_value()
        da = self.sides[3].get_value()

        if (ab == cd and bc != da) or (bc == da and ab != cd):
            return True


    def is_rectangular(self):

        # sides
        ab = self.sides[0]
        bc = self.sides[1]
        cd = self.sides[2]
        da = self.sides[3]

        # angles between
        ang = Angle(ab, da)
        ang1 = Angle(ab, bc)
        ang2 = Angle(cd, bc)
        ang3 = Angle(da, cd)

        # angles in degrees
        angle1 = ang.get_value_in_degrees()
        angle2 = ang1.get_value_in_degrees()
        angle3 = ang2.get_value_in_degrees()
        angle4 = ang3.get_value_in_degrees()

        if angle1 == 90 or angle2 == 90 or angle3 == 90 or angle4 == 90:
            return True
        else:
            return False
