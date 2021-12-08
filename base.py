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

    def __init__(self, x=None, y=None, start=None, end=None, value=None):
        self.set_coordinates(x=x, y=y, start=start, end=end, value=value)

    def set_coordinates(self, x=None, y=None, start=None, end=None, value=None):
        if x is not None and y is not None and start is None and end is None and value is None:
            self.__x = float(x)
            self.__y = float(y)
        elif x is None and y is None and start is not None and end is not None and value is None:
            self.__calc_x_and_y(start, end)
        elif x is not None and y is None and start is None and end is None and value is not None:
            self.__x = float(x)
            self.__calc_y_by_value_and_x(value=value)
        elif x is None and y is not None and start is None and end is None and value is not None:
            self.__y = float(y)
            self.__calc_x_by_value_and_y(value=value)
        else:
            raise Exception("Too many or too few arguments")

    def __calc_x_and_y(self, start: Point, end: Point):
        self.__x = float(end.x - start.x)
        self.__y = float(end.y - start.y)

    def __calc_x_by_value_and_y(self, value):
        self.__x = math.sqrt(self.get_value() ** 2 - self.__y ** 2)

    def __calc_y_by_value_and_x(self, value):
        self.__y = math.sqrt(self.get_value() ** 2 - self.__x ** 2)

    def get_value(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def get_direction_in_degrees(self):
        return Angle(value=math.degrees(math.atan2(self.__y, self.__x)))

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
            self.__value = value
            self.__correct_value()
        else:
            raise Exception("Too many or too few arguments")

    def __correct_value(self):
        while self.__value > 360:
            self.__value -= 360

    def get_value_in_degrees(self):
        return self.__value

    def get_sin_in_degrees(self):
        return math.sin(math.radians(self.__value))

    def get_cos_in_degrees(self):
        return math.cos(math.radians(self.__value))

    def get_tan_in_degrees(self):
        return math.tan(math.radians(self.__value))

    def get_value_in_radians(self):
        return math.radians(self.__value)

    def get_sin_in_radians(self):
        return math.sin(self.__value)

    def get_cos_in_radians(self):
        return math.cos(self.__value)

    def get_tan_in_radians(self):
        return math.tan(self.__value)

    @staticmethod
    def __get_angle_between_two_vectors(vector1, vector2):
        return Angle(value=math.degrees(
            math.atan2(vector2.get_y(), vector2.get_x()) - math.atan2(vector1.get_y(), vector1.get_x())))
