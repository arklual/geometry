from base import *

class Polygon:
	def __init__(self, num_of_vertex, sides: list, angles: list):
		if len(sides) != num_of_vertex or len(angles) != num_of_vertex: raise Exception("Entered data isn't correct");
		self.num_of_vertex = int(num_of_vertex)
		self.data = self.set_fig(sides = sides,  angles = angles)

	def set_fig(self, sides: list, angles: list):
		data = {}
		for i in range (len(sides)):
			if sides[i] != None: data["s"+str(i+1)] = sides[i];
			if angles [i] != None: data["a"+str(i+1)] = angles[i];
		return data
	
	def fig(self): return self.data;
	def keys(self): return list(self.data.keys());
	
		

class Quadrangle(Polygon):
	def __init__(self, sides, angles):
		self.data = Polygon(num_of_vertex=4, sides=sides, angles=angles)
		if not self.__is_quadrangle(sides = sides, angles = angles):
			raise Exception("It isn't a quadrangle")

	def __is_quadrangle(self, sides, angles):
		if (len(angles) and len(sides)) == 4: return True;
		else: return False;
		
	def fig(self): return self.data.fig()
		

class Parallelogram(Quadrangle):
	def __init__(self, sides, angles):
		self.data = Quadrangle(sides=sides, angles=angles)
		if not self.__is_parallelogram():
			raise Exception("It isn't a parallelogram")

	def __is_parallelogram(self):
		#TODO: Parallelogram test with support of None-values
		#Do we even need tests? 
		return True
	
	def area (self):
		a = [i for i in ["a1", "a2", "a3","a4"] if i in self.data.keys()]
		s = [i for i in ["s1", "s2", "s3","s4"] if i in self.data.keys()]
		#clac by 2 sides and sin of angle between them
		if ("s1" in s and "s2" in s) and  "a1" in a: return self.data.fig()["s1"].get_value()*self.data.fig()["s2"].get_value()*self.data.fig()["a1"].get_sin();
		if ("s1" in s and "s2" in s) and  "a3" in a: return self.data.fig()["s1"].get_value()*self.data.fig()["s2"].get_value()*self.data.fig()["a3"].get_sin();
		if ("s3" in s and "s4" in s) and  "a1" in a: return self.data.fig()["s3"].get_value()*self.data.fig()["s4"].get_value()*self.data.fig()["a1"].get_sin();
		if ("s3" in s and "s4" in s) and  "a3" in a: return self.data.fig()["s3"].get_value()*self.data.fig()["s4"].get_value()*self.data.fig()["a3"].get_sin();
		
		if ("s2" in s and "s3" in s) and  "a2" in a: return self.data.fig()["s3"].get_value()*self.data.fig()["s2"].get_value()*self.data.fig()["a2"].get_sin();
		if ("s2" in s and "s3" in s) and  "a4" in a: return self.data.fig()["s3"].get_value()*self.data.fig()["s2"].get_value()*self.data.fig()["a4"].get_sin();
		if ("s4" in s and "s1" in s) and  "a2" in a: return self.data.fig()["s1"].get_value()*self.data.fig()["s4"].get_value()*self.data.fig()["a2"].get_sin();
		if ("s4" in s and "s1" in s) and  "a4" in a: return self.data.fig()["s1"].get_value()*self.data.fig()["s4"].get_value()*self.data.fig()["a4"].get_sin();
		#calc by 2 sides (pls, sbd test this piece of shit)
		if "s1" in s and "s2" in s: return self.data.fig()["s1"].get_value()*self.data.fig()["s2"].get_value()*(1/((self.data.fig()["s1"].get_x()*self.data.fig()["s2"].get_x() + self.data.fig()["s1"].get_y()*self.data.fig()["s2"].get_y())/(self.data.fig()["s1"].get_value()*self.data.fig()["s2"].get_value())));
		if "s2" in s and "s3" in s: return self.data.fig()["s3"].get_value()*self.data.fig()["s2"].get_value()*(1/((self.data.fig()["s3"].get_x()*self.data.fig()["s2"].get_x() + self.data.fig()["s3"].get_y()*self.data.fig()["s2"].get_y())/(self.data.fig()["s3"].get_value()*self.data.fig()["s2"].get_value())));
		if "s4" in s and "s3" in s: return self.data.fig()["s3"].get_value()*self.data.fig()["s4"].get_value()*(1/((self.data.fig()["s3"].get_x()*self.data.fig()["s4"].get_x() + self.data.fig()["s3"].get_y()*self.data.fig()["s4"].get_y())/(self.data.fig()["s3"].get_value()*self.data.fig()["s4"].get_value())));
		if "s4" in s and "s1" in s: return self.data.fig()["s1"].get_value()*self.data.fig()["s4"].get_value()*(1/((self.data.fig()["s1"].get_x()*self.data.fig()["s4"].get_x() + self.data.fig()["s1"].get_y()*self.data.fig()["s4"].get_y())/(self.data.fig()["s1"].get_value()*self.data.fig()["s4"].get_value())));
		
		
class Rectangle(Parallelogram):
	def __init__(self, sides):
		self.data = Parallelogram(sides=sides, angles = [Angle(value=90),Angle(value=90),Angle(value=90),Angle(value=90)])
	

class Rhombus(Parallelogram):
	def __init__(self, side, angles):
		self.data = Parallelogram(sides=[side,side,side,side], angles = angles) #finish this..
		if not self.__is_rhombus():
			raise Exception("It isn't a rhombus")

	def __is_rhombus(self): return True;


class Square(Rhombus, Rectangle):
	def __init__(self, side):
		self.data = Rhombus.__init__(self=self, side=side, angles = [Angle(value=90),Angle(value=90),Angle(value=90),Angle(value=90)]) 
