from base import *


class Polygon:
	def __init__(self, num_of_vertex: int, sides: list, angles: list):
		if (len(sides) and len(angles)) != num_of_vertex: raise Exception("Entered data isn't correct");
		self.num_of_vertex = num_of_vertex
		self.sides = sides
		self.angles = angles

	def __get_sorted_sides_value(self):
		value_sides = []
		for side in self.sides:
			value_sides.append(side.get_value())
		return sorted(value_sides)

	
class Quadrangle(Polygon):
	def __init__(self, sides, angles):
		Polygon(num_of_vertex=4, sides=sides, angles=angles)
		self.angles = angles
		self.sides = sides
		if not self.__is_quadrangle(): raise Exception("It isn't a quadrangle");

	def __is_quadrangle(self):
		if len(self.angles) == len(self.sides) == 4: return True;

class Parallelogram(Quadrangle):
	def __init__(self, side1=None, side2=None, angle1=None, angle2=None):
		Quadrangle(sides=[side1, side2, side1, side2], angles=[angle1, angle2, angle1, angle2])
		self.angle1,self.angle2, self.side2, self.side1 = angle1, angle2, side2, side1
	
	def area (self):
		angle1, angle2, side2, side1 = self.angle1,self.angle2, self.side2, self.side1
		if (side1 and side2 and angle1) != None: return side1.get_value()*side2.get_value()*angle1.get_sin();
		elif (side1 and side2 and angle2) != None: return side1.get_value()*side2.get_value()*angle2.get_sin();
		#place to calc by 2 sides [shit] code

class Rectangle(Parallelogram):
	def __init__(self, side1 = None, side2 = None):
		Parallelogram(side1=side1, side2=side2, angle1=Angle(value=90), angle2=Angle(value=90))

class Rhombus(Parallelogram):
	def __init__(self, side=None, angle2=None, angle1=None):
		Parallelogram(side1=side, side2=side, angle1=angle1, angle2=angle2)

class Square(Rhombus, Rectangle):
	def __init__(self, side=None):
		Rhombus(side = side, angle1=Angle(value=90), angle2=Angle(value=90))
