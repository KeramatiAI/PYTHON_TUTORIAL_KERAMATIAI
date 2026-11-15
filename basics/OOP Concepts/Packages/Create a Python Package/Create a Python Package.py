"""
Create a Python Package
"""

# mathfunctions.py
def sum(x, y):
    val = x + y
    return val


def average(x, y):
    val = (x + y) / 2
    return val


def power(x, y):
    val = x ** y
    return val


"""
Create
another
Python
script −
"""

# areafunctions.py
def rectangle(w, h):
    area = w * h
    return area


def circle(r):
    import math
    area = math.pi * math.pow(r, 2)
    return area


"""
Let us now test the
myexample
package
with the help of a Python script above this package folder.Refer to the folder structure above."""

# example.py
from mypackage.areafunctions import rectangle

print("Area :", rectangle(10, 20))

from mypackage.mathsfunctions import average

print("average:", average(10, 20))
"""
This
program
imports
functions
from mypackage.If the

above
script is executed, you
should
get
following
output −
"""

Area: 200
average: 15.0