# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:15:07 2022

@author: sam-b
"""

"""Imports the following modules to be used in the code - random"""
import random

"""Create a Class called Agent and define the class with the init function 
and the parameter label as self. Create a self.x and self.y label randomised 
betweent the ingegers 0 and 99. 
The move() method is created to move the agent class a place along the X and Y
axis every time. Tarus code used to prevent spillage outside of the chart"""
class Agent():
    def __init__(self):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100