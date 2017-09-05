#This program contains functions that evaluate formulas used in geometry
#
#Your name
#August 22, 2017
import math

def triangle_area(b, h):
        a = (1/2) * b * h
        return a

def circle_area(r):
        a = math.pi * r**2
        return a

#function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b, h):
        a = b * h
        return a

def trapezoid_area(a, b, h):
        a = (a + b / 2) * h
        return a

def rectangle_volume(w, h, l):
        a = w * h * l
        return a

def cone_volume(r, h):
        a = math.pi * r**2 * (h/3)
        return a

def sphere_volume(r):
        a = (4/3) * math.pi * r**3
        return a

def rectangle_sa(w, l, h):
        a = 2*((w * l)+(h * l)+(h * w))
        return a

def sphere_sa(r):
        a = 4*(math.pi * r**2)
        return a

def triangle_hypo(a, b):
        a = a**2 + b**2
        return a

#function calls
print(parallelogram_area(5,5))
print(trapezoid_area(3,4,5))
print(rectangle_volume(2,2,2))
print(cone_volume(2,4))
print(sphere_volume(4))
print(rectangle_sa(2,3,4))
print(sphere_sa(2))
print(triangle_hypo(4,4))

#challenge
#def herons_formula(a, b, c):
        #s = a + b + c
        #d = **(1/2)(s*(s - a)*(s - b)*(s - c)
        #return d
#print(herons_formula(5,10,15))
                   




