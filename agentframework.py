# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:15:07 2022

@author: sam-b
"""

"""Imports the following modules to be used in the code - random"""
import random

"""Create a Class called Agent and define the class with the init function 
and the parameter label as self. Create a self.x and self.y label randomised 
betweent the ingegers 0 and 99. Create a self.environment label to take in the 
environments list created in the model.py and enbed it into the Agent object.Create
a self.store label to store 'eaten' values.

The get() method is used to only retrieve the __init__ data without being able to
change the values. The set() method allows the user to chnage the value of the 
object different to that assigned from __init__. 

The __str__() method allows a default print return when called in the main code. 

The move() method is created to move the agent class a place along the X and Y
axis every time. Tarus code used to prevent spillage outside of the chart.

The eat() method makes the agents eat what is in the environment, if there are
over 10 units in the environment, it takes 10 away from the environment and 
adds 10 to the store. The elif satement will remove the remaining value from the
envronment if it is under 10 using the modulo function.

The greedy() method returns 100 units beck to the envronment and loses them from
the store after 100 units have been consumed."""

class Agent():
    def __init__(self, environment):
            self._x = random.randint(0,300)
            self._y = random.randint(0,300)
            self._store = 0
            self.environment = environment
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
    def getstore(self):
        return self._store
    def setstore(self, value):
        self._store = value
    def __str__(self):
        return("The XY Coordinate is " + str(self._x) + " " + str(self._y) + ", The store value is " + str(self._store))
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300
        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -=10
            self._store +=10
        elif self.environment[self._y][self._x] < 10:
            self.environment[self._y][self._x] -=self.environment % 10
    def greedy(self):
        if self._store > 100:
            self.environment[self._y][self._x] +=100
            self._store -=100
            