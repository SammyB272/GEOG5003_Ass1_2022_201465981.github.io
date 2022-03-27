# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:45:26 2022

@author: sam-b
"""


"""Imports the following modules to be used in the code - random, operator,
matplotlib.pyplot"""
import random
import operator
import matplotlib.pyplot

"""Create an empty list called with the variable name agents"""
agents = []

"""Create two sets of coordinate variables (yx0 and yx1) using the random.randint
function to include values between 0 and 99 (Now Redundant - Replaced by agents list)
y0 = random.randint(0,99)
x0 = random.randint(0,99)

y1 = random.randint(0,99)
x1 = random.randint(0,99)"""

"""Create a set of Y and X variables, to represent coordinates, 
and assign them the integer 50 (Now Redundant - Replaced by random.randint function)
y0 = 50
x0 = 50"""

"""Create a second set of coordinate variables (Now Redundant - Replaced by 
random.randint function)
y1 = 50
x1 = 50"""

"""Append random integers between 0 and 99 to the agents list, the list will
be a 2 dimensional list, with each column containing a value relating to an
X and Y coordinate"""
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])
              
"""Create red and blue variables to encompass the most eastern and most western
coordinates from the list agents"""
red = max(agents, key=operator.itemgetter(1))
blue = min(agents, key=operator.itemgetter(1))

"""Using the if/else statements increase or decrase the value of the coordinate
variables in steps of 1, dependant on if the random number is greater than 0.5
(Now Redundant - Replaced by random.randint function)
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
 (Now Redundant - Replaced by random.randint function)
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
y_axis_calulation = (agents[0][0] - agents[1][0]) ** 2
x_axis_calcualtion = (agents[0][1] - agents[1][1]) ** 2

sum_of_axis_calculations = (y_axis_calulation + x_axis_calcualtion)

hypotenuse = sum_of_axis_calculations ** 0.5


"""Print the two sets of coordinate variables to test they work(Now Redundant 
- Replaced by agents list)
print(y0, x0)
print(y1, x1)"""

"""Prints the agents varibale to test the container works"""
print(agents)

"""Prints the maximum coordinate from the agents, using the operator.itemgetter
function to choose the second (or easterly) variable in each column in the list"""
print(max(agents, key=operator.itemgetter(1)))

"""Print the straight line distance between the yx0 and yx1 coordinate variables,
to check answer on calulator"""
print(hypotenuse)

"""print red and blue variables to test values and see output (Now Redundant -
testing only for purpose of determining code)
print(red)
print(blue)"""

"""Plot the coordinate columns contained in the agents list onto a graph, with
the X and Y axis ranging from 0 - 99, using the created red and blue variables
to colour red as most estern and blue as most western"""
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(red[1],red[0],color='red')
matplotlib.pyplot.scatter(blue[1],blue[0],color='blue')
matplotlib.pyplot.show()

"""Test the document properly runs code (Now Redundant - relpaced by model)
print ("Hello World")"""