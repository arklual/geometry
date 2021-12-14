# Geometry. What is it?
Geometry is a project with open source code. It is developing by community. 
Geometry have to teach students how to solve the school tasks using the coordinate method from 9 to 11 russian school classes. 

# Documentation
## base.py
#### 1. Class Point
Coordinates of a point are keeped in this class. This is a data structure so there isn't any methods.
#### 2. Class Vector
**Methods**:
```python
def __init__(self, x=None, y=None, start=None, end=None, value=None)
```
We can init vector by:
* x and y
* start poin and end point
* x and value of the vector
* y and value of the vector
```python
def set_coordinates(self, x=None, y=None, start=None, end=None, value=None):
```
This method set vector by arguments(arguments are same as arguments in constructor).
```python
def get_value(self)
```
This method returns a value of the vector.
```python
def get_direction_in_degrees(self)
```
This method returns a direction of the vector in degrees related to Ox.
```python
def get_x(self)
```
This method returns x coordinate of the vector.
```python
def get_y(self)
```
This method returns x coordinate of the vector. <br>

**Operations:**
* Add <br>
This operation returns the vector, that equals sum of vectros.
## Useful links
https://github.com/JnyJny/Geometry/tree/master/Geometry <br>
https://scikit-geometry.github.io/scikit-geometry/arrangements_visibility.html <br>
https://docs.sympy.org/latest/modules/geometry/index.html <br>
https://trinket.io/python/6b7c42a9c3 <br>
https://dev.to/rvodden/writing-a-geometric-solver-in-python-part-2-more-modelling-44md <br>
https://medium.com/codex/solving-coordinate-geometry-problems-with-pure-python-7417619db690 <br>
https://github.com/seominjoon/geosolver <br>
https://github.com/agnimish/PhotoMath <br>
https://ai.facebook.com/blog/using-neural-networks-to-solve-advanced-mathematics-equations/ <br>
