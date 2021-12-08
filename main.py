from base import *
import math

class Parallelogram:
	def __init__(self, vec1 = None, vec2 = None, vec3 = None, vec4 = None, ang1 = None, ang2 = None):
		#ang1 - angel between vec1 and vec2 or vec3 and vec4; ang2 - angel between vec2 and vec3 or vec4 and vec1
		data = {}
		self.set_fig(vec1=vec1, vec2=vec2, vec3=vec3, vec4=vec4, ang1=ang1, ang2=ang2)

	def set_fig(self, vec1: float = None, vec2: float = None, vec3: float = None, vec4: float = None, ang1: float = None, ang2: float = None):
		
		self.data = {"v1": vec1,
		"v2":vec2,
		"v3":vec3,
		"v4":vec4,
		"a1":ang1,
		"a2":ang2}
		
		#deliting "None" values
		to_del = []
		for i in self.data:
			if self.data[i] == None:
				to_del.append(i)
		for i in to_del:
			del self.data[i]

	def area(self):
		#TODO: finish function

		key_list = list(self.data.keys())
		
		if ("v1" in key_list) and ("v2" in key_list) and ("a1" in key_list):
			return self.data["v1"].get_value()*self.data["v2"].get_value()*self.data["a1"].get_sin_in_degrees()

		elif ("v3" in key_list) and ("v4" in key_list) and ("a1" in key_list):
		return self.data["v3"].get_value()*self.data["v4"].get_value()*self.data["a1"].get_sin_in_degrees()

		elif ("v2" in key_list) and ("v3" in key_list) and ("a2" in key_list):
			return self.data["v2"].get_value()*self.data["v3"].get_value()*self.data["a2"].get_sin_in_degrees()

		elif ("v1" in key_list) and ("v4" in key_list) and ("a2" in key_list):
			return self.data["v1"].get_value()*self.data["v4"].get_value()*self.data["a2"].get_sin_in_degrees()

		else:
			print ("this function can't search area of parallelogram with given arguments")
