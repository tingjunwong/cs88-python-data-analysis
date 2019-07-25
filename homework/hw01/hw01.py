"""Homework 1."""

def odd(number):
    if (number %2==1):
        return True
    else:
        return False
    



from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    "*** YOUR CODE HERE ***"

def distance3d(x1, y1, z1, x2, y2, z2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
    "*** YOUR CODE HERE ***"


def diff(x, y, z):
    if (x+y==z) or (x+z==y) or (z+y==x):
        return True
    else:
        return False




from math import sqrt

def quadratic(a,b,c):

    delta =sqrt(b*b-4*a*c)

    d=-b/2/a+ delta /2/a
    e=-b/2/a- delta/2/a
    return (e,d)

from operator import add, sub

def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
 
print(a_plus_abs_b(1, -2))