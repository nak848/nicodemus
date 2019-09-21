#   File: Geom.py
#   Description: This file contains several classes that create Points, Circles, and Rectangles
#                It shows the functions through main and the geom txt file
#   Student Name: Nicolas Kim
#   Student UT EID: nak848
#   Course Name:    CS 313E
#   Unique Number:
#   Date Create: 9/20/19
#   Date Last Modified: 9/21/2019


import math


class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute circumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return self.center.dist(p) < self.radius

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        distance = self.center.dist(c.center)
        return ((distance + c.radius) > self.radius) and (c.radius < (distance + self.radius))

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe(self, r):
        distance = r.ul.dist(r.lr)
        self.radius = distance / 2
        self.center.x = r.length() / 2 + r.ul.x
        self.center.y = r.width() / 2 + r.lr.y

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return abs(self.radius) == abs(other.radius)


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if (ul_x < lr_x) and (ul_y > lr_y):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return float(abs(self.lr.x - self.ul.x))

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return float(abs(self.ul.y - self.lr.y))

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return (float(abs(self.ul.y - self.lr.y)) * 2) + (float(abs(self.lr.x - self.ul.x)) * 2)

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return float(abs(self.ul.y - self.lr.y)) * float(abs(self.lr.x - self.ul.x))

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return (self.ul.x < p.x < self.lr.x) and (self.lr.y < p.y < self.ul.y)

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return ((self.ul.x < r.ul.x < self.lr.x) and (self.lr.x > r.lr.x > self.ul.x)) and (
                (self.ul.y > r.ul.y > self.lr.y) and (self.lr.y < r.lr.y < self.ul.y))

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap(self, r):
        if self.ul == r.ul and self.lr == r.lr:
            return True
        if (self.ul.x > r.lr.x) or (self.lr.x < r.ul.x):
            return False
        if (self.ul.y < r.lr.y) or (self.lr.y > r.ul.y):
            return False
        else:
            return True

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe(self, c):
        left = c.center.x - c.radius
        right = c.center.x + c.radius
        top = c.center.y + c.radius
        bottom = c.center.y - c.radius
        return Rectangle(left, top, right, bottom)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        return self.ul == other.ul and self.lr == other.lr


def is_or_not(boolean):
    if boolean:
        return 'is'
    if not boolean:
        return 'is not'


def main():
    # Reading the file
    file = open('geom.txt', 'r')
    coordinate_list = []
    for line in file:
        file_line = line.split()
        i = file_line.index('#')
        del file_line[i:]
        file_line = [float(x) for x in file_line]
        coordinate_list.append(file_line)

    # Calling the classes and creating object instances
    P = Point(coordinate_list[0][0], coordinate_list[0][1])
    Q = Point(coordinate_list[1][0], coordinate_list[1][1])
    C = Circle(coordinate_list[2][0], coordinate_list[2][1], coordinate_list[2][2])
    D = Circle(coordinate_list[3][0], coordinate_list[3][1], coordinate_list[3][2])
    G = Rectangle(coordinate_list[4][0], coordinate_list[4][1], coordinate_list[4][2], coordinate_list[4][3])
    H = Rectangle(coordinate_list[5][0], coordinate_list[5][1], coordinate_list[5][2], coordinate_list[5][3])

    # Formatting to match the specs
    print('Coordinates of P:', P)
    print('Coordinates of Q:', Q)
    print('Distance between P and Q:', P.dist(Q))
    print('Circle C:', C)
    print('Circle D:', D)
    print('Circumference of C:', C.circumference())
    print('Area of D:', D.area())
    print('P', is_or_not(C.point_inside(P)), 'inside C')
    print('C', is_or_not(D.circle_inside(C)), 'inside D')
    print('C', is_or_not(C.circle_overlap(D)), 'intersecting D')
    print('C', is_or_not(C.__eq__(D)), 'equal to D')
    print('Rectangle G:', G)
    print('Rectangle H:', H)
    print('Length of G:', G.length())
    print('Width of H:', H.width())
    print('Perimeter of G:', G.perimeter())
    print('Area of H:', H.area())
    print('P', is_or_not(G.point_inside(P)), 'inside G')
    print('G', is_or_not(H.rectangle_inside(G)), 'inside H')
    print('G', is_or_not(H.rectangle_overlap(G)), 'overlapping H')
    print('Circle that circumscribes G:', C.circle_circumscribe(G))
    print('Rectangle that circumscribes D:', G.rectangle_circumscribe(D))
    print('Rectangle G', is_or_not(G.__eq__(H)), 'equal to H')

if __name__ == "__main__":
    main()
