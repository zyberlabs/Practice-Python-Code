#!/usr/bin/python

class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        total = self.angle1 + self.angle2 + self.angle3
        if total == 180:
            return True
        else:
            return False

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
	self.angle1 = self.angle
	self.angle2 = self.angle
	self.angle3 = self.angle

my_triangle = Triangle(10,90,80)
print my_triangle.number_of_sides
print my_triangle.check_angles()

triangle = Equilateral()
print triangle.angle
print triangle.angle1
