from base import Vector

vector1 = Vector(x=1, y=1)
vector2 = Vector(x=3, y=6)
vector3 = Vector(x=5, y=1)

a = vector1.get_value()
b = vector2.get_value()
c = vector3.get_value()

if a == b:
    print("Solved")
elif b == c:
    print("Solved")
elif a == c:
    print("Solved")
else:
    print("Задача не решена")
