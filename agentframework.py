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
The move() method is created to move the agent class a place along the X and Y
axis every time. Tarus code used to prevent spillage outside of the chart
The eat() method makes the agents eat what is in the environment, if there are
over 10 units in the environment, it takes 10 away from the environment and 
adds 10 to the store"""
class Agent():
    def __init__(self, environment):
            self._x = random.randint(0,99)
            self._y = random.randint(0,99)
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
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -=10
            self._store +=10
            