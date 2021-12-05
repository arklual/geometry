from polygons.polygons import *

sides = [Vector(value=6, y=4.8), Vector(value=10, y=8), Vector(value=6, y=4.8), Vector(value=10, y=8)]
p = Quadrangle(sides, angles=[Angle(value=20), Angle(value=20), Angle(value=20), Angle(value=20)])
print(p.get_area())
