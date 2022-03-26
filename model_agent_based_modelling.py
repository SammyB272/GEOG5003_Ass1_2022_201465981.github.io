# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:45:26 2022

@author: sam-b
"""


"""Import the random module to be used in the code"""
import random


"""Create two sets of coordinate variables (yx0 and yx1) using the random.randint
function to include values between 0 and 99"""
y0 = random.randint(0,99)
x0 = random.randint(0,99)

y1 = random.randint(0,99)
x1 = random.randint(0,99)

"""Create a set of Y and X variables, to represent coordinates, 
and assign them the integer 50 (Now Redundant)
y0 = 50
x0 = 50"""

"""Create a second set of coordinate variables (Now Redundant)
y1 = 50
x1 = 50"""


"""Using the if/else statements increase or decrase the value of the coordinate
variables in steps of 1, dependant on if the random number is greater than 0.5
(Now Redundant)
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1"""

"""Randomise the second set of coordinate varibales using the same method as above
 (Now Redundant)
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1"""


"""Perform Pythagorus theorem to calculate the straight line distance 
between the yx0 and the yx1 coordinate variables"""
y_axis_calulation = (y0 - y1) ** 2
x_axis_calcualtion = (x0 - x1) ** 2

sum_of_axis_calculations = (y_axis_calulation + x_axis_calcualtion)

hypotenuse = sum_of_axis_calculations ** 0.5


"""Print the two sets of coordinate variables to test they work"""
print(y0, x0)
print(y1, x1)

"""Print the straight line distance between the yx0 and yx1 coordinate variables,
to check answer on calulator"""
print(hypotenuse)

"""Test the document properly runs code (Now Redundant)
print ("Hello World")"""