import math


class Point:
    x = float(0)
    y = float(0)

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class Vector:
    __x = float(0)
    __y = float(0)

    def __init__(self, x=None, y=None, start=None, end=None):
        self.set_coordinates(x=x, y=y, start=start, end=end)

    def set_coordinates(self, x=None, y=None, start=None, end=None):
        if x and y and not start and not end:
            self.__x = float(x)
            self.__y = float(y)
        elif start and end and not x and not y:
            self.__calc_x_and_y(start, end)
        else:
            raise Exception("Too many or too few arguments")

    def __calc_x_and_y(self, start: Point, end: Point):
        self.__x = float(end.x - start.x)
        self.__y = float(end.y - start.y)

    def get_value(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_direction_in_degrees(self):
        return Angle(value=math.degrees(math.atan2(self.y, self.x)))

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Angle:
    __value = float(0)

    def __init__(self, vector1=None, vector2=None, value=None):
        self.set_value(vector1=vector1, vector2=vector2, value=value)

    def set_value(self, vector1=None, vector2=None, value=None):
        if vector1 and vector2 and not value:
            self.__value = self.__get_angle_between_two_vectors(vector1=vector1, vector2=vector2)
        elif value and not vector1 and not vector2:
            while value > 360:
                value -= 360
            self.__value = value
        else:
            raise Exception("Too many or too few arguments")

    def get_value(self):
        return self.__value

    def get_sin(self):
        return math.degrees(math.sin(self.__value))

    def get_cos(self):
        return math.degrees(math.cos(self.__value))

    def get_tan(self):
        return math.degrees(math.tan(self.__value))

    @staticmethod
    def __get_angle_between_two_vectors(vector1, vector2):
        return Angle(value=math.degrees(
            math.atan2(vector2.get_y(), vector2.get_x()) - math.atan2(vector1.get_y(), vector1.get_x())))
